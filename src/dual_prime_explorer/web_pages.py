"""HTML page definitions for the web UI."""

from __future__ import annotations

from dataclasses import dataclass
import html

from .web_content import EXPLANATORY_PAGES
from .web_limits import MAX_WEB_END, MAX_WEB_RANGE_SIZE


@dataclass(frozen=True)
class PageDefinition:
    route: str
    title: str
    nav_label: str
    active_route: str
    hero_html: str
    main_html: str
    script_name: str
    meta_description: str | None = None
    include_in_nav: bool = True


def _render_explanatory_links(items: list[dict[str, str]]) -> str:
    return "".join(
        """<article class="metric-box theory-path-card">
      <h3>{title}</h3>
      <p>{body}</p>
      <p><a class="inline-link" href="{href}">{label}</a></p>
    </article>""".format(
            title=html.escape(item["title"]),
            body=html.escape(item["body"]),
            href=html.escape(item["href"], quote=True),
            label=html.escape(item["label"]),
        )
        for item in items
    )


def _build_explanatory_page(content: dict[str, object]) -> PageDefinition:
    sections = "".join(
        """<article class="theory-section">
      <h3>{title}</h3>
      <p>{body}</p>
    </article>""".format(
            title=html.escape(section["title"]),
            body=html.escape(section["body"]),
        )
        for section in content["sections"]
    )
    related_links = _render_explanatory_links(content["related_links"])
    hero_html = """<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">{eyebrow}</p>
    <h1>{hero_title}</h1>
    <p class="hero-text">{hero_text}</p>
  </div>
</section>""".format(
        eyebrow=html.escape(content["eyebrow"]),
        hero_title=html.escape(content["hero_title"]),
        hero_text=html.escape(content["hero_text"]),
    )
    main_html = """<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>{intro_title}</h2>
      <p>{intro_text}</p>
    </div>
  </div>
  <div class="section-stack">
    {sections}
  </div>
</section>

<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Where to go next</h2>
      <p>Use these links to keep reading or jump back into the live number views.</p>
    </div>
  </div>
  <div class="metric-grid theory-path-grid">
    {related_links}
  </div>
</section>""".format(
        intro_title=html.escape(content["intro_title"]),
        intro_text=html.escape(content["intro_text"]),
        sections=sections,
        related_links=related_links,
    )
    return PageDefinition(
        route=content["route"],
        title=content["title"],
        nav_label=content["nav_label"],
        active_route="theory",
        hero_html=hero_html,
        main_html=main_html,
        script_name="theory.js",
        meta_description=content["meta_description"],
        include_in_nav=False,
    )


LAB_PAGE = PageDefinition(
    route="/lab",
    title="Twin Prime Exploration Lab | Lab",
    nav_label="Lab",
    active_route="lab",
    meta_description="Explore primes, twin primes, and twin centers in a live visual field with lightweight range controls and connected analysis links.",
    hero_html="""<section class="hero-block">
  <div class="hero-copy">
    <p class="eyebrow">Lab</p>
    <h1>See twin-prime structure as a visual field.</h1>
    <p class="hero-text">Adjust the range, watch primes and <a class="inline-link" href="/glossary#glossary-term-twin-center">twin centers</a> light up, and move into exact inspection, deeper analysis, or theory context when you want more structure.</p>
  </div>
</section>""",
    main_html="""<section class="panel explorer-lab-panel">
  <div class="panel-heading">
    <div>
      <h2>Visualization Lab</h2>
      <p>Explore primes, twin primes, and <a class="inline-link" href="/glossary#glossary-term-twin-center">twin centers</a> as a single visual pattern field.</p>
    </div>
    <p id="visualization-range-label">Loading range...</p>
  </div>
  <div class="lab-layout">
    <form id="analysis-form" class="control-panel explorer-lab-controls">
      <div class="lab-card-copy">
        <h3>Range Controls</h3>
        <p>Pick a span of integers and the lab updates in place.</p>
      </div>
      <label>
        <span>Range Start</span>
        <input id="start-input" name="start" type="number" min="1" max="200000" value="1" required>
      </label>
      <label>
        <span>Range End</span>
        <input id="end-input" name="end" type="number" min="2" max="200000" value="500" required>
      </label>
      <button type="submit">Refresh Range</button>
      <fieldset class="lab-experiment-panel">
        <legend>Mod Filter</legend>
        <label>
          <span>Modulus</span>
          <input id="mod-base-input" type="number" min="2" max="60" placeholder="6">
        </label>
        <p class="section-copy">Choose a modulus from 2 to 60, then select one or more residues. The modulus sets the remainder system; the field only changes after you choose residues. If you want the shortest plain-language explanation, read <a class="inline-link" href="/why-mod-6-shows-up-so-often">Why Mod 6 Shows Up So Often</a>.</p>
        <div>
          <span class="filter-label">Residues</span>
          <div id="mod-residue-options" class="mod-residue-options"></div>
        </div>
        <div id="mod-filter-summary" class="lab-experiment-summary">No mod filter active.</div>
        <button id="clear-mod-filter" class="lab-inline-button" type="button">Clear Mod Filter</button>
        <p class="section-copy">Use this as a lightweight residue filter. If terms like modulus or residue class feel unfamiliar, use the <a class="inline-link" href="/glossary#glossary-term-residue-class">Glossary</a> instead of learning them here.</p>
      </fieldset>
      <p class="section-copy">Updates live while you adjust the range. Web ranges are capped at 20,000 numbers and an end value of 200,000 to keep the app responsive.</p>
      <p class="section-copy"><a class="inline-link" href="/explorer">Open the detailed Explorer page</a></p>
    </form>
    <section class="lab-visualization-card" aria-labelledby="visualization-title">
      <div class="lab-card-header">
        <div>
          <h3 id="visualization-title">Prime Field</h3>
          <p class="section-copy"><a class="inline-link" href="/glossary#glossary-term-twin-center">Twin centers</a> mark where twin primes occur. Read <a class="inline-link" href="/why-twin-centers-matter">Why Twin Centers Matter</a> for the short explanation.</p>
        </div>
      </div>
      <div class="lab-visual-tools">
        <div class="lab-view-switch" role="group" aria-label="Visualization mode">
          <button type="button" class="lab-view-button active" data-visual-mode="standard" aria-pressed="true">Standard</button>
          <button type="button" class="lab-view-button" data-visual-mode="mod6" aria-pressed="false">Mod 6</button>
          <button type="button" class="lab-view-button" data-visual-mode="factors" aria-pressed="false">Factors</button>
          <button type="button" class="lab-view-button" data-visual-mode="centers" aria-pressed="false">Twin Centers</button>
        </div>
        <p class="section-copy">Glossary: <a class="inline-link" href="/glossary#glossary-term-mod-6">Mod 6</a>, <a class="inline-link" href="/glossary#glossary-term-divisor">Divisor</a>, <a class="inline-link" href="/glossary#glossary-term-twin-center">Twin Center</a>.</p>
        <p id="visualization-mode-note" class="lab-mode-note">Standard view keeps the field compact so prime, twin-prime, and twin-center clusters are easy to scan.</p>
        <div id="visualization-pagination" class="lab-pagination" aria-label="Visualization pages"></div>
      </div>
      <div id="visualization-stage" class="visualization-stage"></div>
      <div class="lab-visual-summary" aria-labelledby="lab-visual-summary-title">
        <h4 id="lab-visual-summary-title">Range Snapshot</h4>
        <div id="explorer-visual-summary"></div>
      </div>
    </section>
    <aside class="lab-context-card" aria-labelledby="context-title">
      <div class="lab-card-header">
        <div>
          <h3 id="context-title">Context</h3>
          <p class="section-copy">Hover any number to inspect its role in the range.</p>
        </div>
      </div>
      <div id="visualization-hover" class="lab-hover-card"></div>
      <div class="lab-legend">
        <div class="lab-legend-item"><span class="lab-swatch composite"></span><span>Composite / neutral</span></div>
        <div class="lab-legend-item"><span class="lab-swatch prime"></span><span>Prime</span></div>
        <div class="lab-legend-item"><span class="lab-swatch twin-prime"></span><span>Twin prime</span></div>
        <div class="lab-legend-item"><span class="lab-swatch twin-center"></span><span>Twin center</span></div>
      </div>
    </aside>
  </div>
</section>

<section class="panel">
  <div class="panel-heading">
    <div>
      <h2>What To Do Next</h2>
      <p>Move from seeing the pattern to inspecting or interpreting it.</p>
    </div>
    </div>
  </div>
  <div class="metric-grid">
    <article class="metric-box">
      <h3>Need exact numbers?</h3>
      <p>Use Explorer for row-by-row inspection, divisibility filters, and number-level detail.</p>
      <p><a class="inline-link" href="/explorer">Open Explorer</a></p>
    </article>
    <article class="metric-box">
      <h3>Need structured interpretation?</h3>
      <p>Use Analysis for modular patterns, gaps, factor signals, density, and rough benchmarks.</p>
      <p><a class="inline-link" href="/analysis">Open Analysis</a></p>
    </article>
  </div>
</section>""",
    script_name="explorer.js",
)

EXPLORER_PAGE = PageDefinition(
    route="/explorer",
    title="Twin Prime Exploration Lab | Explorer",
    nav_label="Explorer",
    active_route="explorer",
    meta_description="Inspect primes, twin-prime structure, divisors, and prime neighborhoods one number at a time across a selected range.",
    hero_html="""<section class="hero-block hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">Explorer</p>
    <h1>Inspect the range one number at a time.</h1>
    <p class="hero-text">Exact rows, <a class="inline-link" href="/glossary#glossary-term-divisor">divisor</a> filters, and number-level classifications that complement the visualization-first Lab.</p>
  </div>
  <form id="analysis-form" class="control-panel">
    <label>
      <span>Range Start</span>
      <input id="start-input" name="start" type="number" min="1" max="200000" value="1" required>
    </label>
    <label>
      <span>Range End</span>
      <input id="end-input" name="end" type="number" min="2" max="200000" value="100" required>
    </label>
    <button type="submit">Analyze Range</button>
    <p class="section-copy">Web ranges are capped at 20,000 numbers and an end value of 200,000 to keep the app responsive.</p>
    <p class="section-copy"><a class="inline-link" href="/lab">Open the Visualization Lab</a></p>
  </form>
</section>""",
    main_html="""<section class="panel summary-panel">
  <div class="panel-heading">
    <div>
      <h2>Summary</h2>
      <p>Core counts and quick signals from the current range.</p>
    </div>
    <p id="status-text">Ready to analyze.</p>
  </div>
  <div id="summary-cards" class="summary-cards"></div>
</section>

<section class="panel table-panel">
  <div class="panel-heading">
    <div>
      <h2 id="number-table-title">Number Table</h2>
      <p>Prime membership, <a class="inline-link" href="/glossary#glossary-term-prime-neighborhood">prime neighborhood</a> structure, and <a class="inline-link" href="/glossary#glossary-term-divisor">divisibility</a> for each number.</p>
    </div>
    <p id="table-filter-status">Showing all rows.</p>
  </div>
  <section class="filter-panel" aria-labelledby="filter-panel-title">
    <div class="filter-panel-header">
      <div>
        <h3 id="filter-panel-title">Filters</h3>
        <p>Refine the number table by <a class="inline-link" href="/glossary#glossary-term-single-prime">prime role</a>, <a class="inline-link" href="/glossary#glossary-term-prime-neighborhood">neighborhood</a>, <a class="inline-link" href="/glossary#glossary-term-divisor">divisors</a>, or numeric range.</p>
      </div>
      <button id="filter-reset" class="filter-reset-button" type="button">Reset Filters</button>
    </div>
    <form id="table-filter-form" class="filter-layout">
      <div class="filter-column">
        <fieldset class="filter-group">
          <legend>Prime filters</legend>
          <div class="filter-group-grid">
            <label class="filter-control">
              <span>Prime Role</span>
              <select id="filter-role">
                <option value="all">All roles</option>
                <option value="prime_in_twin_pair">Twin Prime</option>
                <option value="prime_not_in_twin_pair">Single Prime</option>
                <option value="not_prime">Not Prime</option>
              </select>
            </label>
          </div>
        </fieldset>
        <fieldset class="filter-group">
          <legend>Divisor filter</legend>
          <div class="filter-group-grid">
            <label class="filter-control">
              <span>Divisors</span>
              <input id="filter-divisors" type="text" inputmode="numeric" placeholder="2, 3, 5">
            </label>
            <label class="filter-control">
              <span>Match</span>
              <select id="filter-divisor-logic">
                <option value="or">Any divisor (OR)</option>
                <option value="and">All divisors (AND)</option>
              </select>
            </label>
          </div>
        </fieldset>
      </div>
      <div class="filter-column">
        <fieldset class="filter-group">
          <legend>Neighborhood filters</legend>
          <div class="filter-group-grid">
            <div class="filter-control">
              <span>Prime Neighborhood</span>
              <div id="filter-neighborhood" class="checkbox-group" role="group" aria-label="Prime Neighborhood">
                <label class="checkbox-pill"><input type="checkbox" value="twin_center"> <span>Twin Center</span></label>
                <label class="checkbox-pill"><input type="checkbox" value="next_to_one_prime"> <span>Next to one prime</span></label>
                <label class="checkbox-pill"><input type="checkbox" value="not_next_to_primes"> <span>No adjacent primes</span></label>
                <label class="checkbox-pill"><input type="checkbox" value="prime_edge_case"> <span>Prime edge case</span></label>
                <label class="checkbox-pill"><input type="checkbox" value="prime"> <span>Prime</span></label>
              </div>
            </div>
          </div>
        </fieldset>
        <fieldset class="filter-group">
          <legend>Range</legend>
          <div class="filter-range-row">
            <label class="filter-control">
              <span>Minimum</span>
              <input id="filter-min" type="number" min="1" placeholder="1">
            </label>
            <div class="filter-range-arrow" aria-hidden="true">&rarr;</div>
            <label class="filter-control">
              <span>Maximum</span>
              <input id="filter-max" type="number" min="1" placeholder="100">
            </label>
          </div>
        </fieldset>
      </div>
    </form>
  </section>
  <div id="table-state-explanation" class="explorer-state-explanation"></div>
  <section class="column-panel" aria-labelledby="column-panel-title">
    <div class="column-panel-header">
      <div>
        <h3 id="column-panel-title">Columns</h3>
        <p>Choose which details appear in the number classification table, including <a class="inline-link" href="/glossary#glossary-term-prime-neighborhood">prime neighborhood</a> and divisor views.</p>
      </div>
    </div>
    <div id="filter-columns" class="column-toggle-row" role="group" aria-label="Table Columns">
      <label class="checkbox-pill"><input type="checkbox" value="number_type" checked> <span>Number type</span></label>
      <label class="checkbox-pill"><input type="checkbox" value="prime_role"> <span>Prime role</span></label>
      <label class="checkbox-pill"><input type="checkbox" value="prime_neighborhood"> <span>Prime neighborhood</span></label>
      <label class="checkbox-pill"><input type="checkbox" value="prime_divisors" checked> <span>Prime divisors</span></label>
      <label class="checkbox-pill"><input type="checkbox" value="all_divisors" checked> <span>All divisors</span></label>
    </div>
  </section>
  <div id="number-table" class="scroll-region"></div>
</section>

<section class="panel">
  <div class="panel-heading">
    <div>
      <h2>Need More Interpretation?</h2>
      <p>Detailed modular, gap, factor, density, and expected-count views now live on their own page.</p>
    </div>
  </div>
  <div class="metric-grid">
    <article class="metric-box">
      <h3>Go Deeper</h3>
      <p>Open the dedicated Analysis page for the structured breakdowns that used to sit at the bottom of Explorer.</p>
      <p><a class="inline-link" href="/analysis">Open Analysis page</a></p>
    </article>
  </div>
</section>""",
    script_name="explorer.js",
)

ANALYSIS_PAGE = PageDefinition(
    route="/analysis",
    title="Twin Prime Exploration Lab | Analysis",
    nav_label="Analysis",
    active_route="analysis",
    meta_description="Read twin-prime ranges through modular structure, gaps, factors, density, and rough expected-versus-observed benchmarks.",
    hero_html="""<section class="hero-block hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">Analysis</p>
    <h1>Structured views for twin-prime patterns.</h1>
    <p class="hero-text">Deeper mathematical breakdowns for <a class="inline-link" href="/glossary#glossary-term-mod-6">modular structure</a>, <a class="inline-link" href="/glossary#glossary-term-prime-gap">prime gaps</a>, factorization signals, density windows, and expected-versus-observed counts.</p>
  </div>
  <form id="analysis-form" class="control-panel">
    <label>
      <span>Range Start</span>
      <input id="start-input" name="start" type="number" min="1" max="200000" value="1" required>
    </label>
    <label>
      <span>Range End</span>
      <input id="end-input" name="end" type="number" min="2" max="200000" value="100" required>
    </label>
    <button type="submit">Refresh Analysis</button>
    <p class="section-copy">Web ranges are capped at 20,000 numbers and an end value of 200,000 to keep the app responsive.</p>
  </form>
</section>""",
    main_html="""<section class="panel summary-panel">
  <div class="panel-heading">
    <div>
      <h2>Analysis Summary</h2>
      <p>Quick context for the current range before diving into the detailed views.</p>
    </div>
    <p id="status-text">Ready to analyze.</p>
  </div>
  <div id="summary-cards" class="summary-cards"></div>
</section>

<section class="panel">
  <div class="panel-heading">
    <div>
      <h2>How To Read The Analysis Page</h2>
      <p>Choose the question you want answered, then let the active tab guide the read.</p>
    </div>
  </div>
  <div class="glossary-jump-shell">
    <div class="glossary-strip-header">
      <p class="section-copy glossary-strip-label">Glossary links</p>
    </div>
    <div class="glossary-jump-strip" aria-label="Analysis glossary links">
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-mod-6" title="Open glossary entry: Mod 6">Mod 6</a>
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-prime-gap" title="Open glossary entry: Prime Gap">Prime Gap</a>
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-twin-center" title="Open glossary entry: Twin Center">Twin Center</a>
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-bounded-gaps-between-primes" title="Open glossary entry: Bounded Gaps Between Primes">Bounded Gaps Between Primes</a>
    </div>
  </div>
  <div class="metric-grid">
    <article class="metric-box">
      <h3>How this page helps</h3>
      <p>The Analysis page gives several coordinated reads of the same twin-prime range. Each tab changes the interpretation lens, not the underlying numbers.</p>
    </article>
    <article class="metric-box">
      <h3>If terms feel unfamiliar</h3>
      <p>Start with Modular or Gaps for the clearest pattern read. If terms like Mod 6, twin center, or heuristic feel unfamiliar, use the <a class="inline-link" href="/glossary">Glossary</a> for quick definitions, read <a class="inline-link" href="/why-mod-6-shows-up-so-often">Why Mod 6 Shows Up So Often</a> for a short modular refresher, or use the guide for a slightly fuller read.</p>
      <p><a class="inline-link" href="/analysis-guide" target="_blank" rel="noopener noreferrer">Open the full analysis guide in a new tab</a></p>
    </article>
  </div>
  <div class="insight-strip" aria-label="Recommended tab starting points">
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="modular">Start with Modular for structure</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="gaps">Start with Gaps for spacing</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="factors">Start with Factors for centers</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="density">Start with Density for clustering</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="expected">Use Expected last for a rough benchmark</button>
  </div>
</section>

<section class="panel analysis-panel">
  <div class="panel-heading">
    <div>
      <h2 id="analysis-views-title">Analysis Views</h2>
      <p>Switch between modular structure, gaps, factors, density, and expected counts.</p>
    </div>
  </div>
  <div class="tab-row" id="tab-row">
    <button class="tab-button active" data-tab="modular">Modular</button>
    <button class="tab-button" data-tab="gaps">Gaps</button>
    <button class="tab-button" data-tab="factors">Factors</button>
    <button class="tab-button" data-tab="density">Density</button>
    <button class="tab-button" data-tab="expected">Expected</button>
  </div>
  <div id="tab-content" class="scroll-region"></div>
</section>""",
    script_name="analysis.js",
)

ANALYSIS_GUIDE_PAGE = PageDefinition(
    route="/analysis-guide",
    title="Twin Prime Exploration Lab | Analysis Guide",
    nav_label="Analysis Guide",
    active_route="analysis",
    meta_description="A practical guide to reading the Analysis page, including modular patterns, prime gaps, factor views, density, and expected counts.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Analysis Guide</p>
    <h1>How to understand the analysis views.</h1>
    <p class="hero-text">A fuller explanation of what each analysis tab is measuring, what question it answers, and how to interpret the results together.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Analysis Guide</h2>
      <p>A practical reference for reading the Analysis page with more confidence.</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <h3>How the Analysis page is organized</h3>
      <p>The Analysis page takes one selected range and reuses the same twin-prime dataset across multiple views. That means the tabs are not separate calculations with separate inputs. They are coordinated interpretations of the same analyzed range.</p>
    </article>
    <article class="theory-section">
      <h3>Which tab should you open first?</h3>
      <p>Start with the question you are asking. If you want structural rules, begin with Modular. If you want spacing behavior, begin with Gaps. If you want to compare centers against other numbers, begin with Factors. If you want local clustering, begin with Density. If you want a rough heuristic benchmark, begin with Expected.</p>
    </article>
    <article class="theory-section">
      <h3>Modular view</h3>
      <p>Open Modular first when your question is, what structural pattern do twin-prime pairs seem to follow? The Modular tab shows residue patterns for twin-prime pairs and their centers, and it is the fastest way to inspect whether the usual 6k minus 1 and 6k plus 1 structure is appearing clearly in the selected range.</p>
    </article>
    <article class="theory-section">
      <h3>Gap view</h3>
      <p>Open Gaps first when your question is, how are twin-prime pairs spaced? The Gaps tab measures spacing between consecutive twin-prime pairs and between their centers. Use it when you want to see whether pairs appear tightly clustered, widely separated, or distributed in repeating gap sizes.</p>
    </article>
    <article class="theory-section">
      <h3>Factors view</h3>
      <p>Open Factors first when your question is, do twin-prime centers look arithmetically unusual? The Factors tab compares twin-prime centers against other even numbers. It helps answer whether centers show unusually simple or distinctive factorization behavior relative to a nearby baseline.</p>
    </article>
    <article class="theory-section">
      <h3>Density view</h3>
      <p>Open Density first when your question is, do twin primes live in locally richer prime neighborhoods? The Density tab measures how many primes and twin-prime pairs appear in local windows around each pair. This view is best when you want to compare local clustering against the global average for the same range.</p>
    </article>
    <article class="theory-section">
      <h3>Expected view</h3>
      <p>Open Expected when your question is, how does the observed count compare with a rough benchmark? The Expected tab compares observed twin-prime counts to N divided by log squared N. Treat it as a supporting benchmark, not as proof or as a full explanation of the range.</p>
    </article>
    <article class="theory-section">
      <h3>Recommended reading order</h3>
      <p>If you are exploring a new range for the first time, start with Modular, then Gaps, then Factors. Move to Density when you want to test whether the local environment around pairs looks special, and use Expected last when you want a coarse benchmark instead of a structural explanation.</p>
    </article>
    <article class="theory-section">
      <h3>How to read the tabs together</h3>
      <p>A useful pattern is to move from structural questions to comparative questions. Start with Modular and Gaps to see visible patterns, then move to Factors, Density, and Expected to test whether those patterns also show up in the broader summaries.</p>
      <p><a class="inline-link" href="/analysis">Return to the Analysis page</a></p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)


GLOSSARY_PAGE = PageDefinition(
    route="/glossary",
    title="Twin Prime Exploration Lab | Glossary",
    nav_label="Glossary",
    active_route="glossary",
    meta_description="Quick definitions for twin-prime, modular, gap, divisor, and theory terms used across the Twin Prime Exploration Lab.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Glossary</p>
    <h1>A shared vocabulary for exploring twin primes.</h1>
    <p class="hero-text">Quick, reliable definitions for the mathematical and site terms that appear across the Lab, Explorer, Analysis, and Theory pages.</p>
  </div>
</section>""",
    main_html="""<section class="panel glossary-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Glossary</h2>
      <p>A concise reference for core terms used throughout the Twin Prime Exploration Lab.</p>
    </div>
  </div>
  <div class="glossary-toolbar" aria-label="Glossary tools">
    <label class="glossary-search-control">
      <span>Search terms</span>
      <input id="glossary-search" type="search" placeholder="Search prime, twin center, mod 6...">
    </label>
  </div>
  <div id="glossary-sections"></div>
</section>""",
    script_name="theory.js",
)

THEORY_PAGE = PageDefinition(
    route="/theory",
    title="Twin Prime Exploration Lab | Theory",
    nav_label="Theory",
    active_route="theory",
    meta_description="Reference notes on the twin prime conjecture, modern progress, research approaches, and why the problem remains difficult.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Theory</p>
    <h1>The mathematical context behind twin-prime exploration.</h1>
    <p class="hero-text">The conceptual companion to the explorer, focused on the problem statement, the main research ideas, what modern breakthroughs actually proved, and why a proof remains difficult.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Theory</h2>
      <p>A concise guide to the twin prime problem, organized as readable reference notes rather than a long article.</p>
    </div>
  </div>
  <div class="glossary-jump-shell">
    <div class="glossary-strip-header">
      <p class="section-copy glossary-strip-label">Glossary links</p>
      <p class="glossary-strip-copy">These pills open glossary entries for the theory concepts below.</p>
    </div>
    <div class="glossary-jump-strip" aria-label="Related glossary links">
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-twin-prime-conjecture" title="Open glossary entry: Twin Prime Conjecture">Twin Prime Conjecture</a>
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-bounded-gaps-between-primes" title="Open glossary entry: Bounded Gaps Between Primes">Bounded Gaps Between Primes</a>
      <a class="insight-pill glossary-inline-link" href="/glossary#glossary-term-hardy-littlewood-conjecture" title="Open glossary entry: Hardy-Littlewood Conjecture">Hardy-Littlewood Conjecture</a>
    </div>
  </div>
  <section class="theory-block">
    <h3>Explore the site next</h3>
    <div class="metric-grid theory-path-grid">
      <article class="metric-box theory-path-card">
        <h4>Lab</h4>
        <p>The fastest route from a theory concept to a visible pattern.</p>
        <p><a class="inline-link" href="/lab#visualization-title">Open the Lab</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Explorer</h4>
        <p>Exact rows, divisors, and number-by-number inspection tied to the current theory topic.</p>
        <p><a class="inline-link" href="/explorer#number-table-title">Open Explorer</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Analysis</h4>
        <p>The same range interpreted through modular structure, gaps, density, and rough benchmarks.</p>
        <p><a class="inline-link" href="/analysis#analysis-views-title">Open Analysis</a></p>
      </article>
    </div>
  </section>
  <div class="theory-layout">
    <div class="theory-tabs-shell">
      <div class="theory-tabs" role="tablist" aria-label="Theory topics" id="theory-tablist"></div>
    </div>
    <div class="theory-content-shell">
      <div id="theory-tabpanel" class="theory-tabpanel" role="tabpanel" tabindex="0"></div>
    </div>
  </div>
</section>""",
    script_name="theory.js",
)

ABOUT_PAGE = PageDefinition(
    route="/about",
    title="Twin Prime Exploration Lab | About",
    nav_label="About",
    active_route="about",
    meta_description="About Twin Prime Exploration Lab, a small independent site for exploring primes, twin primes, twin centers, and related patterns.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">About</p>
    <h1>A small site for exploring primes and twin primes.</h1>
    <p class="hero-text">Twin Prime Exploration Lab is a focused mathematics site built for people who enjoy patterns in prime numbers and want a simple way to explore them a little more deeply.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>About This Site</h2>
      <p>What the site is for, who it is for, and what kind of experience it is trying to offer.</p>
    </div>
  </div>
  <div class="metric-grid">
    <article class="metric-box">
      <h3>What it is</h3>
      <p>A compact mathematics site for exploring prime structure, twin primes, twin centers, and a few related ways of reading the same range of numbers.</p>
    </article>
    <article class="metric-box">
      <h3>Who it is for</h3>
      <p>Anyone who likes number patterns, from casual curiosity and student exploration to more serious independent interest in prime behavior.</p>
    </article>
    <article class="metric-box">
      <h3>What makes it different</h3>
      <p>The site treats twin centers as part of the story, not just the primes around them, and it tries to connect visual discovery, exact inspection, interpretation, and reference notes in one place.</p>
    </article>
    <article class="metric-box">
      <h3>What it is not</h3>
      <p>It is not a proof tool, a full research environment, or a giant general-purpose number theory site. It stays intentionally narrow and exploratory.</p>
    </article>
  </div>
</section>

<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Ways To Explore The Site</h2>
      <p>The main pages are meant to work together without feeling heavy or technical.</p>
    </div>
  </div>
  <div class="metric-grid theory-path-grid">
    <article class="metric-box theory-path-card">
      <h3>Lab</h3>
      <p>Start with the visual side and scan a live range for structure.</p>
      <p><a class="inline-link" href="/lab">Open the Lab</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>Explorer</h3>
      <p>Look at exact rows, divisors, and filtered slices of the same numbers.</p>
      <p><a class="inline-link" href="/explorer">Open Explorer</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>Analysis</h3>
      <p>Read the range through modular patterns, gaps, factors, density, and rough benchmarks.</p>
      <p><a class="inline-link" href="/analysis">Open Analysis</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>Theory and Glossary</h3>
      <p>Use the reference pages when you want concept support or a quick definition.</p>
      <p><a class="inline-link" href="/theory">Open Theory</a> or <a class="inline-link" href="/glossary">Open Glossary</a></p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)

CONTACT_PAGE = PageDefinition(
    route="/contact",
    title="Twin Prime Exploration Lab | Contact",
    nav_label="Contact",
    active_route="contact",
    meta_description="Contact information, scope notes, and feedback expectations for the Twin Prime Exploration Lab site.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Contact</p>
    <h1>Questions, corrections, and general feedback.</h1>
    <p class="hero-text">This is a small independent site. If a public contact method is offered with the live release, this page is where it should be listed clearly.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Contact</h2>
      <p>This page is here to make the site feel transparent and reachable, even though it is a small independently maintained project.</p>
    </div>
  </div>
  <div class="metric-grid">
    <article class="metric-box">
      <h3>General questions</h3>
      <p>If you want to ask about the site, suggest a correction, or point out something unclear, use the contact method published with the live version of the site.</p>
    </article>
    <article class="metric-box">
      <h3>Site issues</h3>
      <p>If you notice a broken page, incorrect link, or behavior that does not match what the page says it should do, that is the most useful kind of feedback to send first.</p>
    </article>
    <article class="metric-box">
      <h3>Scope</h3>
      <p>This site is meant for playful exploration and reference, not formal support, tutoring, or custom mathematical research help.</p>
    </article>
    <article class="metric-box">
      <h3>Response expectations</h3>
      <p>Because the site is independently maintained, replies may be limited or slow. The contact route listed with the live release should be treated as the current best path.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)

PRIVACY_PAGE = PageDefinition(
    route="/privacy",
    title="Twin Prime Exploration Lab | Privacy Policy",
    nav_label="Privacy Policy",
    active_route="privacy",
    meta_description="Privacy policy for Twin Prime Exploration Lab, including the site's current handling of technical data, cookies, and future advertising changes.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Privacy Policy</p>
    <h1>How this site currently handles information.</h1>
    <p class="hero-text">This policy is written to match the current state of the site and should be updated again before advertising, analytics, or other third-party services go live.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Privacy Policy</h2>
      <p>Last updated: April 7, 2026</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <h3>What this site is</h3>
      <p>Twin Prime Exploration Lab is a mathematics website focused on twin-prime visualization, inspection, analysis, theory, and glossary reference content.</p>
    </article>
    <article class="theory-section">
      <h3>Information you actively provide</h3>
      <p>The site does not currently provide user accounts, comments, uploads, or on-site contact forms. If a direct contact method is added later, this policy should be updated to explain what information may be shared through that route.</p>
    </article>
    <article class="theory-section">
      <h3>Technical data and server logs</h3>
      <p>Like most websites, hosting or delivery infrastructure may record basic technical information such as IP address, browser type, referring pages, timestamps, and requested URLs for security, diagnostics, and normal site operations.</p>
    </article>
    <article class="theory-section">
      <h3>Cookies and tracking</h3>
      <p>The site does not currently present itself as using advertising cookies, user accounts, or a broader tracking stack. If analytics, advertising, consent tools, or other tracking technologies are added later, this policy should be updated before they are enabled.</p>
    </article>
    <article class="theory-section">
      <h3>Advertising</h3>
      <p>Google Ads or other advertising services are not described here as active unless they are actually deployed. If advertising is enabled in the future, this policy should be updated to describe those services, any related cookies or personalization behavior, and any consent choices offered to users.</p>
    </article>
    <article class="theory-section">
      <h3>Third-party links</h3>
      <p>This site may link to third-party destinations such as reference sources or other outside websites. Those sites have their own privacy practices, and this policy does not control how they handle information.</p>
    </article>
    <article class="theory-section">
      <h3>Policy updates</h3>
      <p>This page should be reviewed and updated whenever the site's data practices materially change, especially before analytics, ad technology, contact forms, or account features are introduced.</p>
    </article>
    <article class="theory-section">
      <h3>Questions about this policy</h3>
      <p>Use the <a class="inline-link" href="/contact">Contact page</a> for the currently supported public contact routes.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)

EXPERIMENTS_PAGE = PageDefinition(
    route="/experiments",
    title="Twin Prime Exploration Lab | Experiments",
    nav_label="Experiments",
    active_route="experiments",
    meta_description="A structured hypothesis workbench for testing bounded twin-prime rules and reading verdicts, evidence, and next steps.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Experiments</p>
    <h1>Test one structured rule against a live range.</h1>
    <p class="hero-text">Choose an experiment type, adjust a few meaningful parameters, and see whether the current twin-prime structure supports the rule you want to test.</p>
  </div>
</section>""",
    main_html=f'''<section class="panel experiments-panel">
  <div class="panel-heading">
    <div>
      <h2>Hypothesis Workbench</h2>
      <p>Pick a range, choose a structured experiment type, and read the evidence before deciding what to inspect next.</p>
    </div>
  </div>
  <div class="experiments-layout">
    <form id="analysis-form" class="control-panel experiments-controls">
      <div class="lab-card-copy">
        <h3>Experiment Setup</h3>
        <p>Use a bounded rule template so the result stays testable, readable, and grounded in twin-prime structure.</p>
      </div>
      <label>
        <span>Range Start</span>
        <input id="start-input" name="start" type="number" min="1" max="{MAX_WEB_END}" value="1" required>
      </label>
      <label>
        <span>Range End</span>
        <input id="end-input" name="end" type="number" min="2" max="{MAX_WEB_END}" value="600" required>
      </label>
      <button type="submit">Run Experiment</button>
      <div class="lab-experiment-panel experiment-setup-shell">
        <div class="experiment-setup-group">
          <label>
            <span>Experiment type</span>
            <select id="experiment-type">
              <option value="center-congruent">Twin centers congruent to k mod n</option>
              <option value="center-divisible">Twin centers divisible by n</option>
              <option value="pair-residues">Twin-prime pair residues mod n</option>
              <option value="center-spacing">Twin center spacing</option>
            </select>
          </label>
        </div>
        <div class="experiment-setup-group">
          <span class="filter-label">Parameters</span>
          <div id="experiment-parameter-fields" class="experiment-parameter-grid">
            <label id="experiment-param-1-group">
              <span id="experiment-param-1-label">Modulus</span>
              <input id="experiment-param-1" type="number" min="2" max="60" value="6">
            </label>
            <label id="experiment-param-2-group">
              <span id="experiment-param-2-label">Target residue</span>
              <input id="experiment-param-2" type="number" min="0" max="5" value="0">
            </label>
            <label id="experiment-param-3-group" class="is-hidden">
              <span id="experiment-param-3-label">Right residue</span>
              <input id="experiment-param-3" type="number" min="0" max="5" value="1">
            </label>
          </div>
        </div>
        <div id="experiment-template-summary" class="lab-experiment-summary active">Testing whether twin-prime centers above 4 land in residue 0 mod 6.</div>
        <p class="section-copy">Keep the interaction structured: choose an experiment type, adjust only the parameters that matter, and let the page return a verdict plus evidence.</p>
      </div>
      <p id="status-text" class="section-copy">Ready to test a range.</p>
      <p class="section-copy">Web ranges are capped at {MAX_WEB_RANGE_SIZE:,} numbers and an end value of {MAX_WEB_END:,}.</p>
    </form>
    <section class="experiments-results" aria-labelledby="experiment-results-title">
      <div class="lab-card-copy">
        <h3 id="experiment-results-title">Experiment Results</h3>
        <p>Read the verdict, check the evidence, and then continue into Explorer, Analysis, or Theory if the pattern looks meaningful.</p>
      </div>
      <div id="summary-cards" class="summary-cards"></div>
      <div id="experiment-results" class="analysis-layout">
        <div class="empty-note">Run an experiment to populate these results.</div>
      </div>
    </section>
  </div>
</section>''',
    script_name="experiments.js",
    include_in_nav=False,
)

EXPLANATORY_PAGE_DEFINITIONS = [_build_explanatory_page(content) for content in EXPLANATORY_PAGES]

PAGE_DEFINITIONS = [LAB_PAGE, EXPLORER_PAGE, ANALYSIS_PAGE, ANALYSIS_GUIDE_PAGE, GLOSSARY_PAGE, THEORY_PAGE, *EXPLANATORY_PAGE_DEFINITIONS, ABOUT_PAGE, CONTACT_PAGE, PRIVACY_PAGE, EXPERIMENTS_PAGE]
PAGE_BY_ROUTE = {page.route: page for page in PAGE_DEFINITIONS}
PAGE_BY_ACTIVE_ROUTE = {page.active_route: page for page in PAGE_DEFINITIONS}
