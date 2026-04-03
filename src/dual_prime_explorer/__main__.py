"""Command-line entry point for twin-prime exploration."""

from __future__ import annotations

import argparse
from dataclasses import asdict
from pprint import pformat

from .core import NumberClassification, analyze_primes_up_to
from .web import run_server


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore twin-prime structure up to a chosen limit."
    )
    parser.add_argument(
        "limit",
        nargs="?",
        type=int,
        help="Upper bound for the search.",
    )
    parser.add_argument(
        "--window",
        type=int,
        default=50,
        help="Half-width of the local density window used by --density.",
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Launch the local web app instead of printing CLI output.",
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="When used with --serve, reload web UI modules on each request for local development.",
    )
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host interface for --serve.",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for --serve.",
    )

    output_group = parser.add_mutually_exclusive_group()
    output_group.add_argument(
        "--count-only",
        action="store_true",
        help="Print only the number of twin-prime pairs found.",
    )
    output_group.add_argument(
        "--table",
        action="store_true",
        help="Print a row-by-row table for every number up to the limit.",
    )
    output_group.add_argument(
        "--csv",
        action="store_true",
        help="Print CSV output for every number up to the limit.",
    )
    output_group.add_argument(
        "--gaps",
        action="store_true",
        help="Print gap analysis for consecutive twin-prime pairs and centers.",
    )
    output_group.add_argument(
        "--modular",
        action="store_true",
        help="Print modular and structural analysis for twin-prime pairs.",
    )
    output_group.add_argument(
        "--factors",
        action="store_true",
        help="Print factorization metrics for centers and non-center even numbers.",
    )
    output_group.add_argument(
        "--density",
        action="store_true",
        help="Print local density measurements around each twin-prime pair.",
    )
    output_group.add_argument(
        "--expected",
        action="store_true",
        help="Print observed vs heuristic twin-prime counts up to the limit.",
    )
    return parser


def _format_center(pair: tuple[int, int] | None) -> str:
    if pair is None:
        return ""
    return f"{pair[0]}-{pair[1]}"


def _render_table(rows: list[NumberClassification]) -> str:
    headers = [
        "number",
        "number_type",
        "is_prime",
        "prime_role",
        "is_edge_case",
        "structural_region",
        "is_pair_center",
    ]
    table_rows = [
        [
            str(row.number),
            row.number_type,
            str(row.is_prime),
            row.prime_role,
            str(row.is_edge_case),
            row.structural_region,
            str(row.is_pair_center),
        ]
        for row in rows
    ]
    widths = [len(header) for header in headers]
    for table_row in table_rows:
        for index, value in enumerate(table_row):
            widths[index] = max(widths[index], len(value))

    lines = []
    lines.append(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    lines.append("-+-".join("-" * width for width in widths))
    for table_row in table_rows:
        lines.append(" | ".join(value.ljust(widths[index]) for index, value in enumerate(table_row)))
    return "\n".join(lines)


def _render_csv(rows: list[NumberClassification]) -> str:
    lines = ["number,is_prime,prime_role,is_pair_center,center_of_pair"]
    for row in rows:
        lines.append(
            ",".join(
                [
                    str(row.number),
                    str(row.is_prime),
                    row.prime_role,
                    str(row.is_pair_center),
                    _format_center(row.center_of_pair),
                ]
            )
        )
    return "\n".join(lines)


def _render_expected(records: list[dict[str, object]]) -> str:
    headers = ["limit", "actual_count", "expected_count", "ratio"]
    rows = []
    for record in records:
        ratio = "" if record["ratio"] is None else f"{record['ratio']:.6f}"
        rows.append(
            [
                str(record["limit"]),
                str(record["actual_count"]),
                f"{record['expected_count']:.6f}",
                ratio,
            ]
        )
    widths = [len(header) for header in headers]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    lines = []
    lines.append(" | ".join(header.ljust(widths[index]) for index, header in enumerate(headers)))
    lines.append("-+-".join("-" * width for width in widths))
    for row in rows:
        lines.append(" | ".join(value.ljust(widths[index]) for index, value in enumerate(row)))
    return "\n".join(lines)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.dev and not args.serve:
        parser.error("--dev can only be used together with --serve")

    if args.serve:
        if args.window < 0:
            parser.error("window must be non-negative")
        run_server(host=args.host, port=args.port, dev_mode=args.dev)
        return 0

    if args.limit is None:
        parser.error("limit is required unless --serve is used")
    if args.limit < 2:
        parser.error("limit must be at least 2")
    if args.window < 0:
        parser.error("window must be non-negative")

    analysis = analyze_primes_up_to(args.limit, density_window=args.window)

    if args.count_only:
        print(len(analysis.twin_pairs))
        return 0

    if args.table:
        print(_render_table(analysis.number_classifications))
        return 0

    if args.csv:
        print(_render_csv(analysis.number_classifications))
        return 0

    if args.gaps:
        print(pformat(asdict(analysis.gap_analysis), sort_dicts=False))
        return 0

    if args.modular:
        modular_view = {
            "pair_structures": [asdict(structure) for structure in analysis.pair_structures],
            "center_mod6_counts": analysis.center_mod6_counts,
            "center_mod30_counts": analysis.center_mod30_counts,
        }
        print(pformat(modular_view, sort_dicts=False))
        return 0

    if args.factors:
        print(pformat(asdict(analysis.factorization_analysis), sort_dicts=False))
        return 0

    if args.density:
        print(pformat(asdict(analysis.density_analysis), sort_dicts=False))
        return 0

    if args.expected:
        print(_render_expected([asdict(record) for record in analysis.expected_vs_observed]))
        return 0

    print(f"Prime analysis up to {args.limit}")
    print(f"All primes: {analysis.primes}")
    print(f"Twin-prime pairs ({len(analysis.twin_pairs)}): {analysis.twin_pairs}")
    print(f"Primes in at least one pair: {analysis.paired_primes}")
    print(f"Primes not in any pair: {analysis.unpaired_primes}")
    print(f"Centers between twin primes: {analysis.pair_centers}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
