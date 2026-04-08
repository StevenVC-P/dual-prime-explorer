"""Reloadable web-runtime helpers for the browser app."""

from __future__ import annotations

import importlib
import json
from dataclasses import asdict
from math import log
from typing import Any, TypedDict

from .web_limits import MAX_WEB_END, MAX_WEB_RANGE_SIZE


class WebRuntime(TypedDict):
    page_by_route: dict[str, Any]
    page_registry: dict[str, str]
    app_css: str
    explorer_js: str
    analysis_js: str
    theory_js: str
    experiments_js: str
    ads_txt: str


def _load_core_module(dev_mode: bool = False) -> Any:
    core_module = importlib.import_module("dual_prime_explorer.core")
    if dev_mode:
        core_module = importlib.reload(core_module)
    return core_module


def _histogram(values: list[int]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def _average(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _aggregate_factorization_records(records: list[dict[str, Any]]) -> dict[str, Any]:
    if not records:
        return {
            "numbers": [],
            "average_divisor_count": 0.0,
            "divisor_count_histogram": {},
            "distinct_prime_factor_count_histogram": {},
            "squarefree_count": 0,
            "squarefree_frequency": 0.0,
            "average_largest_prime_factor": 0.0,
        }

    return {
        "numbers": [record["number"] for record in records],
        "average_divisor_count": _average([float(record["divisor_count"]) for record in records]),
        "divisor_count_histogram": _histogram([int(record["divisor_count"]) for record in records]),
        "distinct_prime_factor_count_histogram": _histogram(
            [int(record["distinct_prime_factor_count"]) for record in records]
        ),
        "squarefree_count": sum(1 for record in records if record["is_squarefree"]),
        "squarefree_frequency": sum(1 for record in records if record["is_squarefree"]) / len(records),
        "average_largest_prime_factor": _average(
            [float(record["largest_prime_factor"]) for record in records]
        ),
    }


def _build_range_density_analysis(
    start: int,
    end: int,
    twin_pairs: list[list[int]],
    primes: list[int],
    density_window: int,
) -> dict[str, Any]:
    range_size = end - start + 1
    global_prime_density = len(primes) / range_size if range_size else 0.0
    global_twin_pair_density = len(twin_pairs) / range_size if range_size else 0.0
    pair_density_stats: list[dict[str, Any]] = []

    for left, right in twin_pairs:
        center = (left + right) // 2
        window_start = max(start, center - density_window)
        window_end = min(end, center + density_window)
        window_size = window_end - window_start + 1
        primes_in_window = sum(window_start <= prime <= window_end for prime in primes)
        twin_pairs_in_window = sum(
            window_start <= pair_left and pair_right <= window_end
            for pair_left, pair_right in twin_pairs
        )
        local_prime_density = primes_in_window / window_size if window_size else 0.0
        local_twin_pair_density = twin_pairs_in_window / window_size if window_size else 0.0
        prime_density_ratio = (
            local_prime_density / global_prime_density if global_prime_density else 0.0
        )
        pair_density_stats.append(
            {
                "pair": [left, right],
                "center": center,
                "window_start": window_start,
                "window_end": window_end,
                "primes_in_window": primes_in_window,
                "twin_pairs_in_window": twin_pairs_in_window,
                "local_prime_density": local_prime_density,
                "local_twin_pair_density": local_twin_pair_density,
                "global_prime_density": global_prime_density,
                "global_twin_pair_density": global_twin_pair_density,
                "prime_density_ratio": prime_density_ratio,
            }
        )

    return {
        "window_radius": density_window,
        "pair_density_stats": pair_density_stats,
        "global_prime_density": global_prime_density,
        "global_twin_pair_density": global_twin_pair_density,
        "average_local_prime_density": _average(
            [record["local_prime_density"] for record in pair_density_stats]
        ),
        "average_local_twin_pair_density": _average(
            [record["local_twin_pair_density"] for record in pair_density_stats]
        ),
        "average_prime_density_ratio": _average(
            [record["prime_density_ratio"] for record in pair_density_stats]
        ),
    }


def _build_expected_vs_observed(
    core_module: Any,
    start: int,
    end: int,
    twin_pairs: list[list[int]],
) -> list[dict[str, Any]]:
    checkpoints = [point for point in core_module._normalized_sample_points(end, None) if point >= start]
    if end not in checkpoints:
        checkpoints.append(end)
    checkpoints = sorted(set(checkpoints))

    records: list[dict[str, Any]] = []
    for checkpoint in checkpoints:
        actual_count = sum(1 for _, right in twin_pairs if right <= checkpoint)
        expected_count = checkpoint / (log(checkpoint) ** 2) if checkpoint > 1 else 0.0
        ratio = actual_count / expected_count if expected_count > 0 else None
        records.append(
            {
                "limit": checkpoint,
                "actual_count": actual_count,
                "expected_count": expected_count,
                "ratio": ratio,
            }
        )
    return records


def _filter_analysis_payload(
    core_module: Any,
    raw_payload: dict[str, Any],
    start: int,
    end: int,
    density_window: int,
) -> dict[str, Any]:
    primes = [prime for prime in raw_payload["primes"] if start <= prime <= end]
    twin_pairs = [
        pair for pair in raw_payload["twin_pairs"]
        if start <= pair[0] and pair[1] <= end
    ]
    pair_centers = [(left + right) // 2 for left, right in twin_pairs]
    paired_prime_set = {prime for pair in twin_pairs for prime in pair}
    number_classifications = [
        row for row in raw_payload["number_classifications"]
        if start <= row["number"] <= end
    ]
    pair_structures = [
        row for row in raw_payload["pair_structures"]
        if start <= row["pair"][0] and row["pair"][1] <= end
    ]
    center_mod6_counts = _histogram([int(row["center_mod6"]) for row in pair_structures])
    center_mod30_counts = _histogram([int(row["center_mod30"]) for row in pair_structures])
    pair_starts = [pair[0] for pair in twin_pairs]
    pair_start_gaps = [current - previous for previous, current in zip(pair_starts, pair_starts[1:])]
    center_gaps = [current - previous for previous, current in zip(pair_centers, pair_centers[1:])]

    center_records = [
        record for record in raw_payload["factorization_analysis"]["center_records"]
        if start <= record["number"] <= end
    ]
    non_center_even_records = [
        record for record in raw_payload["factorization_analysis"]["non_center_even_records"]
        if start <= record["number"] <= end
    ]

    return {
        "start": start,
        "limit": end,
        "primes": primes,
        "twin_pairs": twin_pairs,
        "paired_primes": [prime for prime in primes if prime in paired_prime_set],
        "unpaired_primes": [prime for prime in primes if prime not in paired_prime_set],
        "pair_centers": pair_centers,
        "number_classifications": number_classifications,
        "pair_structures": pair_structures,
        "center_mod6_counts": center_mod6_counts,
        "center_mod30_counts": center_mod30_counts,
        "gap_analysis": {
            "pair_start_gaps": pair_start_gaps,
            "center_gaps": center_gaps,
            "pair_start_gap_histogram": _histogram(pair_start_gaps),
            "center_gap_histogram": _histogram(center_gaps),
        },
        "factorization_analysis": {
            "center_records": center_records,
            "non_center_even_records": non_center_even_records,
            "center_aggregate": _aggregate_factorization_records(center_records),
            "non_center_even_aggregate": _aggregate_factorization_records(non_center_even_records),
        },
        "density_analysis": _build_range_density_analysis(start, end, twin_pairs, primes, density_window),
        "expected_vs_observed": _build_expected_vs_observed(core_module, start, end, twin_pairs),
    }


def build_analysis_payload(
    end: int,
    density_window: int = 50,
    *,
    start: int = 1,
    dev_mode: bool = False,
) -> dict[str, Any]:
    """Return a JSON-ready payload for the web UI."""
    if start < 1:
        raise ValueError("start must be at least 1")
    if end < 2:
        raise ValueError("end must be at least 2")
    if start > end:
        raise ValueError("start must be less than or equal to end")
    if end > MAX_WEB_END:
        raise ValueError(f"end must be less than or equal to {MAX_WEB_END:,} for the web app")
    if (end - start + 1) > MAX_WEB_RANGE_SIZE:
        raise ValueError(f"range size must be {MAX_WEB_RANGE_SIZE:,} numbers or fewer")

    core_module = _load_core_module(dev_mode)
    raw_payload = asdict(core_module.analyze_primes_up_to(end, density_window=density_window))
    filtered_payload = _filter_analysis_payload(core_module, raw_payload, start, end, density_window)
    return json.loads(json.dumps(filtered_payload))


def load_web_runtime(dev_mode: bool = False) -> WebRuntime:
    """Load the current web pages and static assets."""
    web_content = importlib.import_module("dual_prime_explorer.web_content")
    web_pages = importlib.import_module("dual_prime_explorer.web_pages")
    web_assets = importlib.import_module("dual_prime_explorer.web_assets")

    if dev_mode:
        web_content = importlib.reload(web_content)
        web_pages = importlib.reload(web_pages)
        web_assets = importlib.reload(web_assets)

    return {
        "page_by_route": web_pages.PAGE_BY_ROUTE,
        "page_registry": web_assets.build_page_registry(),
        "app_css": web_assets.APP_CSS,
        "explorer_js": web_assets.EXPLORER_JS,
        "analysis_js": web_assets.ANALYSIS_JS,
        "theory_js": web_assets.build_theory_js(),
        "experiments_js": web_assets.EXPERIMENTS_JS,
        "ads_txt": web_assets.ADS_TXT,
    }
