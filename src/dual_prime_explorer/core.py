"""Core algorithms for twin-prime exploration."""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt, log
from typing import Iterable


@dataclass(frozen=True)
class NumberClassification:
    """Classification details for a single number in the search range."""

    number: int
    number_type: str
    is_prime: bool
    prime_role: str
    is_edge_case: bool
    structural_region: str
    is_pair_center: bool
    center_of_pair: tuple[int, int] | None
    adjacent_prime_count: int
    adjacent_prime_role: str
    prime_divisors: tuple[int, ...]
    all_divisors: tuple[int, ...]
    divisor_count: int | None
    smallest_prime_factor: int | None
    distinct_prime_factor_count: int | None


@dataclass(frozen=True)
class TwinPrimeStructure:
    """Modular and structural details for one twin-prime pair."""

    pair: tuple[int, int]
    center: int
    center_mod6: int
    center_mod30: int
    pair_mod6: tuple[int, int]
    pair_mod30: tuple[int, int]


@dataclass(frozen=True)
class GapAnalysis:
    """Gap metrics between consecutive twin-prime pairs and centers."""

    pair_start_gaps: list[int]
    center_gaps: list[int]
    pair_start_gap_histogram: dict[int, int]
    center_gap_histogram: dict[int, int]


@dataclass(frozen=True)
class FactorizationRecord:
    """Factorization-derived metrics for a single number."""

    number: int
    factorization: dict[int, int]
    divisor_count: int
    largest_prime_factor: int
    is_squarefree: bool
    distinct_prime_factor_count: int


@dataclass(frozen=True)
class FactorizationAggregate:
    """Aggregate factorization statistics for a group of numbers."""

    numbers: list[int]
    average_divisor_count: float
    divisor_count_histogram: dict[int, int]
    distinct_prime_factor_count_histogram: dict[int, int]
    squarefree_count: int
    squarefree_frequency: float
    average_largest_prime_factor: float


@dataclass(frozen=True)
class FactorizationAnalysis:
    """Comparison of factorization properties for centers and non-centers."""

    center_records: list[FactorizationRecord]
    non_center_even_records: list[FactorizationRecord]
    center_aggregate: FactorizationAggregate
    non_center_even_aggregate: FactorizationAggregate


@dataclass(frozen=True)
class DensityWindowRecord:
    """Local density measurements around a twin-prime pair."""

    pair: tuple[int, int]
    center: int
    window_start: int
    window_end: int
    primes_in_window: int
    twin_pairs_in_window: int
    local_prime_density: float
    local_twin_pair_density: float
    global_prime_density: float
    global_twin_pair_density: float
    prime_density_ratio: float


@dataclass(frozen=True)
class DensityAnalysis:
    """Density summaries around all twin-prime pairs in the search range."""

    window_radius: int
    pair_density_stats: list[DensityWindowRecord]
    global_prime_density: float
    global_twin_pair_density: float
    average_local_prime_density: float
    average_local_twin_pair_density: float
    average_prime_density_ratio: float


@dataclass(frozen=True)
class ExpectedTwinCountRecord:
    """Observed vs heuristic twin-prime counts at a checkpoint."""

    limit: int
    actual_count: int
    expected_count: float
    ratio: float | None


@dataclass(frozen=True)
class TwinPrimeAnalysis:
    """Summary of prime and twin-prime structure up to a limit."""

    limit: int
    primes: list[int]
    twin_pairs: list[tuple[int, int]]
    paired_primes: list[int]
    unpaired_primes: list[int]
    pair_centers: list[int]
    number_classifications: list[NumberClassification]
    pair_structures: list[TwinPrimeStructure]
    center_mod6_counts: dict[int, int]
    center_mod30_counts: dict[int, int]
    gap_analysis: GapAnalysis
    factorization_analysis: FactorizationAnalysis
    density_analysis: DensityAnalysis
    expected_vs_observed: list[ExpectedTwinCountRecord]


def primes_up_to(limit: int) -> list[int]:
    """Return all prime numbers less than or equal to ``limit``."""
    if limit < 2:
        return []

    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"

    for candidate in range(2, isqrt(limit) + 1):
        if sieve[candidate]:
            start = candidate * candidate
            step = candidate
            sieve[start : limit + 1 : step] = b"\x00" * (((limit - start) // step) + 1)

    return [number for number in range(2, limit + 1) if sieve[number]]


def twin_primes_up_to(limit: int) -> list[tuple[int, int]]:
    """Return all twin-prime pairs less than or equal to ``limit``."""
    primes = primes_up_to(limit)
    return _twin_pairs_from_primes(primes)


def analyze_primes_up_to(
    limit: int,
    *,
    density_window: int = 50,
    expected_sample_points: list[int] | None = None,
) -> TwinPrimeAnalysis:
    """Return a fuller view of primes and twin-prime structure up to ``limit``."""
    if limit < 1:
        raise ValueError("limit must be at least 1")
    if density_window < 0:
        raise ValueError("density_window must be non-negative")

    primes = primes_up_to(limit)
    twin_pairs = _twin_pairs_from_primes(primes)
    pair_centers = [(left + right) // 2 for left, right in twin_pairs]
    paired_prime_set = {prime for pair in twin_pairs for prime in pair}
    center_map = {center: pair for center, pair in zip(pair_centers, twin_pairs)}
    paired_primes = [prime for prime in primes if prime in paired_prime_set]
    unpaired_primes = [prime for prime in primes if prime not in paired_prime_set]
    prime_set = set(primes)

    number_classifications = _build_number_classifications(
        limit=limit,
        prime_set=prime_set,
        paired_prime_set=paired_prime_set,
        center_map=center_map,
        primes=primes,
    )
    pair_structures = _build_pair_structures(twin_pairs)
    center_mod6_counts = _histogram(structure.center_mod6 for structure in pair_structures)
    center_mod30_counts = _histogram(structure.center_mod30 for structure in pair_structures)
    gap_analysis = _build_gap_analysis(twin_pairs, pair_centers)
    factorization_analysis = _build_factorization_analysis(limit, pair_centers, primes)
    density_analysis = _build_density_analysis(limit, twin_pairs, pair_centers, primes, density_window)
    expected_vs_observed = _build_expected_vs_observed(limit, twin_pairs, expected_sample_points)

    return TwinPrimeAnalysis(
        limit=limit,
        primes=primes,
        twin_pairs=twin_pairs,
        paired_primes=paired_primes,
        unpaired_primes=unpaired_primes,
        pair_centers=pair_centers,
        number_classifications=number_classifications,
        pair_structures=pair_structures,
        center_mod6_counts=center_mod6_counts,
        center_mod30_counts=center_mod30_counts,
        gap_analysis=gap_analysis,
        factorization_analysis=factorization_analysis,
        density_analysis=density_analysis,
        expected_vs_observed=expected_vs_observed,
    )


def _twin_pairs_from_primes(primes: list[int]) -> list[tuple[int, int]]:
    return [
        (left, right)
        for left, right in zip(primes, primes[1:])
        if right - left == 2
    ]


def _classify_number_type(number: int, is_prime: bool) -> str:
    if number == 1:
        return "unit"
    if is_prime:
        return "prime"
    return "composite"


def _classify_prime_role(number: int, is_prime: bool, paired_prime_set: set[int]) -> str:
    if not is_prime:
        return "not_prime"
    if number in paired_prime_set:
        return "prime_in_twin_pair"
    return "prime_not_in_twin_pair"


def _structural_region_for_number(number: int) -> str:
    return "bootstrap" if number <= 5 else "standard"


def _build_number_classifications(
    *,
    limit: int,
    prime_set: set[int],
    paired_prime_set: set[int],
    center_map: dict[int, tuple[int, int]],
    primes: list[int],
) -> list[NumberClassification]:
    number_classifications = []
    for number in range(1, limit + 1):
        is_prime = number in prime_set
        number_type = _classify_number_type(number, is_prime)
        prime_role = _classify_prime_role(number, is_prime, paired_prime_set)
        structural_region = _structural_region_for_number(number)
        is_edge_case = structural_region == "bootstrap"

        adjacent_prime_count = sum(
            neighbor in prime_set for neighbor in (number - 1, number + 1)
        )
        if adjacent_prime_count == 2:
            adjacent_prime_role = "between_two_primes"
        elif adjacent_prime_count == 1:
            adjacent_prime_role = "next_to_one_prime"
        else:
            adjacent_prime_role = "not_next_to_primes"

        prime_divisors: tuple[int, ...] = ()
        all_divisors: tuple[int, ...] = (1,) if number == 1 else ()
        divisor_count: int | None = None
        smallest_prime_factor: int | None = None
        distinct_prime_factor_count: int | None = None
        if number_type == "prime":
            all_divisors = (1, number)
        elif number_type == "composite":
            factorization = _prime_factorization(number, primes)
            prime_divisors = tuple(sorted(factorization))
            all_divisors = _all_divisors_from_factorization(factorization)
            divisor_count = len(all_divisors)
            smallest_prime_factor = min(factorization) if factorization else None
            distinct_prime_factor_count = len(factorization)

        number_classifications.append(
            NumberClassification(
                number=number,
                number_type=number_type,
                is_prime=is_prime,
                prime_role=prime_role,
                is_edge_case=is_edge_case,
                structural_region=structural_region,
                is_pair_center=number in center_map,
                center_of_pair=center_map.get(number),
                adjacent_prime_count=adjacent_prime_count,
                adjacent_prime_role=adjacent_prime_role,
                prime_divisors=prime_divisors,
                all_divisors=all_divisors,
                divisor_count=divisor_count,
                smallest_prime_factor=smallest_prime_factor,
                distinct_prime_factor_count=distinct_prime_factor_count,
            )
        )
    return number_classifications


def _build_pair_structures(twin_pairs: list[tuple[int, int]]) -> list[TwinPrimeStructure]:
    structures = []
    for left, right in twin_pairs:
        center = (left + right) // 2
        structures.append(
            TwinPrimeStructure(
                pair=(left, right),
                center=center,
                center_mod6=center % 6,
                center_mod30=center % 30,
                pair_mod6=(left % 6, right % 6),
                pair_mod30=(left % 30, right % 30),
            )
        )
    return structures


def _build_gap_analysis(
    twin_pairs: list[tuple[int, int]], pair_centers: list[int]
) -> GapAnalysis:
    pair_starts = [left for left, _ in twin_pairs]
    pair_start_gaps = _consecutive_gaps(pair_starts)
    center_gaps = _consecutive_gaps(pair_centers)
    return GapAnalysis(
        pair_start_gaps=pair_start_gaps,
        center_gaps=center_gaps,
        pair_start_gap_histogram=_histogram(pair_start_gaps),
        center_gap_histogram=_histogram(center_gaps),
    )


def _build_factorization_analysis(
    limit: int,
    pair_centers: list[int],
    primes: list[int],
) -> FactorizationAnalysis:
    center_records = [_factorization_record(center, primes) for center in pair_centers]
    center_set = set(pair_centers)
    non_center_even_numbers = [number for number in range(2, limit + 1, 2) if number not in center_set]
    non_center_even_records = [
        _factorization_record(number, primes) for number in non_center_even_numbers
    ]
    return FactorizationAnalysis(
        center_records=center_records,
        non_center_even_records=non_center_even_records,
        center_aggregate=_aggregate_factorization_records(center_records),
        non_center_even_aggregate=_aggregate_factorization_records(non_center_even_records),
    )


def _build_density_analysis(
    limit: int,
    twin_pairs: list[tuple[int, int]],
    pair_centers: list[int],
    primes: list[int],
    density_window: int,
) -> DensityAnalysis:
    global_prime_density = len(primes) / limit if limit else 0.0
    global_twin_pair_density = len(twin_pairs) / limit if limit else 0.0
    pair_density_stats = []

    for pair, center in zip(twin_pairs, pair_centers):
        window_start = max(1, center - density_window)
        window_end = min(limit, center + density_window)
        window_size = window_end - window_start + 1
        primes_in_window = sum(window_start <= prime <= window_end for prime in primes)
        twin_pairs_in_window = sum(
            window_start <= left and right <= window_end for left, right in twin_pairs
        )
        local_prime_density = primes_in_window / window_size if window_size else 0.0
        local_twin_pair_density = twin_pairs_in_window / window_size if window_size else 0.0
        prime_density_ratio = (
            local_prime_density / global_prime_density if global_prime_density else 0.0
        )
        pair_density_stats.append(
            DensityWindowRecord(
                pair=pair,
                center=center,
                window_start=window_start,
                window_end=window_end,
                primes_in_window=primes_in_window,
                twin_pairs_in_window=twin_pairs_in_window,
                local_prime_density=local_prime_density,
                local_twin_pair_density=local_twin_pair_density,
                global_prime_density=global_prime_density,
                global_twin_pair_density=global_twin_pair_density,
                prime_density_ratio=prime_density_ratio,
            )
        )

    average_local_prime_density = _average(
        record.local_prime_density for record in pair_density_stats
    )
    average_local_twin_pair_density = _average(
        record.local_twin_pair_density for record in pair_density_stats
    )
    average_prime_density_ratio = _average(
        record.prime_density_ratio for record in pair_density_stats
    )

    return DensityAnalysis(
        window_radius=density_window,
        pair_density_stats=pair_density_stats,
        global_prime_density=global_prime_density,
        global_twin_pair_density=global_twin_pair_density,
        average_local_prime_density=average_local_prime_density,
        average_local_twin_pair_density=average_local_twin_pair_density,
        average_prime_density_ratio=average_prime_density_ratio,
    )


def _build_expected_vs_observed(
    limit: int,
    twin_pairs: list[tuple[int, int]],
    expected_sample_points: list[int] | None,
) -> list[ExpectedTwinCountRecord]:
    checkpoints = _normalized_sample_points(limit, expected_sample_points)
    pair_maxima = [right for _, right in twin_pairs]
    actual_count = 0
    pair_index = 0
    records = []

    for checkpoint in checkpoints:
        while pair_index < len(pair_maxima) and pair_maxima[pair_index] <= checkpoint:
            actual_count += 1
            pair_index += 1
        expected_count = _expected_twin_count(checkpoint)
        ratio = actual_count / expected_count if expected_count > 0 else None
        records.append(
            ExpectedTwinCountRecord(
                limit=checkpoint,
                actual_count=actual_count,
                expected_count=expected_count,
                ratio=ratio,
            )
        )
    return records


def _factorization_record(number: int, primes: list[int]) -> FactorizationRecord:
    factorization = _prime_factorization(number, primes)
    divisor_count = 1
    for exponent in factorization.values():
        divisor_count *= exponent + 1
    largest_prime_factor = max(factorization) if factorization else 1
    return FactorizationRecord(
        number=number,
        factorization=factorization,
        divisor_count=divisor_count,
        largest_prime_factor=largest_prime_factor,
        is_squarefree=all(exponent == 1 for exponent in factorization.values()),
        distinct_prime_factor_count=len(factorization),
    )


def _aggregate_factorization_records(
    records: list[FactorizationRecord],
) -> FactorizationAggregate:
    return FactorizationAggregate(
        numbers=[record.number for record in records],
        average_divisor_count=_average(record.divisor_count for record in records),
        divisor_count_histogram=_histogram(record.divisor_count for record in records),
        distinct_prime_factor_count_histogram=_histogram(
            record.distinct_prime_factor_count for record in records
        ),
        squarefree_count=sum(record.is_squarefree for record in records),
        squarefree_frequency=(
            sum(record.is_squarefree for record in records) / len(records) if records else 0.0
        ),
        average_largest_prime_factor=_average(
            record.largest_prime_factor for record in records
        ),
    )


def _prime_factorization(number: int, primes: list[int]) -> dict[int, int]:
    remaining = number
    factorization: dict[int, int] = {}
    for prime in primes:
        if prime * prime > remaining:
            break
        while remaining % prime == 0:
            factorization[prime] = factorization.get(prime, 0) + 1
            remaining //= prime
    if remaining > 1:
        factorization[remaining] = factorization.get(remaining, 0) + 1
    return factorization


def _all_divisors_from_factorization(factorization: dict[int, int]) -> tuple[int, ...]:
    divisors = [1]
    for prime, exponent in sorted(factorization.items()):
        next_divisors = []
        prime_powers = [prime ** power for power in range(exponent + 1)]
        for divisor in divisors:
            for prime_power in prime_powers:
                next_divisors.append(divisor * prime_power)
        divisors = next_divisors
    return tuple(sorted(divisors))


def _consecutive_gaps(values: list[int]) -> list[int]:
    return [current - previous for previous, current in zip(values, values[1:])]


def _histogram(values: Iterable[int]) -> dict[int, int]:
    histogram: dict[int, int] = {}
    for value in values:
        histogram[value] = histogram.get(value, 0) + 1
    return dict(sorted(histogram.items()))


def _average(values: Iterable[float | int]) -> float:
    items = list(values)
    return sum(items) / len(items) if items else 0.0


def _normalized_sample_points(
    limit: int, expected_sample_points: list[int] | None
) -> list[int]:
    if expected_sample_points is not None:
        return sorted({point for point in expected_sample_points if 2 <= point <= limit}) or [limit]
    if limit <= 10:
        return list(range(2, limit + 1))

    step = max(10, limit // 10)
    checkpoints = list(range(step, limit + 1, step))
    if checkpoints[-1] != limit:
        checkpoints.append(limit)
    return checkpoints


def _expected_twin_count(limit: int) -> float:
    if limit < 3:
        return 0.0
    return limit / (log(limit) ** 2)
