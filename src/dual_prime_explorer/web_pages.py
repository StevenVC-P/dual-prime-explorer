"""HTML page definitions for the web UI."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PageDefinition:
    route: str
    title: str
    nav_label: str
    active_route: str
    hero_html: str
    main_html: str
    script_name: str


EXPLORER_PAGE = PageDefinition(
    route="/explorer",
    title="Dual Prime Explorer | Explorer",
    nav_label="Explorer",
    active_route="explorer",
    hero_html="""<section class=\"hero-block hero-grid\">\n  <div class=\"hero-copy\">\n    <p class=\"eyebrow\">Explorer</p>\n    <h1>Computation-first twin-prime exploration.</h1>\n    <p class=\"hero-text\">Generate a range, inspect the number-level classification, and move into the dedicated analysis page when you want modular, gap, factor, density, and heuristic views.</p>\n  </div>\n  <form id=\"analysis-form\" class=\"control-panel\">\n    <label>\n      <span>Range Start</span>\n      <input id=\"start-input\" name=\"start\" type=\"number\" min=\"1\" value=\"1\" required>\n    </label>\n    <label>\n      <span>Range End</span>\n      <input id=\"end-input\" name=\"end\" type=\"number\" min=\"2\" value=\"100\" required>\n    </label>\n    <button type=\"submit\">Analyze Range</button>\n  </form>\n</section>""",
    main_html="""<section class=\"panel summary-panel\">\n  <div class=\"panel-heading\">\n    <div>\n      <h2>Summary</h2>\n      <p>Core counts and quick signals from the current range.</p>\n    </div>\n    <p id=\"status-text\">Ready to analyze.</p>\n  </div>\n  <div id=\"summary-cards\" class=\"summary-cards\"></div>\n</section>\n\n<section class=\"panel table-panel\">\n  <div class=\"panel-heading\">\n    <div>\n      <h2>Number Table</h2>\n      <p>Prime membership, neighborhood structure, and divisibility for each number.</p>\n    </div>\n    <p id=\"table-filter-status\">Showing all rows.</p>\n  </div>\n  <section class=\"filter-panel\" aria-labelledby=\"filter-panel-title\">\n    <div class=\"filter-panel-header\">\n      <div>\n        <h3 id=\"filter-panel-title\">Filters</h3>\n        <p>Refine the number table by prime role, neighborhood, divisors, or numeric range.</p>\n      </div>\n      <button id=\"filter-reset\" class=\"filter-reset-button\" type=\"button\">Reset Filters</button>\n    </div>\n    <form id="table-filter-form" class="filter-layout">
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
        <p>Choose which details appear in the number classification table.</p>
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
  <div id=\"number-table\" class=\"scroll-region\"></div>\n</section>\n\n<section class=\"panel\">\n  <div class=\"panel-heading\">\n    <div>\n      <h2>Analysis Page</h2>\n      <p>Detailed modular, gap, factor, density, and expected-count views now live on their own page.</p>\n    </div>\n  </div>\n  <div class=\"metric-grid\">\n    <article class=\"metric-box\">\n      <h3>Go Deeper</h3>\n      <p>Open the dedicated Analysis page for the structured breakdowns that used to sit at the bottom of Explorer.</p>\n      <p><a class=\"inline-link\" href=\"/analysis\">Open Analysis page</a></p>\n    </article>\n  </div>\n</section>""",
    script_name="explorer.js",
)

ANALYSIS_PAGE = PageDefinition(
    route="/analysis",
    title="Dual Prime Explorer | Analysis",
    nav_label="Analysis",
    active_route="analysis",
    hero_html="""<section class=\"hero-block hero-grid\">\n  <div class=\"hero-copy\">\n    <p class=\"eyebrow\">Analysis</p>\n    <h1>Structured views for twin-prime patterns.</h1>\n    <p class=\"hero-text\">Use this page for the deeper mathematical breakdowns: modular structure, pair gaps, factorization signals, density windows, and expected-versus-observed counts.</p>\n  </div>\n  <form id=\"analysis-form\" class=\"control-panel\">\n    <label>\n      <span>Range Start</span>\n      <input id=\"start-input\" name=\"start\" type=\"number\" min=\"1\" value=\"1\" required>\n    </label>\n    <label>\n      <span>Range End</span>\n      <input id=\"end-input\" name=\"end\" type=\"number\" min=\"2\" value=\"100\" required>\n    </label>\n    <button type=\"submit\">Refresh Analysis</button>\n  </form>\n</section>""",
    main_html="""<section class=\"panel summary-panel\">\n  <div class=\"panel-heading\">\n    <div>\n      <h2>Analysis Summary</h2>\n      <p>Quick context for the current range before diving into the detailed views.</p>\n    </div>\n    <p id=\"status-text\">Ready to analyze.</p>\n  </div>\n  <div id=\"summary-cards\" class=\"summary-cards\"></div>\n</section>\n\n<section class=\"panel analysis-panel\">\n  <div class=\"panel-heading\">\n    <div>\n      <h2>Analysis Views</h2>\n      <p>Switch between modular structure, gaps, factors, density, and expected counts.</p>\n    </div>\n  </div>\n  <div class=\"tab-row\" id=\"tab-row\">\n    <button class=\"tab-button active\" data-tab=\"modular\">Modular</button>\n    <button class=\"tab-button\" data-tab=\"gaps\">Gaps</button>\n    <button class=\"tab-button\" data-tab=\"factors\">Factors</button>\n    <button class=\"tab-button\" data-tab=\"density\">Density</button>\n    <button class=\"tab-button\" data-tab=\"expected\">Expected</button>\n  </div>\n  <div id=\"tab-content\" class=\"scroll-region\"></div>\n</section>""",
    script_name="analysis.js",
)

THEORY_PAGE = PageDefinition(
    route="/theory",
    title="Dual Prime Explorer | Theory",
    nav_label="Theory",
    active_route="theory",
    hero_html="""<section class=\"hero-block theory-hero\">\n  <div class=\"hero-copy theory-copy\">\n    <p class=\"eyebrow\">Theory</p>\n    <h1>The mathematical context behind twin-prime exploration.</h1>\n    <p class=\"hero-text\">Use this page as the conceptual companion to the explorer. It focuses on the problem statement, the main research ideas, what modern breakthroughs actually proved, and why a proof remains difficult.</p>\n  </div>\n</section>""",
    main_html="""<section class=\"panel theory-panel\">\n  <div class=\"panel-heading theory-heading\">\n    <div>\n      <h2>Theory</h2>\n      <p>A concise guide to the twin prime problem, organized as product-style reference notes rather than a long article.</p>\n    </div>\n  </div>\n  <div class=\"theory-layout\">\n    <div class=\"theory-tabs-shell\">\n      <div class=\"theory-tabs\" role=\"tablist\" aria-label=\"Theory topics\" id=\"theory-tablist\"></div>\n    </div>\n    <div class=\"theory-content-shell\">\n      <div id=\"theory-tabpanel\" class=\"theory-tabpanel\" role=\"tabpanel\" tabindex=\"0\"></div>\n    </div>\n  </div>\n</section>""",
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

PAGE_DEFINITIONS = [EXPLORER_PAGE, ANALYSIS_PAGE, THEORY_PAGE, EXPERIMENTS_PAGE]
PAGE_BY_ROUTE = {page.route: page for page in PAGE_DEFINITIONS}
PAGE_BY_ACTIVE_ROUTE = {page.active_route: page for page in PAGE_DEFINITIONS}
