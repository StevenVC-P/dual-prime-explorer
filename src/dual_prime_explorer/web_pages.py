"""HTML page definitions for the web UI."""

from __future__ import annotations

from dataclasses import dataclass

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
    include_in_nav: bool = True


LAB_PAGE = PageDefinition(
    route="/lab",
    title="Twin Prime Exploration Lab | Lab",
    nav_label="Lab",
    active_route="lab",
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
      <p class="section-copy">Updates live while you adjust the range. Web ranges are capped at 20,000 numbers and an end value of 200,000.</p>
      <p class="section-copy"><a class="inline-link" href="/explorer">Open the detailed Explorer page</a></p>
    </form>
    <section class="lab-visualization-card" aria-labelledby="visualization-title">
      <div class="lab-card-header">
        <div>
          <h3 id="visualization-title">Prime Field</h3>
          <p class="section-copy"><a class="inline-link" href="/glossary#glossary-term-twin-center">Twin centers</a> mark where twin primes occur.</p>
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
      <p>Use Analysis for modular patterns, gaps, factor signals, density, and heuristic comparisons.</p>
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
    <p class="section-copy">Web ranges are capped at 20,000 numbers and an end value of 200,000.</p>
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
      <h2>Analysis Page</h2>
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
    title="Dual Prime Explorer | Analysis",
    nav_label="Analysis",
    active_route="analysis",
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
    <p class="section-copy">Web ranges are capped at 20,000 numbers and an end value of 200,000.</p>
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
      <p>A quick orientation before you move through the tabbed views.</p>
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
      <h3>What this page does</h3>
      <p>The Analysis page turns one selected number range into several mathematical views. Each tab is looking at the same twin-prime data from a different angle: structure, spacing, factorization, local clustering, or heuristic comparison.</p>
    </article>
    <article class="metric-box">
      <h3>How to use the tabs</h3>
      <p>Start with Modular or Gaps if you want pattern recognition, then move to Factors, Density, and Expected when you want comparison metrics and broader interpretation.</p>
      <p><a class="inline-link" href="/analysis-guide" target="_blank" rel="noopener noreferrer">Open the full analysis guide in a new tab</a></p>
    </article>
  </div>
  <div class="insight-strip" aria-label="Recommended tab starting points">
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="modular">Start with Modular for structure</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="gaps">Start with Gaps for spacing</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="factors">Start with Factors for centers</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="density">Start with Density for clustering</button>
    <button class="insight-pill insight-pill-button" type="button" data-analysis-target="expected">Start with Expected for heuristic comparison</button>
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
    title="Dual Prime Explorer | Analysis Guide",
    nav_label="Analysis Guide",
    active_route="analysis",
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
      <p>Open Expected first when your question is, how does the observed count compare with a common heuristic? The Expected tab compares observed twin-prime counts to the heuristic N divided by log squared N. It does not prove anything by itself, but it helps you judge whether the observed range behaves roughly in line with a common asymptotic expectation.</p>
    </article>
    <article class="theory-section">
      <h3>Recommended reading order</h3>
      <p>If you are exploring a new range for the first time, start with Modular, then Gaps, then Factors. Move to Density when you want to test whether the local environment around pairs looks special, and use Expected last when you want a coarse benchmark instead of a structural explanation.</p>
    </article>
    <article class="theory-section">
      <h3>How to read the tabs together</h3>
      <p>A useful pattern is to move from structural questions to comparative questions. Start with Modular and Gaps to see visible patterns, then move to Factors, Density, and Expected to test whether those patterns also show up in aggregate measurements and heuristic comparisons.</p>
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
    hero_html="""<section class="hero-block theory-hero">
  <div class="hero-copy theory-copy">
    <p class="eyebrow">Glossary</p>
    <h1>A shared vocabulary for exploring twin primes.</h1>
    <p class="hero-text">Quick, reliable definitions for the mathematical and product terms that appear across the Lab, Explorer, Analysis, and Theory pages.</p>
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
    title="Dual Prime Explorer | Theory",
    nav_label="Theory",
    active_route="theory",
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
      <p>A concise guide to the twin prime problem, organized as product-style reference notes rather than a long article.</p>
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
    <h3>Choose your next product surface</h3>
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
        <p>The same range interpreted through modular structure, gaps, density, and heuristics.</p>
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

EXPERIMENTS_PAGE = PageDefinition(
    route="/experiments",
    title="Dual Prime Explorer | Experiments",
    nav_label="Experiments",
    active_route="experiments",
    hero_html="""<section class=\"hero-block theory-hero\">\n  <div class=\"hero-copy theory-copy\">\n    <p class=\"eyebrow\">Experiments</p>\n    <h1>Hypothesis-driven tools are coming next.</h1>\n    <p class=\"hero-text\">This space is reserved for future workflows that compare conjectures, save experiment settings, and turn the current analysis engine into a more explicit research notebook.</p>\n  </div>\n</section>""",
    main_html="""<section class=\"panel theory-panel\">\n  <div class=\"panel-heading theory-heading\">\n    <div>\n      <h2>Experiments</h2>\n      <p>Planned direction for the next layer of the app.</p>\n    </div>\n  </div>\n  <div class=\"metric-grid\">\n    <article class=\"metric-box\">\n      <h3>Future Workbench</h3>\n      <p>Compare multiple ranges side by side, save conjecture notes, and test hypotheses against the explorer output.</p>\n    </article>\n    <article class=\"metric-box\">\n      <h3>Why It Is Separate</h3>\n      <p>The app now has clear roles: Explorer for computation, Analysis for structured views, Theory for context, and Experiments for future hypothesis testing.</p>\n    </article>\n  </div>\n</section>""",
    script_name="theory.js",
)

PAGE_DEFINITIONS = [LAB_PAGE, EXPLORER_PAGE, ANALYSIS_PAGE, ANALYSIS_GUIDE_PAGE, GLOSSARY_PAGE, THEORY_PAGE, EXPERIMENTS_PAGE]
PAGE_BY_ROUTE = {page.route: page for page in PAGE_DEFINITIONS}
PAGE_BY_ACTIVE_ROUTE = {page.active_route: page for page in PAGE_DEFINITIONS}
