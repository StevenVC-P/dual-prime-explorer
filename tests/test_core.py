from math import isclose, log

from dual_prime_explorer import web
from dual_prime_explorer.__main__ import build_parser
from dual_prime_explorer.core import analyze_primes_up_to, primes_up_to, twin_primes_up_to
from dual_prime_explorer.web import build_analysis_payload, load_web_runtime
from dual_prime_explorer.web_assets import build_page_registry
from dual_prime_explorer.web_content import THEORY_TABS
from dual_prime_explorer.web_pages import PAGE_BY_ROUTE


def test_primes_up_to_30() -> None:
    assert primes_up_to(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_twin_primes_up_to_100() -> None:
    assert twin_primes_up_to(100) == [
        (3, 5),
        (5, 7),
        (11, 13),
        (17, 19),
        (29, 31),
        (41, 43),
        (59, 61),
        (71, 73),
    ]


def test_prime_analysis_up_to_100() -> None:
    analysis = analyze_primes_up_to(100)
    assert analysis.primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert analysis.paired_primes == [3, 5, 7, 11, 13, 17, 19, 29, 31, 41, 43, 59, 61, 71, 73]
    assert analysis.unpaired_primes == [2, 23, 37, 47, 53, 67, 79, 83, 89, 97]
    assert analysis.pair_centers == [4, 6, 12, 18, 30, 42, 60, 72]


def test_number_classifications_capture_edge_cases_and_centers() -> None:
    analysis = analyze_primes_up_to(12)
    by_number = {row.number: row for row in analysis.number_classifications}

    assert by_number[1].number_type == "unit"
    assert by_number[1].is_prime is False
    assert by_number[1].prime_role == "not_prime"
    assert by_number[1].is_edge_case is True
    assert by_number[1].structural_region == "bootstrap"
    assert by_number[1].is_pair_center is False
    assert by_number[1].prime_divisors == ()
    assert by_number[1].all_divisors == (1,)

    assert by_number[2].number_type == "prime"
    assert by_number[2].is_prime is True
    assert by_number[2].prime_role == "prime_not_in_twin_pair"
    assert by_number[2].is_edge_case is True
    assert by_number[2].structural_region == "bootstrap"
    assert by_number[2].is_pair_center is False

    assert by_number[3].number_type == "prime"
    assert by_number[3].is_prime is True
    assert by_number[3].prime_role == "prime_in_twin_pair"
    assert by_number[3].is_edge_case is True
    assert by_number[3].structural_region == "bootstrap"
    assert by_number[3].is_pair_center is False

    assert by_number[4].number_type == "composite"
    assert by_number[4].prime_role == "not_prime"
    assert by_number[4].is_edge_case is True
    assert by_number[4].structural_region == "bootstrap"
    assert by_number[4].is_pair_center is True
    assert by_number[4].center_of_pair == (3, 5)
    assert by_number[4].adjacent_prime_role == "between_two_primes"
    assert by_number[4].prime_divisors == (2,)
    assert by_number[4].all_divisors == (1, 2, 4)

    assert by_number[5].structural_region == "bootstrap"
    assert by_number[6].structural_region == "standard"
    assert by_number[6].is_pair_center is True
    assert by_number[6].center_of_pair == (5, 7)
    assert by_number[8].adjacent_prime_role == "next_to_one_prime"
    assert by_number[8].prime_divisors == (2,)
    assert by_number[10].number_type == "composite"
    assert by_number[10].prime_role == "not_prime"
    assert by_number[10].structural_region == "standard"
    assert by_number[11].prime_role == "prime_not_in_twin_pair"
    assert by_number[12].is_pair_center is False
    assert by_number[12].center_of_pair is None
    assert by_number[12].adjacent_prime_role == "next_to_one_prime"
    assert by_number[12].prime_divisors == (2, 3)
    assert by_number[12].all_divisors == (1, 2, 3, 4, 6, 12)


def test_modular_structure_matches_twin_prime_pattern() -> None:
    analysis = analyze_primes_up_to(100)

    assert analysis.center_mod6_counts == {0: 7, 4: 1}
    assert analysis.center_mod30_counts == {0: 2, 4: 1, 6: 1, 12: 3, 18: 1}

    structures_after_first = analysis.pair_structures[1:]
    assert all(structure.center_mod6 == 0 for structure in structures_after_first)
    assert all(structure.pair_mod6 == (5, 1) for structure in structures_after_first)


def test_gap_analysis_for_first_100_numbers() -> None:
    analysis = analyze_primes_up_to(100)

    assert analysis.gap_analysis.pair_start_gaps == [2, 6, 6, 12, 12, 18, 12]
    assert analysis.gap_analysis.center_gaps == [2, 6, 6, 12, 12, 18, 12]
    assert analysis.gap_analysis.pair_start_gap_histogram == {2: 1, 6: 2, 12: 3, 18: 1}
    assert analysis.gap_analysis.center_gap_histogram == {2: 1, 6: 2, 12: 3, 18: 1}


def test_factorization_metrics_include_centers_and_non_center_evens() -> None:
    analysis = analyze_primes_up_to(100)
    center_records = {
        record.number: record for record in analysis.factorization_analysis.center_records
    }

    assert center_records[12].factorization == {2: 2, 3: 1}
    assert center_records[12].divisor_count == 6
    assert center_records[12].largest_prime_factor == 3
    assert center_records[12].is_squarefree is False

    assert center_records[30].factorization == {2: 1, 3: 1, 5: 1}
    assert center_records[30].divisor_count == 8
    assert center_records[30].largest_prime_factor == 5
    assert center_records[30].is_squarefree is True

    center_aggregate = analysis.factorization_analysis.center_aggregate
    assert center_aggregate.squarefree_count == 3
    assert isclose(center_aggregate.squarefree_frequency, 3 / 8)
    assert 8 in center_aggregate.divisor_count_histogram

    non_center_aggregate = analysis.factorization_analysis.non_center_even_aggregate
    assert 2 in non_center_aggregate.numbers
    assert 4 not in non_center_aggregate.numbers


def test_density_window_stats_are_computed_locally() -> None:
    analysis = analyze_primes_up_to(100, density_window=10)
    record = next(
        item for item in analysis.density_analysis.pair_density_stats if item.pair == (11, 13)
    )

    assert record.window_start == 2
    assert record.window_end == 22
    assert record.primes_in_window == 8
    assert record.twin_pairs_in_window == 4
    assert isclose(record.local_prime_density, 8 / 21)
    assert isclose(record.global_prime_density, 25 / 100)
    assert isclose(record.prime_density_ratio, (8 / 21) / (25 / 100))


def test_expected_vs_observed_uses_requested_checkpoints() -> None:
    analysis = analyze_primes_up_to(100, expected_sample_points=[10, 50, 100])
    records = {record.limit: record for record in analysis.expected_vs_observed}

    assert records[10].actual_count == 2
    assert records[50].actual_count == 6
    assert records[100].actual_count == 8
    assert isclose(records[10].expected_count, 10 / (log(10) ** 2))
    assert isclose(records[100].ratio, 8 / (100 / (log(100) ** 2)))


def test_web_payload_matches_analysis_shape() -> None:
    payload = build_analysis_payload(30, density_window=10, start=1)

    assert payload["start"] == 1
    assert payload["limit"] == 30
    assert payload["twin_pairs"] == [[3, 5], [5, 7], [11, 13], [17, 19]]
    assert payload["density_analysis"]["window_radius"] == 10
    assert payload["center_mod6_counts"] == {"4": 1, "0": 3}
    assert payload["number_classifications"][0]["number_type"] == "unit"
    assert payload["number_classifications"][0]["prime_role"] == "not_prime"
    assert payload["number_classifications"][1]["number_type"] == "prime"
    assert payload["number_classifications"][1]["is_edge_case"] is True
    assert payload["number_classifications"][2]["prime_role"] == "prime_in_twin_pair"
    assert payload["number_classifications"][3]["is_pair_center"] is True
    assert payload["number_classifications"][3]["structural_region"] == "bootstrap"
    assert payload["number_classifications"][3]["adjacent_prime_role"] == "between_two_primes"
    assert payload["number_classifications"][3]["prime_divisors"] == [2]
    assert payload["number_classifications"][3]["all_divisors"] == [1, 2, 4]
    assert payload["number_classifications"][3]["divisor_count"] == 3

def test_web_payload_supports_selected_ranges() -> None:
    payload = build_analysis_payload(30, start=10)

    assert payload["start"] == 10
    assert payload["limit"] == 30
    assert payload["primes"] == [11, 13, 17, 19, 23, 29]
    assert payload["twin_pairs"] == [[11, 13], [17, 19]]
    assert payload["pair_centers"] == [12, 18]
    assert payload["number_classifications"][0]["number"] == 10
    assert payload["number_classifications"][-1]["number"] == 30
    assert payload["density_analysis"]["pair_density_stats"][0]["window_start"] == 10
    assert payload["density_analysis"]["pair_density_stats"][-1]["window_end"] == 30


def test_route_registry_is_ready_for_more_pages() -> None:
    assert set(PAGE_BY_ROUTE) == {"/lab", "/explorer", "/analysis", "/analysis-guide", "/glossary", "/theory", "/experiments"}
    rendered_pages = build_page_registry()
    assert "/analysis" in rendered_pages
    assert "href=\"/analysis\"" in rendered_pages["/explorer"]
    assert "Analysis Views" in rendered_pages["/analysis"]


def test_theory_tab_configuration_is_present() -> None:
    tab_ids = [tab["id"] for tab in THEORY_TABS]
    assert tab_ids == ["history", "approaches", "progress", "why-its-hard"]
    history_tab = THEORY_TABS[0]
    assert history_tab["updated"] == "Last reviewed: April 2026"
    assert any("twin prime conjecture" in section["body"].lower() for section in history_tab["sections"])
    assert any("Hardy-Littlewood" in section["title"] or "Hardy-Littlewood" in section["body"] for section in history_tab["sections"])
    assert any("twin prime constant" in section["body"].lower() for section in history_tab["sections"])
    assert any(item["title"] == "Yitang Zhang proves bounded gaps between primes" for item in history_tab["timeline"])
    assert any(item["question"] == "What did Yitang Zhang prove?" for item in history_tab["faq"])
    assert any("Hardy & Littlewood" in item["title"] for item in history_tab["references"])
    assert any(card["title"] == "Sieve Methods" for card in THEORY_TABS[1]["cards"])
    assert THEORY_TABS[1]["intro"].startswith("Mathematicians study the twin prime conjecture")
    assert any("bounded gaps between primes" in card["helps"].lower() for card in THEORY_TABS[1]["cards"])
    assert any("parity problem" in card["falls_short"].lower() for card in THEORY_TABS[1]["cards"])
    assert any(section["title"] == "Synthesis: Why the Twin Prime Problem Persists" for section in THEORY_TABS[1]["sections"])
    assert THEORY_TABS[2]["intro"].startswith("Modern progress on the twin prime conjecture")
    assert any(section["title"] == "Bounded Gaps Breakthrough" for section in THEORY_TABS[2]["sections"])
    assert any("Yitang Zhang" in section["body"] for section in THEORY_TABS[2]["sections"])
    assert any(section["title"] == "Synthesis: Where We Stand" for section in THEORY_TABS[2]["sections"])
    assert THEORY_TABS[3]["intro"].startswith("The twin prime conjecture is difficult because it lies at the intersection")
    assert any(section["title"] == "Global vs Local Tension" for section in THEORY_TABS[3]["sections"])
    assert any("gap 2" in section["body"].lower() for section in THEORY_TABS[3]["sections"])
    assert any(section["title"] == "Synthesis: The Core Difficulty" for section in THEORY_TABS[3]["sections"])
    assert "DualPrimeRequestHandler" in dir(web)


def test_load_web_runtime_supports_dev_mode() -> None:
    runtime = load_web_runtime(dev_mode=True)

    assert set(runtime["page_by_route"]) == {"/lab", "/explorer", "/analysis", "/analysis-guide", "/glossary", "/theory", "/experiments"}
    assert "Visualization Lab" in runtime["page_registry"]["/lab"]
    assert "visualization-stage" in runtime["page_registry"]["/lab"]
    assert "Range Snapshot" in runtime["page_registry"]["/lab"]
    assert "Visualization mode" in runtime["page_registry"]["/lab"]
    assert ">Mod 6<" in runtime["page_registry"]["/lab"]
    assert "/glossary#glossary-term-mod-6" in runtime["page_registry"]["/lab"]
    assert "/glossary#glossary-term-twin-center" in runtime["page_registry"]["/lab"]
    assert "Twin center" in runtime["page_registry"]["/lab"]
    assert "This panel is ready for future theory and analysis callouts tied to the active view." not in runtime["page_registry"]["/lab"]
    assert "Filters" in runtime["page_registry"]["/explorer"]
    assert "/glossary#glossary-term-prime-neighborhood" in runtime["page_registry"]["/explorer"]
    assert "/glossary#glossary-term-divisor" in runtime["page_registry"]["/explorer"]
    assert "Range Start" in runtime["page_registry"]["/explorer"]
    assert "Range End" in runtime["page_registry"]["/explorer"]
    assert "Number Table" in runtime["page_registry"]["/explorer"]
    assert "filter-columns" in runtime["page_registry"]["/explorer"]
    assert "filter-divisors" in runtime["page_registry"]["/explorer"]
    assert "filter-divisor-logic" in runtime["page_registry"]["/explorer"]
    assert "Not Prime" in runtime["page_registry"]["/explorer"]
    assert "Single Prime" in runtime["page_registry"]["/explorer"]
    assert "Number type" in runtime["explorer_js"]
    assert "filter-neighborhood" in runtime["page_registry"]["/explorer"]
    assert "Twin Center" in runtime["explorer_js"]
    assert "Prime neighborhood" in runtime["explorer_js"]
    assert "getVisibleNumberTableColumns" in runtime["explorer_js"]
    assert "Analyzed range:" in runtime["explorer_js"]
    assert "before table filters." in runtime["explorer_js"]
    assert "parseDivisorFilterValues" in runtime["explorer_js"]
    assert "filter-divisor-logic" in runtime["page_registry"]["/explorer"]
    assert "row.all_divisors" in runtime["explorer_js"]
    assert "prime_divisors" in runtime["explorer_js"]
    assert "All divisors" in runtime["explorer_js"]
    assert "filterColumnOptions" in runtime["explorer_js"]
    assert "renderExplorerVisualization" in runtime["explorer_js"]
    assert "buildVisualizationModel" in runtime["explorer_js"]
    assert "state.visualMode" in runtime["explorer_js"]
    assert "mode-mod6" in runtime["explorer_js"]
    assert "Primes greater than 3 land in the 1 and 5 columns" in runtime["explorer_js"]
    assert "Standard is the fastest way to scan the field." in runtime["explorer_js"]
    assert "Why this matters" in runtime["explorer_js"]
    assert "Mod 6 makes the residue pattern visible." in runtime["explorer_js"]
    assert "syncVisualizationSelectionStyles" in runtime["explorer_js"]
    assert "clear-visual-selection" in runtime["explorer_js"]
    assert "Pinned selection" in runtime["explorer_js"]
    assert "analysisCache" in runtime["explorer_js"]
    assert "tryFetchExplorerRange();" in runtime["explorer_js"]
    assert "Composite" in runtime["explorer_js"]
    assert "How To Read The Analysis Page" in runtime["page_registry"]["/analysis"]
    assert "Glossary links" in runtime["page_registry"]["/analysis"]
    assert "Open glossary entry: Prime Gap" in runtime["page_registry"]["/analysis"]
    assert "/glossary#glossary-term-prime-gap" in runtime["page_registry"]["/analysis"]
    assert "/glossary#glossary-term-bounded-gaps-between-primes" in runtime["page_registry"]["/analysis"]
    assert "Start with Gaps for spacing" in runtime["page_registry"]["/analysis"]
    assert "Open the full analysis guide in a new tab" in runtime["page_registry"]["/analysis"]
    assert "data-analysis-target" in runtime["analysis_js"]
    assert "tabShortcutButtons" in runtime["analysis_js"]
    assert "getAnalysisTabExplanation" in runtime["analysis_js"]
    assert "Start here for structural patterns." in runtime["analysis_js"]
    assert "Glossary" in runtime["page_registry"]["/glossary"]
    assert "id=\"glossary-term-mod-6\"" in runtime["page_registry"]["/glossary"]
    assert "Twin Center" in runtime["page_registry"]["/glossary"]
    assert "Hardy-Littlewood Conjecture" in runtime["page_registry"]["/glossary"]
    assert "Analysis Guide" in runtime["page_registry"]["/analysis-guide"]
    assert "Which tab should you open first?" in runtime["page_registry"]["/analysis-guide"]
    assert "Recommended reading order" in runtime["page_registry"]["/analysis-guide"]
    assert "Modular view" in runtime["page_registry"]["/analysis-guide"]
    assert "theoryTabs" in runtime["theory_js"]
    assert "Twin Prime History Timeline" in runtime["theory_js"]
    assert "Last reviewed: April 2026" in runtime["page_registry"]["/theory"]
    assert "Glossary links" in runtime["page_registry"]["/theory"]
    assert "These pills open glossary entries for the theory concepts below." in runtime["page_registry"]["/theory"]
    assert "Open glossary entry: Hardy-Littlewood Conjecture" in runtime["page_registry"]["/theory"]
    assert "What did Yitang Zhang prove?" in runtime["page_registry"]["/theory"]
    assert "Hardy-Littlewood prime pair conjecture" in runtime["page_registry"]["/theory"] or "Hardy-Littlewood" in runtime["page_registry"]["/theory"]
    assert "/glossary#glossary-term-bounded-gaps-between-primes" in runtime["page_registry"]["/theory"]
    assert "glossarySearch" in runtime["theory_js"]
    assert "applyGlossaryFilter" in runtime["theory_js"]


def test_parser_supports_dev_flag() -> None:
    parser = build_parser()
    args = parser.parse_args(["--serve", "--dev"])

    assert args.serve is True
    assert args.dev is True


def test_web_runtime_module_matches_web_exports() -> None:
    from dual_prime_explorer import web_runtime

    payload = web.build_analysis_payload(30, start=10, dev_mode=True)
    direct_payload = web_runtime.build_analysis_payload(30, start=10, dev_mode=True)

    assert payload == direct_payload
    assert payload["start"] == 10
    assert payload["number_classifications"][0]["number"] == 10


def test_small_limits() -> None:
    assert primes_up_to(1) == []
    assert twin_primes_up_to(3) == []
    analysis = analyze_primes_up_to(3)
    assert analysis.primes == [2, 3]
    assert analysis.twin_pairs == []
    assert analysis.paired_primes == []
    assert analysis.unpaired_primes == [2, 3]
    assert analysis.pair_centers == []
    assert [row.number for row in analysis.number_classifications] == [1, 2, 3]
    assert analysis.gap_analysis.pair_start_gaps == []
    assert analysis.factorization_analysis.center_records == []

