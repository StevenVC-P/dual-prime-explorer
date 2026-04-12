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
    robots_directive: str | None = None


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


def _render_explanatory_references(items: list[dict[str, str]]) -> str:
    return "".join(
        """<li><a class="inline-link" href="{href}" target="_blank" rel="noopener noreferrer">{label}</a>{note}</li>""".format(
            href=html.escape(item["href"], quote=True),
            label=html.escape(item["label"]),
            note=f" - {html.escape(item['note'])}" if item.get("note") else "",
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
    reviewed_html = ""
    if content.get("reviewed"):
        reviewed_html = """<p class="section-copy">{reviewed}</p>""".format(
            reviewed=html.escape(content["reviewed"])
        )
    references_html = ""
    if content.get("references"):
        references_html = """<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>References and further reading</h2>
      <p>These links support the theorem, history, and heuristic claims summarized on this page.</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <ul class="theory-reference-list">
        {references}
      </ul>
    </article>
  </div>
</section>""".format(
            references=_render_explanatory_references(content["references"])
        )
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
      {reviewed_html}
    </div>
  </div>
  <div class="section-stack">
    {sections}
  </div>
</section>

{references_html}

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
        reviewed_html=reviewed_html,
        sections=sections,
        references_html=references_html,
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


HOME_PAGE = PageDefinition(
    route="/",
    title="Twin Prime Explorer - Explore Prime Pairs, Patterns, and Gaps",
    nav_label="Home",
    active_route="home",
    meta_description="Explore twin primes, prime pairs, patterns, and gaps with Twin Prime Explorer. Start with the Lab, inspect ranges in Explorer, or use Analysis for deeper pattern views.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Twin Prime Explorer</p>
    <h1>Explore Twin Primes Visually</h1>
    <p class="hero-text">TwinPrimeExplorer.com helps you visualize prime pairs, inspect ranges, study gaps and patterns, and move between live tools and plain-language explanations without losing the thread.</p>
    <p class="section-copy"><a class="inline-link" href="/lab">Open the Lab</a> | <a class="inline-link" href="/explorer">Open Explorer</a> | <a class="inline-link" href="/analysis">Open Analysis</a></p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>What Twin Prime Explorer is for</h2>
      <p>A compact mathematics site for exploring twin primes, prime pairs, prime gaps, and the number patterns that appear around them.</p>
      <p class="section-copy">Use Twin Prime Explorer to visualize twin primes, inspect prime pairs inside real ranges, compare prime gaps, and move into plain-language explanations when you want more mathematical context.</p>
    </div>
  </div>
  <div class="metric-grid theory-path-grid">
    <article class="metric-box theory-path-card">
      <h3>See the pattern</h3>
      <p>Open the Lab when you want the fastest visual view of twin primes, twin centers, and range-level structure.</p>
      <p><a class="inline-link" href="/lab">Open the Lab</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>Inspect exact ranges</h3>
      <p>Use Explorer when you want row-by-row inspection, divisors, and number-level detail inside a chosen range.</p>
      <p><a class="inline-link" href="/explorer">Open Explorer</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>Read the pattern</h3>
      <p>Use Analysis when you want modular structure, gaps, density, and expected-versus-observed views of the same range.</p>
      <p><a class="inline-link" href="/analysis">Open Analysis</a></p>
    </article>
  </div>
</section>

<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Start with the math</h2>
      <p>These pages give the quickest route into the main ideas behind the tools.</p>
    </div>
  </div>
  <div class="metric-grid theory-path-grid">
    <article class="metric-box theory-path-card">
      <h3>Twin primes</h3>
      <p>Start with the core definition, simple examples, and the plain-language foundation for the whole site.</p>
      <p><a class="inline-link" href="/what-are-twin-primes">Read What Are Twin Primes?</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>Prime gaps</h3>
      <p>Use the gap page when you want the spacing story that sits behind twin primes and nearby comparisons.</p>
      <p><a class="inline-link" href="/prime-gaps">Read What Are Prime Gaps?</a></p>
    </article>
    <article class="metric-box theory-path-card">
      <h3>The open question</h3>
      <p>Read the conjecture page when you want the shortest careful statement of what is still unproved.</p>
      <p><a class="inline-link" href="/twin-prime-conjecture">Read Twin Prime Conjecture Explained</a></p>
    </article>
  </div>
</section>

<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Choose your next step</h2>
      <p>Use the route that matches how you want to learn or explore.</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <h3>Use Lab first</h3>
      <p>Choose Lab when you want a visual entry point and want to see twin primes, residues, and twin centers appear together in a live field.</p>
    </article>
    <article class="theory-section">
      <h3>Use Explorer first</h3>
      <p>Choose Explorer when your question is about exact numbers, divisors, local neighborhoods, or which rows belong in a twin-prime pair.</p>
    </article>
    <article class="theory-section">
      <h3>Use Analysis first</h3>
      <p>Choose Analysis when your question is about structure: gaps, density, modular patterns, or how a selected range compares with a rough benchmark.</p>
      <p>Need the reading path first? Open <a class="inline-link" href="/start-here">Start Here</a> for a guided route through the content, or use the <a class="inline-link" href="/glossary">Glossary</a> if you want quick definitions before opening the tools.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
)

LAB_PAGE = PageDefinition(
    route="/lab",
    title="Twin Prime Explorer - Visualize, Find, and Analyze Twin Primes",
    nav_label="Lab",
    active_route="lab",
    meta_description="Explore twin primes visually, inspect prime pairs by range, and analyze prime gaps, patterns, and twin centers with Twin Prime Explorer.",
    hero_html="""<section class="hero-block">
  <div class="hero-copy">
    <p class="eyebrow">Lab</p>
    <h1>Explore Twin Primes Visually</h1>
    <p class="hero-text">Use the Lab to visualize twin primes, explore prime pairs by range, and study patterns, gaps, and <a class="inline-link" href="/glossary#glossary-term-twin-center">twin-center</a> structure in the prime landscape.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>What is Twin Prime Explorer?</h2>
      <p>TwinPrimeExplorer.com is an educational math platform for exploring patterns in prime numbers, with a focus on twin primes and the number structures that appear around them.</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <p>Twin primes are pairs of prime numbers that differ by two, such as 11 and 13 or 17 and 19. This site combines visual exploration, structured analysis, and guided explanations so you can study how prime gaps behave, how twin-prime candidates appear, and why certain number patterns repeat across ranges.</p>
      <p>You can <a class="inline-link" href="/lab#visualization-title">explore patterns visually in the Lab</a>, <a class="inline-link" href="/explorer">inspect exact ranges in Explorer</a>, <a class="inline-link" href="/analysis">use Analysis to interpret what the patterns are showing</a>, and read <a class="inline-link" href="/theory">Theory</a> or the <a class="inline-link" href="/glossary">Glossary</a> for mathematical context.</p>
      <p>If you want the clearest background first, start with <a class="inline-link" href="/what-are-twin-primes">What Are Twin Primes?</a>, then compare that picture with <a class="inline-link" href="/prime-gaps">What Are Prime Gaps?</a> and the open-question framing in <a class="inline-link" href="/twin-prime-conjecture">Twin Prime Conjecture Explained</a>.</p>
    </article>
  </div>
</section>

<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Why study twin primes?</h2>
      <p>Twin primes are easy to define, but they sit next to one of the most famous open questions in number theory.</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <p>Individual prime numbers are familiar, but the way primes cluster, separate, and occasionally appear in closely spaced pairs remains deeply interesting. Studying twin primes helps reveal how prime numbers distribute across ranges, how small prime gaps behave, why some number patterns recur while others break down, and how visual and structural exploration can support mathematical intuition.</p>
      <p>If you want the plain-language entry point first, start with <a class="inline-link" href="/what-are-twin-primes">What Are Twin Primes?</a> before moving back into the live tools.</p>
    </article>
  </div>
</section>

<section class="panel explorer-lab-panel">
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
    <article class="metric-box">
      <h3>Need the plain-language overview?</h3>
      <p>Start with the educational intro before returning to the live views.</p>
      <p><a class="inline-link" href="/what-are-twin-primes">Read What Are Twin Primes?</a></p>
    </article>
  </div>
</section>""",
    script_name="explorer.js",
)

EXPLORER_PAGE = PageDefinition(
    route="/explorer",
    title="Twin Prime Finder and Explorer - Inspect Prime Pairs by Range",
    nav_label="Explorer",
    active_route="explorer",
    meta_description="Find twin primes in a selected range, inspect prime pairs row by row, and explore number structure through divisors, neighborhoods, and prime roles.",
    hero_html="""<section class="hero-block hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">Explorer</p>
    <h1>Inspect the range one number at a time.</h1>
    <p class="hero-text">Exact rows, <a class="inline-link" href="/glossary#glossary-term-divisor">divisor</a> filters, and number-level classifications that complement the visualization-first Lab.</p>
    <div class="metric-grid hero-metric-grid">
      <article class="metric-box">
        <h3>Best for</h3>
        <p>Checking exact twin-prime pairs, divisor patterns, and which numbers sit inside the range story you are inspecting.</p>
      </article>
      <article class="metric-box">
        <h3>Best next move</h3>
        <p>Use Explorer after the <a class="inline-link" href="/lab">Lab</a>, or move to <a class="inline-link" href="/analysis">Analysis</a> when you want the same range summarized through gaps and density.</p>
      </article>
    </div>
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
    <p class="section-copy">Need a fast refresher first? Read <a class="inline-link" href="/how-to-find-twin-primes">How To Find Twin Primes</a> or start with <a class="inline-link" href="/what-are-twin-primes">What Are Twin Primes?</a>.</p>
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
    title="Twin Prime Analysis - Prime Gaps, Density, and Pattern Views",
    nav_label="Analysis",
    active_route="analysis",
    meta_description="Analyze twin-prime ranges through prime gaps, density patterns, modular structure, and observed versus expected distributions.",
    hero_html="""<section class="hero-block hero-grid">
  <div class="hero-copy">
    <p class="eyebrow">Analysis</p>
    <h1>Structured views for twin-prime patterns.</h1>
    <p class="hero-text">Deeper mathematical breakdowns for <a class="inline-link" href="/glossary#glossary-term-mod-6">modular structure</a>, <a class="inline-link" href="/glossary#glossary-term-prime-gap">prime gaps</a>, factorization signals, density windows, and expected-versus-observed counts.</p>
    <div class="metric-grid hero-metric-grid">
      <article class="metric-box">
        <h3>Best for</h3>
        <p>Reading a selected range through structure instead of rows: modular patterns, spacing behavior, density, and center comparisons.</p>
      </article>
      <article class="metric-box">
        <h3>Best next move</h3>
        <p>Start here after <a class="inline-link" href="/explorer">Explorer</a> if you want interpretation, or open <a class="inline-link" href="/how-to-read-analysis">How To Read Analysis</a> for the fastest orientation.</p>
      </article>
    </div>
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
      <p><a class="inline-link" href="/how-to-read-analysis">Open the shorter analysis companion page</a> if you want the quick orientation first, or step back to <a class="inline-link" href="/prime-gaps">What Are Prime Gaps?</a> if the spacing language still feels unfamiliar.</p>
    </article>
    <article class="metric-box">
      <h3>If terms feel unfamiliar</h3>
      <p>Start with Modular or Gaps for the clearest pattern read. If terms like Mod 6, twin center, or heuristic feel unfamiliar, use the <a class="inline-link" href="/glossary">Glossary</a> for quick definitions, read <a class="inline-link" href="/why-mod-6-shows-up-so-often">Why Mod 6 Shows Up So Often</a> for a short modular refresher, revisit <a class="inline-link" href="/prime-gaps">What Are Prime Gaps?</a> for the spacing background, or compare the page with <a class="inline-link" href="/what-bounded-gaps-between-primes-actually-proved">What Bounded Gaps Between Primes Actually Proved</a> before using the guide for a slightly fuller read.</p>
      <p><a class="inline-link" href="/how-to-read-analysis">Open the shorter analysis companion page</a></p>
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
    title="TwinPrimeExplorer.com | Analysis Guide",
    nav_label="Analysis Guide",
    active_route="analysis",
    meta_description="A practical guide to interpreting TwinPrimeExplorer.com analysis views, including modular structure, prime gaps, factors, density, and rough benchmarks.",
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
      <p>This guide explains how to read the site's structured analysis outputs and how to interpret the mathematical signals they highlight. It is meant for visitors who want more than a tab label but less than a full theory article.</p>
      <p class="section-copy">Last reviewed: April 2026</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <h3>How the Analysis page is organized</h3>
      <p>The Analysis page takes one selected range and reuses the same twin-prime dataset across multiple views. That means the tabs are not separate calculations with separate inputs. They are coordinated interpretations of the same analyzed range.</p>
    </article>
    <article class="theory-section">
      <h3>Keep these terms nearby</h3>
      <p><strong>Residue</strong> means the remainder a number leaves after division by a chosen modulus. <strong>Prime gap</strong> means the difference between one prime and the next. <strong>Twin center</strong> means the number between two twin primes. <strong>Expected</strong> on this site means a rough benchmark, not a theorem and not a promise that the selected range must behave a certain way.</p>
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
      <p>The rough idea behind that expression is that primes thin out as numbers grow, and the chance of seeing two prime-like events together is much smaller than the chance of seeing one. That is why log terms keep appearing in prime-density discussions. On this site, Expected is intentionally framed as a quick comparison layer, not as a full Hardy-Littlewood model and not as a proof-backed prediction for every interval.</p>
    </article>
    <article class="theory-section">
      <h3>Recommended reading order</h3>
      <p>If you are exploring a new range for the first time, start with Modular, then Gaps, then Factors. Move to Density when you want to test whether the local environment around pairs looks special, and use Expected last when you want a coarse benchmark instead of a structural explanation.</p>
    </article>
    <article class="theory-section">
      <h3>Three quick reading recipes</h3>
      <p>If your question is <em>why does Mod 6 keep appearing?</em>, start with Modular and then compare the same range in the Lab. If your question is <em>are twin-prime pairs clumping or spreading out?</em>, start with Gaps and then use Density to see whether local neighborhoods also look unusual. If your question is <em>does this range look high or low for twin primes?</em>, start with Expected, then move back to Gaps and Modular so the benchmark does not float free of the actual structure.</p>
    </article>
    <article class="theory-section">
      <h3>How to read the tabs together</h3>
      <p>A useful pattern is to move from structural questions to comparative questions. Start with Modular and Gaps to see visible patterns, then move to Factors, Density, and Expected to test whether those patterns also show up in the broader summaries.</p>
      <p><a class="inline-link" href="/how-to-read-analysis">Use the shorter companion page</a> if you want a faster entry route before returning to the longer guide.</p>
      <p><a class="inline-link" href="/analysis">Return to the Analysis page</a></p>
    </article>
    <article class="theory-section">
      <h3>Take this back into the tools</h3>
      <p>Use the live <a class="inline-link" href="/analysis">Analysis page</a> when you want to compare a real range, then move into the <a class="inline-link" href="/lab">Lab</a> or <a class="inline-link" href="/explorer">Explorer</a> if you want to see the same idea from a visual or row-by-row angle.</p>
    </article>
  </div>
</section>

<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>References and further reading</h2>
      <p>These links support the benchmark and heuristic framing used in the guide.</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <ul class="theory-reference-list">
        <li><a class="inline-link" href="https://www.britannica.com/science/number-theory/Prime-number-theorem" target="_blank" rel="noopener noreferrer">Britannica: prime number theorem</a> - background for the average-density and log-term discussion.</li>
        <li><a class="inline-link" href="https://primes.utm.edu/glossary/page.php?sort=TwinPrimeConstant" target="_blank" rel="noopener noreferrer">PrimePages: twin prime constant</a> - compact reference for the heuristic correction factor behind twin-prime expectations.</li>
        <li><a class="inline-link" href="https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf" target="_blank" rel="noopener noreferrer">Hardy and Littlewood, Some Problems of Partitio Numerorum (V)</a> - classic source for the prime-pair heuristic framework.</li>
      </ul>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)


GLOSSARY_PAGE = PageDefinition(
    route="/glossary",
    title="TwinPrimeExplorer.com | Glossary",
    nav_label="Glossary",
    active_route="glossary",
    meta_description="A glossary of the core twin-prime, modular, gap, divisor, and theory terms used across TwinPrimeExplorer.com.",
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
      <p>This glossary collects the core terms used throughout TwinPrimeExplorer.com so visitors can move between the educational pages and interactive tools without losing context. Use it when a definition should stay short, clear, and tied to the rest of the site.</p>
      <p class="section-copy">Last reviewed: April 2026</p>
    </div>
  </div>
  <div class="glossary-toolbar" aria-label="Glossary tools">
    <label class="glossary-search-control">
      <span>Search terms</span>
      <input id="glossary-search" type="search" placeholder="Search prime, twin center, mod 6...">
    </label>
  </div>
  <div id="glossary-sections"></div>
  <div class="section-stack">
    <article class="theory-section">
      <h3>Selected references</h3>
      <ul class="theory-reference-list">
        <li><a class="inline-link" href="https://www.britannica.com/science/prime-number" target="_blank" rel="noopener noreferrer">Britannica: prime number</a> - basic reference for the foundational number-theory terms used throughout the site.</li>
        <li><a class="inline-link" href="https://mathworld.wolfram.com/TwinPrimeConjecture.html" target="_blank" rel="noopener noreferrer">MathWorld: Twin Prime Conjecture</a> - compact reference for the research-facing conjecture terms in the glossary.</li>
        <li><a class="inline-link" href="https://annals.math.princeton.edu/2014/179-3/p07" target="_blank" rel="noopener noreferrer">Yitang Zhang, Bounded gaps between primes</a> - theorem-level source for the bounded-gaps glossary entry.</li>
        <li><a class="inline-link" href="https://primes.utm.edu/glossary/page.php?sort=TwinPrimeConstant" target="_blank" rel="noopener noreferrer">PrimePages: twin prime constant</a> - compact reference for the Hardy-Littlewood and twin-prime-constant entries.</li>
      </ul>
    </article>
    <article class="theory-section">
      <h3>Where to use these terms next</h3>
      <p>Open <a class="inline-link" href="/start-here">Start Here</a> if you want a guided reading path first, move to the <a class="inline-link" href="/lab">Lab</a> if you want to see terms like twin center and Mod 6 in a live range, continue to <a class="inline-link" href="/analysis">Analysis</a> for structured interpretation, or read <a class="inline-link" href="/what-are-twin-primes">What Are Twin Primes?</a> if you want the quickest educational entry page.</p>
      <p>For newer background clusters, move from <a class="inline-link" href="/prime-number-theorem">The Prime Number Theorem In Plain Language</a> to <a class="inline-link" href="/why-log-n-appears-in-prime-number-theory">Why log n Appears In Prime Number Theory</a> when you want average-density context, use <a class="inline-link" href="/hardy-littlewood-twin-primes">Hardy-Littlewood For Twin Primes</a> when you want the heuristic side of the twin-prime story, or use <a class="inline-link" href="/how-to-read-prime-patterns-in-the-lab">How To Read Prime Patterns In The Lab</a> if you want the educational pages to feed more directly into the live tools.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
)

THEORY_PAGE = PageDefinition(
    route="/theory",
    title="TwinPrimeExplorer.com | Theory",
    nav_label="Theory",
    active_route="theory",
    meta_description="Educational background on the twin prime conjecture, research progress, key approaches, and why twin-prime patterns remain mathematically difficult.",
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
      <p>This section introduces the core ideas behind twin-prime exploration on this site. It is meant to help readers understand the patterns, questions, and terminology that appear throughout the Lab, Explorer, Analysis, and the standalone educational pages.</p>
      <p class="section-copy">Last reviewed: April 2026</p>
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
    <h3>Start reading here</h3>
    <div class="metric-grid theory-path-grid">
      <article class="metric-box theory-path-card">
        <h4>Reading Guide</h4>
        <p>Use one page to map a clear educational route through the site before you branch into tools or deeper theory.</p>
        <p><a class="inline-link" href="/start-here">Open Start Here</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Prime Numbers</h4>
        <p>Begin with the basic prime-versus-composite split if you want the cleanest foundation for everything else.</p>
        <p><a class="inline-link" href="/prime-numbers">Read Prime Numbers Explained</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Prime Gaps</h4>
        <p>Use the gap page when you want spacing language before bounded gaps or the conjecture.</p>
        <p><a class="inline-link" href="/prime-gaps">Read What Are Prime Gaps?</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Twin Prime Conjecture</h4>
        <p>Use the conjecture page for the shortest clear statement of the big open question behind the site.</p>
        <p><a class="inline-link" href="/twin-prime-conjecture">Read Twin Prime Conjecture Explained</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Finding Twin Primes</h4>
        <p>Use the finding guide when you want a practical bridge from definitions and residues back to concrete examples.</p>
        <p><a class="inline-link" href="/how-to-find-twin-primes">Read How To Find Twin Primes</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Prime Number Theorem</h4>
        <p>Use the average-density page when you want the background theorem behind thinning primes, log terms, and expected-count language.</p>
        <p><a class="inline-link" href="/prime-number-theorem">Read The Prime Number Theorem In Plain Language</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Infinitely Many Twin Primes?</h4>
        <p>Use the search-style question page when you want the shortest careful answer about expectation versus proof.</p>
        <p><a class="inline-link" href="/are-there-infinitely-many-twin-primes">Read Are There Infinitely Many Twin Primes?</a></p>
      </article>
    </div>
  </section>

  <section class="theory-block">
    <h3>Go deeper by question type</h3>
    <div class="metric-grid theory-path-grid">
      <article class="metric-box theory-path-card">
        <h4>Heuristic Background</h4>
        <p>Hardy-Littlewood, the softer expectation page, and the log n background pages explain why mathematicians expect continuing twin-prime structure without calling that expectation a proof.</p>
        <p><a class="inline-link" href="/hardy-littlewood-twin-primes">Read Hardy-Littlewood For Twin Primes</a> or <a class="inline-link" href="/why-twin-primes-are-expected-to-continue-forever">Read Why Twin Primes Are Expected To Continue Forever</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Progress Near Misses</h4>
        <p>Use Chen's theorem and bounded-gap pages when you want theorem-level progress that comes close to twin primes without crossing the exact gap-2 line.</p>
        <p><a class="inline-link" href="/chens-theorem">Read Chen's Theorem Explained</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Research Background</h4>
        <p>Arithmetic progressions and modular structure help explain why the site's residue-class language belongs to real prime-number research rather than only visualization shortcuts.</p>
        <p><a class="inline-link" href="/arithmetic-progressions-primes">Read Arithmetic Progressions Explained For Prime Patterns</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Clarify Similar Ideas</h4>
        <p>Use the bridge pages when prime gaps, prime pairs, bounded gaps, and related terms are starting to blur together.</p>
        <p><a class="inline-link" href="/prime-gaps-vs-prime-pairs">Read Prime Gaps vs Prime Pairs</a></p>
      </article>
      <article class="metric-box theory-path-card">
        <h4>Read The Tools Better</h4>
        <p>Use the Lab-reading guide when you want the educational pages to feed back into the live visual and analysis surfaces more deliberately.</p>
        <p><a class="inline-link" href="/how-to-read-prime-patterns-in-the-lab">Read How To Read Prime Patterns In The Lab</a></p>
      </article>
    </div>
  </section>

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
  <section class="theory-block">
    <h3>Selected references</h3>
    <div class="section-stack">
      <article class="theory-section">
        <ul class="theory-reference-list">
          <li><a class="inline-link" href="https://annals.math.princeton.edu/2014/179-3/p07" target="_blank" rel="noopener noreferrer">Yitang Zhang, Bounded gaps between primes</a> - Annals of Mathematics, 2014.</li>
          <li><a class="inline-link" href="https://annals.math.princeton.edu/2015/181-1/p07" target="_blank" rel="noopener noreferrer">James Maynard, Small gaps between primes</a> - Annals of Mathematics, 2015.</li>
          <li><a class="inline-link" href="https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes" target="_blank" rel="noopener noreferrer">Polymath8 bounded-gaps retrospective and bounds timeline</a> - collaborative project overview.</li>
          <li><a class="inline-link" href="https://mathworld.wolfram.com/PrimeNumberTheorem.html" target="_blank" rel="noopener noreferrer">Prime Number Theorem</a> - compact reference for the average prime-density statement.</li>
          <li><a class="inline-link" href="https://primes.utm.edu/glossary/page.php?sort=TwinPrimeConstant" target="_blank" rel="noopener noreferrer">PrimePages: twin prime constant</a> - heuristic background for Hardy-Littlewood style predictions.</li>
          <li><a class="inline-link" href="https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf" target="_blank" rel="noopener noreferrer">Hardy and Littlewood, Some Problems of Partitio Numerorum (V)</a> - classic source for prime-pair heuristics.</li>
        </ul>
      </article>
    </div>
  </section>
  <div class="section-stack">
    <article class="theory-section">
      <h3>Take the theory back into the tools</h3>
      <p>Once a concept here makes sense, use the <a class="inline-link" href="/lab">Lab</a> to see it in a live range, the <a class="inline-link" href="/explorer">Explorer</a> to inspect exact rows, or <a class="inline-link" href="/analysis">Analysis</a> to compare the same idea through modular, gap, factor, and density views.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
)

ABOUT_PAGE = PageDefinition(
    route="/about",
    title="TwinPrimeExplorer.com | About",
    nav_label="About",
    active_route="about",
    meta_description="About TwinPrimeExplorer.com, a small independent site for exploring primes, twin primes, twin centers, and related patterns.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">About</p>
    <h1>A small site for exploring primes and twin primes.</h1>
    <p class="hero-text">TwinPrimeExplorer.com is a focused mathematics site built for people who enjoy patterns in prime numbers and want a simple way to explore them a little more deeply.</p>
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
    <article class="metric-box theory-path-card">
      <h3>Start Reading</h3>
      <p>Use the educational reading guide if you want a clear order for learning the site's main ideas.</p>
      <p><a class="inline-link" href="/start-here">Open Start Here</a></p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)

CONTACT_PAGE = PageDefinition(
    route="/contact",
    title="TwinPrimeExplorer.com | Contact",
    nav_label="Contact",
    active_route="contact",
    meta_description="Contact information, scope notes, and feedback expectations for TwinPrimeExplorer.com.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Contact</p>
    <h1>Questions, corrections, and general feedback.</h1>
    <p class="hero-text">TwinPrimeExplorer.com is independently maintained. The best public contact route is email, especially for corrections, broken links, or site issues.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Contact</h2>
      <p>Use email for questions about the site, corrections, or reports about something that is not working as expected.</p>
    </div>
  </div>
  <div class="metric-grid">
    <article class="metric-box">
      <h3>Email</h3>
      <p><a class="inline-link" href="mailto:contact@twinprimeexplorer.com">contact@twinprimeexplorer.com</a></p>
      <p>This is the best public contact route for TwinPrimeExplorer.com.</p>
    </article>
    <article class="metric-box">
      <h3>Best reasons to reach out</h3>
      <p>Broken pages, incorrect links, factual corrections, and places where the site feels unclear are the most useful messages to send first.</p>
    </article>
    <article class="metric-box">
      <h3>Scope</h3>
      <p>This site is meant for playful exploration and reference, not formal support, tutoring, or custom mathematical research help.</p>
    </article>
    <article class="metric-box">
      <h3>Response expectations</h3>
      <p>Because the site is independently maintained, replies may be limited or slow, but email is the active public contact path.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)

PRIVACY_PAGE = PageDefinition(
    route="/privacy",
    title="TwinPrimeExplorer.com | Privacy Policy",
    nav_label="Privacy Policy",
    active_route="privacy",
    meta_description="Privacy policy for TwinPrimeExplorer.com, including the site's current handling of technical data, telemetry, cookies, and future advertising changes.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Privacy Policy</p>
    <h1>How this site currently handles information.</h1>
    <p class="hero-text">This policy is written to match the site's current live behavior, including basic hosting telemetry, and should be updated again before advertising or additional tracking tools go live.</p>
  </div>
</section>""",
    main_html="""<section class="panel theory-panel">
  <div class="panel-heading theory-heading">
    <div>
      <h2>Privacy Policy</h2>
      <p>Last updated: April 8, 2026</p>
    </div>
  </div>
  <div class="section-stack">
    <article class="theory-section">
      <h3>What this site is</h3>
      <p>TwinPrimeExplorer.com is a mathematics website focused on twin-prime visualization, inspection, analysis, theory, and glossary reference content.</p>
    </article>
    <article class="theory-section">
      <h3>Information you actively provide</h3>
      <p>The site does not currently provide user accounts, comments, uploads, or on-site contact forms. If you email the site directly, the information you choose to send is used only to read and respond to that message.</p>
    </article>
    <article class="theory-section">
      <h3>Technical data and server logs</h3>
      <p>Like most websites, hosting and delivery infrastructure may record basic technical information such as IP address, browser type, referring pages, timestamps, and requested URLs for security, diagnostics, performance, and normal site operations.</p>
    </article>
    <article class="theory-section">
      <h3>Telemetry and basic analytics</h3>
      <p>The live site currently uses Cloudflare services, including a Cloudflare Insights beacon, to measure basic traffic and site performance. This is used for lightweight operational insight rather than a full user-account or on-site profile system.</p>
    </article>
    <article class="theory-section">
      <h3>Cookies and tracking</h3>
      <p>This site does not currently present itself as using advertising cookies or account-based personalization. However, hosting, security, or telemetry services may process limited technical data as part of normal delivery and measurement.</p>
    </article>
    <article class="theory-section">
      <h3>Advertising</h3>
      <p>Google Ads or other advertising services are not described here as active unless they are actually deployed. If advertising is enabled in the future, this policy should be updated before those services go live to describe any related cookies, personalization behavior, and consent choices.</p>
    </article>
    <article class="theory-section">
      <h3>Third-party links</h3>
      <p>This site may link to third-party destinations such as reference sources or other outside websites. Those sites have their own privacy practices, and this policy does not control how they handle information.</p>
    </article>
    <article class="theory-section">
      <h3>Policy updates</h3>
      <p>This page should be reviewed and updated whenever the site's data practices materially change, especially before analytics changes, ad technology, contact forms, or account features are introduced.</p>
    </article>
    <article class="theory-section">
      <h3>Questions about this policy</h3>
      <p>Use the <a class="inline-link" href="/contact">Contact page</a> for the current public contact route.</p>
    </article>
  </div>
</section>""",
    script_name="theory.js",
    include_in_nav=False,
)

EXPERIMENTS_PAGE = PageDefinition(
    route="/experiments",
    title="TwinPrimeExplorer.com | Experiments",
    nav_label="Experiments",
    active_route="experiments",
    meta_description="An archived twin-prime experiments workbench kept available as a limited reference surface.",
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Experiments</p>
    <h1>Archived structured experiments.</h1>
    <p class="hero-text">This page remains available as a limited workbench reference, but the main public TwinPrimeExplorer.com experience is centered on Lab, Explorer, Analysis, Theory, and Glossary.</p>
  </div>
</section>""",
    main_html=f'''<section class="panel experiments-panel">
  <div class="panel-heading">
    <div>
      <h2>Hypothesis Workbench</h2>
      <p>This archived workbench is still available for limited testing, but it is no longer part of the site's main guided flow.</p>
    </div>
  </div>
  <div class="experiments-layout">
    <form id="analysis-form" class="control-panel experiments-controls">
      <div class="lab-card-copy">
        <h3>Experiment Setup</h3>
        <p>Use a bounded rule template if you want to inspect this archived surface, but start with Lab, Explorer, or Analysis for the main product flow.</p>
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
    robots_directive="noindex,follow",
)

EXPLANATORY_PAGE_DEFINITIONS = [_build_explanatory_page(content) for content in EXPLANATORY_PAGES]

PAGE_DEFINITIONS = [HOME_PAGE, LAB_PAGE, EXPLORER_PAGE, ANALYSIS_PAGE, ANALYSIS_GUIDE_PAGE, GLOSSARY_PAGE, THEORY_PAGE, *EXPLANATORY_PAGE_DEFINITIONS, ABOUT_PAGE, CONTACT_PAGE, PRIVACY_PAGE, EXPERIMENTS_PAGE]
PAGE_BY_ROUTE = {page.route: page for page in PAGE_DEFINITIONS}
PAGE_BY_ACTIVE_ROUTE = {page.active_route: page for page in PAGE_DEFINITIONS}
