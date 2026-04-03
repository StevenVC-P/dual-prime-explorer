"""Shared web assets and page rendering helpers."""

from __future__ import annotations

import hashlib
import html
import json

from .web_content import THEORY_TABS
from .web_pages import PAGE_DEFINITIONS, PageDefinition

APP_CSS = """:root {
  --bg: #f4f1eb;
  --panel: #fffdf9;
  --panel-soft: #f8f5ee;
  --panel-subtle: #fbf8f2;
  --panel-strong: #f2ece1;
  --ink: #181512;
  --muted: #60574f;
  --accent: #14532d;
  --accent-soft: #ecf6ee;
  --accent-faint: rgba(20, 83, 45, 0.08);
  --line: rgba(24, 21, 18, 0.12);
  --line-strong: rgba(24, 21, 18, 0.2);
  --shadow: 0 10px 30px rgba(24, 21, 18, 0.08);
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  color: var(--ink);
  background: linear-gradient(180deg, #f7f4ee 0%, #f1ede6 100%);
  font-family: Georgia, "Times New Roman", serif;
}
a { color: inherit; }
.page-shell { max-width: 1240px; margin: 0 auto; padding: 20px 18px 40px; }
.site-header { display: flex; align-items: center; justify-content: space-between; gap: 18px; padding: 14px 0 22px; }
.brand-mark { display: inline-flex; flex-direction: column; gap: 3px; text-decoration: none; }
.brand-kicker { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.16em; color: var(--accent); }
.brand-title { font-size: 1rem; color: var(--muted); }
.top-nav { display: flex; flex-wrap: wrap; gap: 10px; }
.nav-link { text-decoration: none; padding: 10px 14px; border-radius: 999px; border: 1px solid var(--line); background: rgba(255, 255, 255, 0.72); color: var(--muted); transition: border-color 120ms ease, color 120ms ease, background 120ms ease; }
.nav-link:hover, .nav-link:focus-visible { outline: none; border-color: var(--line-strong); color: var(--ink); }
.nav-link.active { background: var(--accent); color: white; border-color: var(--accent); }
.inline-link { color: var(--accent); font-weight: 600; text-decoration: none; }
.inline-link:hover, .inline-link:focus-visible { text-decoration: underline; outline: none; }
.hero-block, .panel, .control-panel { background: var(--panel); border: 1px solid var(--line); box-shadow: var(--shadow); }
.hero-grid { display: grid; grid-template-columns: minmax(0, 1.6fr) minmax(280px, 0.82fr); gap: 18px; }
.hero-block { border-radius: 24px; padding: 22px; margin-bottom: 22px; }
.hero-copy { max-width: 68ch; }
.theory-copy { max-width: 76ch; }
.eyebrow { margin: 0 0 10px; text-transform: uppercase; letter-spacing: 0.16em; font-size: 0.76rem; color: var(--accent); }
h1, h2, h3, h4 { margin: 0; font-weight: 600; }
h1 { font-size: clamp(2.2rem, 5vw, 4rem); line-height: 1.02; letter-spacing: -0.02em; }
h2 { font-size: clamp(1.35rem, 2vw, 1.85rem); }
h3 { font-size: 1rem; }
p { margin: 0; line-height: 1.65; }
.hero-text, .panel-heading p, .metric-box p, .theory-intro, .theory-section p, .theory-approach p, #status-text, .filter-panel-header p, #table-filter-status, .stat-note, .section-copy { color: var(--muted); }
.control-panel { border-radius: 20px; padding: 20px; display: grid; align-content: start; gap: 14px; }
.control-panel label, .filter-control { display: grid; gap: 8px; font-size: 0.95rem; }
.control-panel input, .filter-control input, .filter-control select {
  width: 100%;
  min-height: 46px;
  border: 1px solid var(--line);
  border-radius: 12px;
  padding: 11px 13px;
  font: inherit;
  background: white;
  color: var(--ink);
  transition: border-color 120ms ease, box-shadow 120ms ease, background 120ms ease;
}
.control-panel input:focus-visible,
.filter-control input:focus-visible,
.filter-control select:focus-visible {
  outline: none;
  border-color: rgba(20, 83, 45, 0.35);
  box-shadow: 0 0 0 3px rgba(20, 83, 45, 0.12);
}
.control-panel input:hover,
.filter-control input:hover,
.filter-control select:hover {
  border-color: var(--line-strong);
}
.control-panel button, .tab-button, .theory-tab { font: inherit; }
.control-panel button {
  border: none;
  border-radius: 999px;
  padding: 12px 18px;
  background: var(--accent);
  color: white;
  cursor: pointer;
}
.control-panel button:hover, .control-panel button:focus-visible { outline: none; background: #0f3f22; }
.content-stack { display: grid; gap: 20px; }
.panel { border-radius: 24px; padding: 22px; }
.panel-heading { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 10px; align-items: end; margin-bottom: 16px; }
.summary-cards, .metric-grid, .analysis-stat-grid, .comparison-grid, .histogram-grid { display: grid; gap: 12px; }
.summary-cards { grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); }
.summary-card, .metric-box, .theory-section, .theory-approach, .analysis-card, .histogram-card, .table-card { border: 1px solid var(--line); border-radius: 18px; background: var(--panel-soft); }
.summary-card { padding: 16px; }
.summary-card .label, .stat-label { display: block; margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.78rem; color: var(--muted); }
.summary-card .value, .stat-value { font-size: 1.7rem; }
.filter-panel {
  border: 1px solid var(--line);
  border-radius: 20px;
  background: var(--panel-subtle);
  padding: 18px;
  margin-bottom: 16px;
}
.filter-panel-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  gap: 16px;
  margin-bottom: 16px;
}
.filter-layout {
  display: grid;
  grid-template-columns: repeat(2, minmax(280px, 1fr));
  gap: 14px;
  align-items: start;
}
.filter-column { display: grid; gap: 14px; align-content: start; }
.filter-group {
  margin: 0;
  padding: 14px;
  border: 1px solid var(--line);
  border-radius: 16px;
  background: rgba(255, 255, 255, 0.72);
  min-width: 0;
}
.filter-group legend {
  padding: 0 6px;
  font-size: 0.82rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--muted);
}
.filter-group-grid { display: grid; gap: 12px; }
.filter-group-grid-wide { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.filter-control span { font-size: 0.85rem; color: var(--muted); }
.checkbox-group { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 8px; }
.checkbox-pill { display: flex; align-items: center; gap: 8px; min-height: 38px; padding: 8px 11px; border: 1px solid var(--line); border-radius: 10px; background: white; color: var(--ink); cursor: pointer; transition: border-color 120ms ease, box-shadow 120ms ease, background 120ms ease; }
.checkbox-pill:hover { border-color: var(--line-strong); }
.checkbox-pill:focus-within { border-color: rgba(20, 83, 45, 0.35); box-shadow: 0 0 0 3px rgba(20, 83, 45, 0.12); }
.checkbox-pill input { width: 14px; height: 14px; margin: 0; accent-color: var(--accent); }
.checkbox-pill span { color: var(--ink); font-size: 0.9rem; line-height: 1.3; }
.filter-range-row { display: grid; grid-template-columns: minmax(0, 1fr) auto minmax(0, 1fr); gap: 10px; align-items: end; }
.filter-range-arrow { align-self: center; padding-bottom: 12px; color: var(--muted); font-size: 1rem; }
.filter-reset-button {
  align-self: start;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: transparent;
  color: var(--ink);
  padding: 10px 14px;
  cursor: pointer;
  transition: border-color 120ms ease, background 120ms ease, color 120ms ease;
}
.filter-reset-button:hover,
.filter-reset-button:focus-visible {
  outline: none;
  border-color: var(--line-strong);
  background: rgba(24, 21, 18, 0.03);
}
.column-panel {
  display: grid;
  gap: 12px;
  margin-bottom: 16px;
  padding: 14px 16px;
  border: 1px solid var(--line);
  border-radius: 18px;
  background: rgba(255, 255, 255, 0.64);
}
.column-panel-header p { color: var(--muted); }
.column-toggle-row {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  align-items: center;
}
.column-toggle-row .checkbox-pill {
  min-height: 34px;
  padding: 7px 10px;
}
.tab-row { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 16px; }
.tab-button { border: 1px solid var(--line); background: transparent; color: var(--muted); border-radius: 999px; padding: 10px 14px; cursor: pointer; }
.tab-button.active { background: var(--accent); border-color: var(--accent); color: white; }
.scroll-region { overflow: auto; }
.data-table { width: 100%; border-collapse: collapse; font-size: 0.95rem; min-width: 680px; }
.data-table th, .data-table td { text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--line); vertical-align: top; }
.data-table th { position: sticky; top: 0; background: #f5f1e8; z-index: 1; }
.data-table tr:nth-child(even) td { background: rgba(20, 83, 45, 0.03); }
.table-card, .code-card { padding: 0; overflow: hidden; }
.table-card-header, .histogram-header { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 10px; align-items: end; padding: 16px 16px 0; }
.table-card .scroll-region { padding: 0 0 4px; }
.code-block { padding: 14px; border-radius: 16px; border: 1px solid var(--line); background: #fcfaf6; font-family: Consolas, "Courier New", monospace; white-space: pre-wrap; font-size: 0.9rem; }
.metric-grid { grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.metric-box, .analysis-card, .histogram-card { padding: 16px; }
.metric-box h3, .theory-section h3, .theory-approach h3, .analysis-card h3, .histogram-card h3 { margin-bottom: 8px; }
.analysis-layout, .section-stack { display: grid; gap: 16px; }
.analysis-stat-grid { grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); }
.analysis-card { background: linear-gradient(180deg, rgba(255,255,255,0.92) 0%, rgba(248,245,238,0.92) 100%); }
.analysis-card.accent-card { background: linear-gradient(180deg, rgba(236,246,238,0.95) 0%, rgba(248,245,238,0.95) 100%); border-color: rgba(20, 83, 45, 0.18); }
.stat-note { font-size: 0.92rem; }
.comparison-grid { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.histogram-grid { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.histogram-list { display: grid; gap: 10px; }
.histogram-row { display: grid; grid-template-columns: 72px minmax(0, 1fr) 58px; gap: 10px; align-items: center; }
.histogram-key, .histogram-value { font-variant-numeric: tabular-nums; color: var(--muted); }
.histogram-track { height: 10px; border-radius: 999px; background: rgba(24, 21, 18, 0.08); overflow: hidden; }
.histogram-fill { height: 100%; border-radius: 999px; background: linear-gradient(90deg, #14532d 0%, #2f7a4a 100%); }
.insight-strip { display: flex; flex-wrap: wrap; gap: 10px; }
.insight-pill { padding: 9px 12px; border-radius: 999px; background: var(--accent-faint); color: var(--accent); border: 1px solid rgba(20, 83, 45, 0.12); font-size: 0.92rem; }
.definition-list { display: grid; gap: 10px; margin: 0; }
.definition-row { display: grid; grid-template-columns: minmax(110px, 160px) minmax(0, 1fr); gap: 12px; align-items: start; padding: 10px 0; border-top: 1px solid rgba(24, 21, 18, 0.08); }
.definition-row:first-child { border-top: 0; padding-top: 0; }
.definition-term { color: var(--muted); font-size: 0.92rem; }
.definition-value { font-variant-numeric: tabular-nums; }
.empty-note { padding: 14px 16px; border-radius: 16px; background: var(--panel-subtle); border: 1px dashed var(--line); color: var(--muted); }
.error { color: #8a1c1c; border: 1px solid rgba(138, 28, 28, 0.18); background: rgba(249, 115, 115, 0.08); padding: 14px; border-radius: 16px; }
.theory-layout { display: grid; grid-template-columns: minmax(220px, 260px) minmax(0, 1fr); gap: 18px; }
.theory-tabs-shell { align-self: start; }
.theory-tabs { display: grid; gap: 10px; }
.theory-tab { text-align: left; border: 1px solid var(--line); border-radius: 16px; padding: 14px 16px; background: transparent; color: var(--muted); cursor: pointer; }
.theory-tab:hover, .theory-tab:focus-visible { outline: none; border-color: var(--line-strong); color: var(--ink); }
.theory-tab.active { background: var(--accent-soft); border-color: rgba(20, 83, 45, 0.24); color: var(--ink); }
.theory-tab.active .theory-tab-label { color: var(--accent); }
.theory-tab-label { display: block; font-weight: 600; margin-bottom: 4px; }
.theory-tab-hint { display: block; font-size: 0.92rem; }
.theory-content-shell { min-width: 0; }
.theory-tabpanel { display: grid; gap: 16px; outline: none; }
.theory-intro-block { display: grid; gap: 8px; padding-bottom: 4px; }
.theory-intro { max-width: 70ch; }
.theory-sections, .theory-approaches, .theory-timeline, .theory-faq-grid, .theory-reference-list { display: grid; gap: 14px; }
.theory-section, .theory-approach, .theory-timeline-card, .theory-faq-card, .theory-reference-card { padding: 18px; }
.theory-approach dl { display: grid; gap: 8px; margin: 0; }
.theory-approach dt { font-weight: 600; }
.theory-approach dd { margin: 0; color: var(--muted); }
.theory-meta-strip { display: flex; flex-wrap: wrap; gap: 10px; }
.theory-meta-pill { padding: 8px 12px; border-radius: 999px; background: var(--accent-faint); color: var(--accent); border: 1px solid rgba(20, 83, 45, 0.12); font-size: 0.9rem; }
.theory-block { display: grid; gap: 12px; }
.theory-block h3 { font-size: 1.02rem; }
.theory-timeline-card { border: 1px solid var(--line); border-radius: 18px; background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(248,245,238,0.92) 100%); }
.theory-timeline-label { display: inline-block; margin-bottom: 8px; font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); }
.theory-faq-grid { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.theory-faq-card h4, .theory-reference-card h4 { margin: 0 0 8px; font-size: 0.98rem; }
.theory-reference-note, .theory-faq-card p, .theory-timeline-card p { color: var(--muted); }
.theory-reference-list { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
@media (max-width: 1024px) {
  .filter-layout { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .filter-group-grid-wide { grid-template-columns: 1fr; }
}
@media (max-width: 900px) {
  .site-header, .hero-grid, .theory-layout { grid-template-columns: 1fr; display: grid; }
  .site-header { gap: 14px; }
  .top-nav { justify-content: flex-start; }
  .definition-row { grid-template-columns: 1fr; gap: 4px; }
}
@media (max-width: 700px) {
  .filter-layout { grid-template-columns: 1fr; }
  .filter-column { gap: 12px; }
  .filter-panel-header { flex-direction: column; align-items: stretch; }
  .column-toggle-row { display: grid; grid-template-columns: 1fr; }
  .filter-range-row { grid-template-columns: 1fr; }
  .filter-range-arrow { display: none; }
  .histogram-row { grid-template-columns: 60px minmax(0, 1fr) 42px; }
}
@media (max-width: 640px) {
  .page-shell { padding: 14px 12px 30px; }
  .hero-block, .panel, .control-panel { padding: 18px; }
  h1 { line-height: 1.06; }
  .top-nav { gap: 8px; }
  .nav-link, .tab-button, .theory-tab, .filter-reset-button { width: 100%; justify-content: flex-start; }
}
"""

COMMON_ANALYSIS_JS = """const state = {
  activeTab: 'modular',
  analysis: null,
};

const form = document.getElementById('analysis-form');
const statusText = document.getElementById('status-text');
const summaryCards = document.getElementById('summary-cards');
const tabContent = document.getElementById('tab-content');
const tabButtons = Array.from(document.querySelectorAll('.tab-button'));

function formatValue(value, digits = 6) {
  if (typeof value === 'number') {
    return Number.isInteger(value) ? String(value) : value.toFixed(digits);
  }
  if (Array.isArray(value)) {
    return value.join(', ');
  }
  if (value && typeof value === 'object') {
    return JSON.stringify(value);
  }
  return String(value);
}

function formatPercent(value) {
  return `${(value * 100).toFixed(2)}%`;
}

function formatBool(value) {
  return value ? 'Yes' : 'No';
}

function makeTable(columns, rows) {
  const head = `<thead><tr>${columns.map((column) => `<th>${column.label}</th>`).join('')}</tr></thead>`;
  const bodyRows = rows.map((row) => `<tr>${columns.map((column) => `<td>${column.render(row)}</td>`).join('')}</tr>`).join('');
  return `<table class=\"data-table\">${head}<tbody>${bodyRows}</tbody></table>`;
}

function makeStatCards(items, accentIndex = 0) {
  return `<div class=\"analysis-stat-grid\">${items.map((item, index) => `
    <article class=\"analysis-card${index === accentIndex ? ' accent-card' : ''}\">
      <span class=\"stat-label\">${item.label}</span>
      <div class=\"stat-value\">${item.value}</div>
      ${item.note ? `<p class=\"stat-note\">${item.note}</p>` : ''}
    </article>
  `).join('')}</div>`;
}

function makeDefinitionList(items) {
  return `<div class=\"definition-list\">${items.map((item) => `
    <div class=\"definition-row\">
      <div class=\"definition-term\">${item.term}</div>
      <div class=\"definition-value\">${item.value}</div>
    </div>
  `).join('')}</div>`;
}

function makeHistogramCard(title, subtitle, histogram, formatter = (key) => key) {
  const entries = Object.entries(histogram || {}).sort((left, right) => Number(left[0]) - Number(right[0]));
  if (!entries.length) {
    return `<article class=\"histogram-card\"><div class=\"histogram-header\"><div><h3>${title}</h3><p class=\"section-copy\">${subtitle}</p></div></div><div class=\"empty-note\">No values available in this range.</div></article>`;
  }
  const maxValue = Math.max(...entries.map((entry) => Number(entry[1])));
  return `
    <article class=\"histogram-card\">
      <div class=\"histogram-header\">
        <div>
          <h3>${title}</h3>
          <p class=\"section-copy\">${subtitle}</p>
        </div>
      </div>
      <div class=\"histogram-list\">
        ${entries.map(([key, value]) => `
          <div class=\"histogram-row\">
            <span class=\"histogram-key\">${formatter(key)}</span>
            <div class=\"histogram-track\"><div class=\"histogram-fill\" style=\"width:${(Number(value) / maxValue) * 100}%\"></div></div>
            <span class=\"histogram-value\">${value}</span>
          </div>
        `).join('')}
      </div>
    </article>
  `;
}

function makeTableCard(title, subtitle, tableHtml) {
  return `
    <section class=\"table-card\">
      <div class=\"table-card-header\">
        <div>
          <h3>${title}</h3>
          <p class=\"section-copy\">${subtitle}</p>
        </div>
      </div>
      <div class=\"scroll-region\">${tableHtml}</div>
    </section>
  `;
}

function formatNumberType(row) {
  const labels = {
    unit: 'Unit',
    prime: 'Prime',
    composite: 'Composite',
  };
  return labels[row.number_type] || row.number_type;
}

function formatPrimeRole(row) {
  const labels = {
    prime_in_twin_pair: 'Twin Prime',
    prime_not_in_twin_pair: 'Single Prime',
    not_prime: 'Not Prime',
  };
  return labels[row.prime_role] || row.prime_role;
}

function formatStructuralRegion(row) {
  const labels = {
    bootstrap: 'Bootstrap',
    standard: 'Standard',
  };
  return labels[row.structural_region] || row.structural_region;
}

function getNeighborhoodFilterValue(row) {
  if (row.number_type === 'prime') {
    return row.is_edge_case ? 'prime_edge_case' : 'prime';
  }
  if (row.adjacent_prime_role === 'between_two_primes') {
    return 'twin_center';
  }
  return row.adjacent_prime_role;
}

function formatAdjacentPrimeRole(row) {
  const labels = {
    twin_center: 'Twin Center',
    next_to_one_prime: 'Next to one prime',
    not_next_to_primes: 'No adjacent primes',
    prime_edge_case: 'Prime edge case',
    prime: 'Prime',
  };
  return labels[getNeighborhoodFilterValue(row)] || getNeighborhoodFilterValue(row);
}

function formatDivisibility(row) {
  if (row.number_type === 'prime') {
    return 'Prime';
  }
  if (row.number_type === 'unit') {
    return 'Unit';
  }
  if (!row.prime_divisors || !row.prime_divisors.length) {
    return 'No prime divisors recorded';
  }
  return row.prime_divisors.join(', ');
}

function formatAllDivisors(row) {
  if (!row.all_divisors || !row.all_divisors.length) {
    return '';
  }
  return `${row.all_divisors.join(', ')} (${row.all_divisors.length})`;
}

function renderSummary(analysis) {
  if (!summaryCards) {
    return;
  }
  const cards = [
    ['Range', `${analysis.start} - ${analysis.limit}`],
    ['Range Size', analysis.limit - analysis.start + 1],
    ['Prime Count', analysis.primes.length],
    ['Twin Pairs', analysis.twin_pairs.length],
    ['Unpaired Primes', analysis.unpaired_primes.length],
  ];
  summaryCards.innerHTML = cards.map(([label, value]) => `
    <article class="summary-card">
      <span class="label">${label}</span>
      <span class="value">${formatValue(value)}</span>
    </article>
  `).join('');
}
function renderModular(analysis) {
  const centerMod6Zero = Number(analysis.center_mod6_counts['0'] ?? analysis.center_mod6_counts[0] ?? 0);
  const centerMod6Four = Number(analysis.center_mod6_counts['4'] ?? analysis.center_mod6_counts[4] ?? 0);
  const structuresAfterFirst = analysis.pair_structures.filter((row) => row.pair[0] > 5);
  const sixKPatternCount = structuresAfterFirst.filter((row) => row.pair_mod6[0] === 5 && row.pair_mod6[1] === 1).length;
  const structureTable = makeTable(
    [
      { label: 'Pair', render: (row) => row.pair.join(' - ') },
      { label: 'Center', render: (row) => row.center },
      { label: 'Center mod 6', render: (row) => row.center_mod6 },
      { label: 'Center mod 30', render: (row) => row.center_mod30 },
      { label: 'Pair residues mod 6', render: (row) => row.pair_mod6.join(', ') },
      { label: 'Pair residues mod 30', render: (row) => row.pair_mod30.join(', ') },
    ],
    analysis.pair_structures,
  );

  return `
    <div class=\"analysis-layout\">
      ${makeStatCards([
        { label: 'Pairs After (3, 5)', value: formatValue(structuresAfterFirst.length), note: 'Twin-prime pairs large enough to test the 6k +/- 1 structure.' },
        { label: '6k +/- 1 Matches', value: formatValue(sixKPatternCount), note: 'Pairs whose residues are (5, 1) modulo 6.' },
        { label: 'Centers mod 6 = 0', value: formatValue(centerMod6Zero), note: 'Expected dominant center residue after the first pair.' },
        { label: 'Centers mod 6 = 4', value: formatValue(centerMod6Four), note: 'Captures the exceptional center for (3, 5).' },
      ])}
      <div class=\"histogram-grid\">
        ${makeHistogramCard('Center residues mod 6', 'How often twin-prime centers land in each residue class.', analysis.center_mod6_counts, (key) => `mod ${key}`)}
        ${makeHistogramCard('Center residues mod 30', 'A finer modular view of the center positions.', analysis.center_mod30_counts, (key) => `mod ${key}`)}
      </div>
      ${makeTableCard('Pair structure table', 'Every twin-prime pair with its center and residue data.', structureTable)}
    </div>
  `;
}

function renderGaps(analysis) {
  const gapData = analysis.gap_analysis;
  const pairGaps = gapData.pair_start_gaps;
  const centerGaps = gapData.center_gaps;
  const averagePairGap = pairGaps.length ? pairGaps.reduce((sum, gap) => sum + gap, 0) / pairGaps.length : 0;
  const averageCenterGap = centerGaps.length ? centerGaps.reduce((sum, gap) => sum + gap, 0) / centerGaps.length : 0;

  return `
    <div class=\"analysis-layout\">
      ${makeStatCards([
        { label: 'Pair Start Gaps', value: formatValue(pairGaps.length), note: 'Consecutive gaps between the first elements of twin pairs.' },
        { label: 'Average Pair Gap', value: formatValue(averagePairGap), note: 'Mean separation between pair starts.' },
        { label: 'Center Gaps', value: formatValue(centerGaps.length), note: 'Consecutive gaps between twin-prime centers.' },
        { label: 'Average Center Gap', value: formatValue(averageCenterGap), note: 'Mean separation between centers.' },
      ])}
      <div class=\"histogram-grid\">
        ${makeHistogramCard('Pair-start gap histogram', 'Frequency of each observed gap between pair starts.', gapData.pair_start_gap_histogram)}
        ${makeHistogramCard('Center gap histogram', 'Frequency of each observed gap between centers.', gapData.center_gap_histogram)}
      </div>
      <div class=\"comparison-grid\">
        <article class=\"analysis-card\">
          <h3>Observed pair-start gaps</h3>
          <p class=\"section-copy\">Raw sequence for close inspection and manual pattern spotting.</p>
          <div class=\"code-block\">${JSON.stringify(pairGaps)}</div>
        </article>
        <article class=\"analysis-card\">
          <h3>Observed center gaps</h3>
          <p class=\"section-copy\">Centers mirror the pair-start pattern in early ranges.</p>
          <div class=\"code-block\">${JSON.stringify(centerGaps)}</div>
        </article>
      </div>
    </div>
  `;
}

function renderFactors(analysis) {
  const center = analysis.factorization_analysis.center_aggregate;
  const other = analysis.factorization_analysis.non_center_even_aggregate;
  const centerTable = makeTable(
    [
      { label: 'Center', render: (row) => row.number },
      { label: 'Factorization', render: (row) => JSON.stringify(row.factorization) },
      { label: 'Divisors', render: (row) => row.divisor_count },
      { label: 'Largest prime factor', render: (row) => row.largest_prime_factor },
      { label: 'Squarefree', render: (row) => formatBool(row.is_squarefree) },
    ],
    analysis.factorization_analysis.center_records,
  );

  return `
    <div class=\"analysis-layout\">
      <div class=\"comparison-grid\">
        <article class=\"analysis-card accent-card\">
          <h3>Twin-prime centers</h3>
          ${makeDefinitionList([
            { term: 'Sample size', value: formatValue(center.numbers.length) },
            { term: 'Average divisor count', value: formatValue(center.average_divisor_count) },
            { term: 'Squarefree frequency', value: formatPercent(center.squarefree_frequency) },
            { term: 'Average largest prime factor', value: formatValue(center.average_largest_prime_factor) },
          ])}
        </article>
        <article class=\"analysis-card\">
          <h3>Other even numbers</h3>
          ${makeDefinitionList([
            { term: 'Sample size', value: formatValue(other.numbers.length) },
            { term: 'Average divisor count', value: formatValue(other.average_divisor_count) },
            { term: 'Squarefree frequency', value: formatPercent(other.squarefree_frequency) },
            { term: 'Average largest prime factor', value: formatValue(other.average_largest_prime_factor) },
          ])}
        </article>
      </div>
      <div class=\"histogram-grid\">
        ${makeHistogramCard('Center divisor-count distribution', 'How many divisors twin-prime centers tend to have.', center.divisor_count_histogram)}
        ${makeHistogramCard('Non-center even divisor-count distribution', 'A baseline comparison across even numbers that are not centers.', other.divisor_count_histogram)}
      </div>
      ${makeTableCard('Center factorizations', 'Prime factors and squarefree status for each center in the current range.', centerTable)}
    </div>
  `;
}

function renderDensity(analysis) {
  const density = analysis.density_analysis;
  const densityTable = makeTable(
    [
      { label: 'Pair', render: (row) => row.pair.join(' - ') },
      { label: 'Window', render: (row) => `${row.window_start} - ${row.window_end}` },
      { label: 'Primes in window', render: (row) => row.primes_in_window },
      { label: 'Twin pairs in window', render: (row) => row.twin_pairs_in_window },
      { label: 'Local prime density', render: (row) => formatValue(row.local_prime_density) },
      { label: 'Density ratio', render: (row) => formatValue(row.prime_density_ratio) },
    ],
    density.pair_density_stats,
  );

  return `
    <div class=\"analysis-layout\">
      ${makeStatCards([
        { label: 'Global prime density', value: formatValue(density.global_prime_density), note: 'Prime count divided by the overall range size.' },
        { label: 'Average local prime density', value: formatValue(density.average_local_prime_density), note: 'Average density across all pair-centered windows.' },
        { label: 'Average local twin density', value: formatValue(density.average_local_twin_pair_density), note: 'Twin-pair concentration inside local windows.' },
        { label: 'Average density ratio', value: formatValue(density.average_prime_density_ratio), note: 'Local prime density divided by the global baseline.' },
      ])}
      <div class=\"insight-strip\">
        <span class=\"insight-pill\">Window radius: +/-${density.window_radius}</span>
        <span class=\"insight-pill\">Evaluated pairs: ${density.pair_density_stats.length}</span>
      </div>
      ${makeTableCard('Local density windows', 'Per-pair window statistics for comparing local clustering against the global baseline.', densityTable)}
    </div>
  `;
}

function renderExpected(analysis) {
  const expectedRows = analysis.expected_vs_observed;
  const lastRow = expectedRows[expectedRows.length - 1];
  const expectedTable = makeTable(
    [
      { label: 'Limit', render: (row) => row.limit },
      { label: 'Actual count', render: (row) => row.actual_count },
      { label: 'Expected count', render: (row) => formatValue(row.expected_count) },
      { label: 'Actual / expected', render: (row) => row.ratio === null ? '' : formatValue(row.ratio) },
    ],
    expectedRows,
  );

  return `
    <div class=\"analysis-layout\">
      ${makeStatCards([
        { label: 'Checkpoints', value: formatValue(expectedRows.length), note: 'Sample points included in the heuristic comparison.' },
        { label: 'Final actual count', value: formatValue(lastRow ? lastRow.actual_count : 0), note: 'Twin-prime pairs observed at the largest checkpoint.' },
        { label: 'Final expected count', value: formatValue(lastRow ? lastRow.expected_count : 0), note: 'Using N / (log N)^2 as the heuristic baseline.' },
        { label: 'Final ratio', value: lastRow && lastRow.ratio !== null ? formatValue(lastRow.ratio) : 'N/A', note: 'How observed counts compare to the heuristic at the endpoint.' },
      ])}
      ${makeTableCard('Expected vs observed', 'A checkpoint table for comparing empirical twin-prime counts to the heuristic estimate.', expectedTable)}
    </div>
  `;
}

function renderAnalysisTabs() {
  if (!tabContent) {
    return;
  }
  if (!state.analysis) {
    tabContent.innerHTML = '<p>Run an analysis to populate this view.</p>';
    return;
  }
  const renderers = { modular: renderModular, gaps: renderGaps, factors: renderFactors, density: renderDensity, expected: renderExpected };
  tabContent.innerHTML = renderers[state.activeTab](state.analysis);
  tabButtons.forEach((button) => {
    button.classList.toggle('active', button.dataset.tab === state.activeTab);
  });
}

async function fetchAnalysis(start, end, onSuccess) {
  statusText.textContent = 'Analyzing...';
  try {
    const response = await fetch(`/api/analyze?start=${encodeURIComponent(start)}&end=${encodeURIComponent(end)}`);
    if (!response.ok) {
      const errorPayload = await response.json();
      throw new Error(errorPayload.error || 'Request failed.');
    }
    const analysis = await response.json();
    state.analysis = analysis;
    renderSummary(analysis);
    if (onSuccess) {
      onSuccess(analysis);
    }
    renderAnalysisTabs();
    statusText.textContent = `Computed ${analysis.twin_pairs.length} twin-prime pairs in ${analysis.start}-${analysis.limit}.`;
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Unknown error';
    statusText.textContent = 'Analysis failed.';
    if (tabContent) {
      tabContent.innerHTML = `<div class="error">${message}</div>`;
    }
  }
}
"""

EXPLORER_JS = COMMON_ANALYSIS_JS + """
const numberTable = document.getElementById('number-table');
const filterForm = document.getElementById('table-filter-form');
const filterRole = document.getElementById('filter-role');
const filterNeighborhood = document.getElementById('filter-neighborhood');
const filterNeighborhoodOptions = filterNeighborhood ? Array.from(filterNeighborhood.querySelectorAll('input[type="checkbox"]')) : [];
const filterColumns = document.getElementById('filter-columns');
const filterColumnOptions = filterColumns ? Array.from(filterColumns.querySelectorAll('input[type="checkbox"]')) : [];
const filterDivisors = document.getElementById('filter-divisors');
const filterDivisorLogic = document.getElementById('filter-divisor-logic');
const filterMin = document.getElementById('filter-min');
const filterMax = document.getElementById('filter-max');
const filterReset = document.getElementById('filter-reset');
const filterStatus = document.getElementById('table-filter-status');
function parseDivisorFilterValues() {
  if (!filterDivisors || !filterDivisors.value.trim()) {
    return [];
  }
  const values = filterDivisors.value
    .split(/[\\s,]+/)
    .map((value) => Number(value.trim()))
    .filter((value) => Number.isInteger(value) && value > 0);
  return [...new Set(values)];
}

function getFilteredRows(rows) {
  const divisorValues = parseDivisorFilterValues();
  const divisorLogic = filterDivisorLogic?.value || 'or';
  const minValue = filterMin?.value ? Number(filterMin.value) : null;
  const maxValue = filterMax?.value ? Number(filterMax.value) : null;

  return rows.filter((row) => {
    if (filterRole && filterRole.value !== 'all') {
      if (row.prime_role !== filterRole.value) {
        return false;
      }
    }
    const selectedNeighborhoods = filterNeighborhoodOptions.filter((option) => option.checked).map((option) => option.value);
    if (selectedNeighborhoods.length && !selectedNeighborhoods.includes(getNeighborhoodFilterValue(row))) {
      return false;
    }
    if (divisorValues.length) {
      const rowDivisors = row.all_divisors || [];
      const matches = divisorLogic === 'and'
        ? divisorValues.every((value) => rowDivisors.includes(value))
        : divisorValues.some((value) => rowDivisors.includes(value));
      if (!matches) {
        return false;
      }
    }
    if (minValue !== null && row.number < minValue) {
      return false;
    }
    if (maxValue !== null && row.number > maxValue) {
      return false;
    }
    return true;
  });
}


function getVisibleNumberTableColumns() {
  const selectedColumns = filterColumnOptions.filter((option) => option.checked).map((option) => option.value);
  const columnDefinitions = [
    { key: 'number_type', label: 'Number type', render: (row) => formatNumberType(row) },
    { key: 'prime_role', label: 'Prime role', render: (row) => formatPrimeRole(row) },
    { key: 'prime_neighborhood', label: 'Prime neighborhood', render: (row) => formatAdjacentPrimeRole(row) },
    { key: 'prime_divisors', label: 'Prime divisors', render: (row) => formatDivisibility(row) },
    { key: 'all_divisors', label: 'All divisors', render: (row) => formatAllDivisors(row) },
  ];
  return [
    { label: 'Number', render: (row) => row.number },
    ...columnDefinitions.filter((column) => selectedColumns.includes(column.key)),
  ];
}

function renderNumberTable(analysis) {
  if (!numberTable) {
    return;
  }
  const filteredRows = getFilteredRows(analysis.number_classifications);
  numberTable.innerHTML = makeTableCard(
    'Number classification table',
    `Each row tracks primality, twin-pair membership, and whether the number is the center of a pair. Analyzed range: ${analysis.start}-${analysis.limit} before table filters.`,
    makeTable(
      getVisibleNumberTableColumns(),
      filteredRows,
    ),
  );
  if (filterStatus) {
    filterStatus.textContent = filteredRows.length === analysis.number_classifications.length ? `Showing all ${analysis.number_classifications.length} rows.` : `Showing ${filteredRows.length} of ${analysis.number_classifications.length} rows.`;
  }
}

function rerenderExplorerTable() {
  if (state.analysis) {
    renderNumberTable(state.analysis);
  }
}

if (form && statusText) {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetchAnalysis(formData.get('start'), formData.get('end'), renderNumberTable);
  });

  [filterRole, filterDivisors, filterDivisorLogic, filterMin, filterMax, ...filterNeighborhoodOptions, ...filterColumnOptions].forEach((control) => {
    control?.addEventListener('input', rerenderExplorerTable);
    control?.addEventListener('change', rerenderExplorerTable);
  });

  filterReset?.addEventListener('click', () => {
    if (filterForm) {
      filterForm.reset();
    }
    filterNeighborhoodOptions.forEach((option) => {
      option.checked = false;
    });
    rerenderExplorerTable();
  });

  fetchAnalysis(1, 100, renderNumberTable);
}
"""

ANALYSIS_JS = COMMON_ANALYSIS_JS + """
if (form && statusText) {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    fetchAnalysis(formData.get('start'), formData.get('end'));
  });

  tabButtons.forEach((button) => {
    button.addEventListener('click', () => {
      state.activeTab = button.dataset.tab;
      renderAnalysisTabs();
    });
  });

  fetchAnalysis(1, 100);
}
"""


def _render_theory_tab_buttons_html(active_tab_id: str) -> str:
    buttons = []
    for index, tab in enumerate(THEORY_TABS):
        is_active = tab["id"] == active_tab_id
        buttons.append(
            """<button
      id=\"theory-tab-{id}\"
      class=\"theory-tab{active}\"
      role=\"tab\"
      type=\"button\"
      aria-selected=\"{selected}\"
      aria-controls=\"theory-tabpanel\"
      tabindex=\"{tabindex}\"
      data-tab-id=\"{id}\"
      data-index=\"{index}\"
    >
      <span class=\"theory-tab-label\">{label}</span>
      <span class=\"theory-tab-hint\">{hint}</span>
    </button>""".format(
                id=html.escape(tab["id"]),
                active=" active" if is_active else "",
                selected="true" if is_active else "false",
                tabindex="0" if is_active else "-1",
                index=index,
                label=html.escape(tab["label"]),
                hint=html.escape(tab.get("nav_hint", tab["intro"])),
            )
        )
    return "".join(buttons)


def _render_theory_tab_panel_html(tab: dict[str, object]) -> str:
    intro = html.escape(str(tab["intro"]))
    label = html.escape(str(tab["label"]))
    updated = tab.get("updated")
    meta = (
        '<div class="theory-meta-strip"><span class="theory-meta-pill">{}</span></div>'.format(html.escape(str(updated)))
        if updated
        else ""
    )
    sections = "".join(
        '<article class="theory-section"><h3>{}</h3><p>{}</p></article>'.format(
            html.escape(section["title"]),
            html.escape(section["body"]),
        )
        for section in tab.get("sections", [])
    )
    cards = "".join(
        """<article class=\"theory-approach\">
      <h3>{title}</h3>
      <p>{summary}</p>
      <dl>
        <dt>What it is trying to do</dt>
        <dd>{trying}</dd>
        <dt>Why it helps</dt>
        <dd>{helps}</dd>
        <dt>Why it still falls short</dt>
        <dd>{falls_short}</dd>
      </dl>
    </article>""".format(
            title=html.escape(card["title"]),
            summary=html.escape(card["summary"]),
            trying=html.escape(card["trying"]),
            helps=html.escape(card["helps"]),
            falls_short=html.escape(card["falls_short"]),
        )
        for card in tab.get("cards", [])
    )
    timeline_items = tab.get("timeline", [])
    timeline = ""
    if timeline_items:
        timeline_rows = "".join(
            """<article class=\"theory-timeline-card\">
      <span class=\"theory-timeline-label\">{label}</span>
      <h4>{title}</h4>
      <p>{body}</p>
    </article>""".format(
                label=html.escape(item["label"]),
                title=html.escape(item["title"]),
                body=html.escape(item["body"]),
            )
            for item in timeline_items
        )
        timeline = '<section class="theory-block"><h3>Twin Prime History Timeline</h3><div class="theory-timeline">{}</div></section>'.format(timeline_rows)
    faq_items = tab.get("faq", [])
    faq = ""
    if faq_items:
        faq_rows = "".join(
            """<article class=\"theory-faq-card\">
      <h4>{question}</h4>
      <p>{answer}</p>
    </article>""".format(
                question=html.escape(item["question"]),
                answer=html.escape(item["answer"]),
            )
            for item in faq_items
        )
        faq = '<section class="theory-block"><h3>Twin Prime FAQ</h3><div class="theory-faq-grid">{}</div></section>'.format(faq_rows)
    reference_items = tab.get("references", [])
    references = ""
    if reference_items:
        reference_rows = "".join(
            """<article class=\"theory-reference-card\">
      <h4>{title}</h4>
      <p class=\"theory-reference-note\">{note}</p>
    </article>""".format(
                title=html.escape(item["title"]),
                note=html.escape(item["note"]),
            )
            for item in reference_items
        )
        references = '<section class="theory-block"><h3>Further Reading and References</h3><div class="theory-reference-list">{}</div></section>'.format(reference_rows)
    return (
        '<div class="theory-intro-block"><h2>{}</h2><p class="theory-intro">{}</p>{}</div>'.format(label, intro, meta)
        + ('<div class="theory-sections">{}</div>'.format(sections) if sections else '')
        + ('<div class="theory-approaches">{}</div>'.format(cards) if cards else '')
        + timeline
        + faq
        + references
    )


def _render_theory_main_html(main_html: str) -> str:
    active_tab = THEORY_TABS[0]
    main_html = main_html.replace(
        '<div class="theory-tabs" role="tablist" aria-label="Theory topics" id="theory-tablist"></div>',
        '<div class="theory-tabs" role="tablist" aria-label="Theory topics" id="theory-tablist">{}</div>'.format(_render_theory_tab_buttons_html(active_tab["id"])),
    )
    return main_html.replace(
        '<div id="theory-tabpanel" class="theory-tabpanel" role="tabpanel" tabindex="0"></div>',
        '<div id="theory-tabpanel" class="theory-tabpanel" role="tabpanel" tabindex="0" aria-labelledby="theory-tab-{id}">{content}</div>'.format(
            id=html.escape(active_tab["id"]),
            content=_render_theory_tab_panel_html(active_tab),
        ),
    )


def build_theory_js() -> str:
    return (
        "const theoryTabs = " + json.dumps(THEORY_TABS) + ";\n\n"
        + """const tabList = document.getElementById('theory-tablist');
const tabPanel = document.getElementById('theory-tabpanel');

function getInitialTheoryTabId() {
  const hash = window.location.hash.replace('#', '');
  if (theoryTabs.some((tab) => tab.id === hash)) {
    return hash;
  }
  return theoryTabs[0].id;
}

let activeTheoryTab = getInitialTheoryTabId();

function renderTheoryTabButtons() {
  tabList.innerHTML = theoryTabs.map((tab, index) => `
    <button
      id="theory-tab-${tab.id}"
      class="theory-tab${tab.id === activeTheoryTab ? ' active' : ''}"
      role="tab"
      type="button"
      aria-selected="${tab.id === activeTheoryTab ? 'true' : 'false'}"
      aria-controls="theory-tabpanel"
      tabindex="${tab.id === activeTheoryTab ? '0' : '-1'}"
      data-tab-id="${tab.id}"
      data-index="${index}"
    >
      <span class="theory-tab-label">${tab.label}</span>
      <span class="theory-tab-hint">${tab.nav_hint || tab.intro}</span>
    </button>
  `).join('');
}

function renderTheoryTabPanel() {
  const tab = theoryTabs.find((item) => item.id === activeTheoryTab) ?? theoryTabs[0];
  const sections = (tab.sections || []).map((section) => `
    <article class="theory-section">
      <h3>${section.title}</h3>
      <p>${section.body}</p>
    </article>
  `).join('');
  const cards = (tab.cards || []).map((card) => `
    <article class="theory-approach">
      <h3>${card.title}</h3>
      <p>${card.summary}</p>
      <dl>
        <dt>What it is trying to do</dt>
        <dd>${card.trying}</dd>
        <dt>Why it helps</dt>
        <dd>${card.helps}</dd>
        <dt>Why it still falls short</dt>
        <dd>${card.falls_short}</dd>
      </dl>
    </article>
  `).join('');
  const meta = tab.updated ? `<div class="theory-meta-strip"><span class="theory-meta-pill">${tab.updated}</span></div>` : '';
  const timeline = (tab.timeline || []).length ? `
    <section class="theory-block">
      <h3>Twin Prime History Timeline</h3>
      <div class="theory-timeline">
        ${(tab.timeline || []).map((item) => `
          <article class="theory-timeline-card">
            <span class="theory-timeline-label">${item.label}</span>
            <h4>${item.title}</h4>
            <p>${item.body}</p>
          </article>
        `).join('')}
      </div>
    </section>
  ` : '';
  const faq = (tab.faq || []).length ? `
    <section class="theory-block">
      <h3>Twin Prime FAQ</h3>
      <div class="theory-faq-grid">
        ${(tab.faq || []).map((item) => `
          <article class="theory-faq-card">
            <h4>${item.question}</h4>
            <p>${item.answer}</p>
          </article>
        `).join('')}
      </div>
    </section>
  ` : '';
  const references = (tab.references || []).length ? `
    <section class="theory-block">
      <h3>Further Reading and References</h3>
      <div class="theory-reference-list">
        ${(tab.references || []).map((item) => `
          <article class="theory-reference-card">
            <h4>${item.title}</h4>
            <p class="theory-reference-note">${item.note}</p>
          </article>
        `).join('')}
      </div>
    </section>
  ` : '';
  tabPanel.setAttribute('aria-labelledby', `theory-tab-${tab.id}`);
  tabPanel.innerHTML = `
    <div class="theory-intro-block">
      <h2>${tab.label}</h2>
      <p class="theory-intro">${tab.intro}</p>
      ${meta}
    </div>
    ${sections ? `<div class="theory-sections">${sections}</div>` : ''}
    ${cards ? `<div class="theory-approaches">${cards}</div>` : ''}
    ${timeline}
    ${faq}
    ${references}
  `;
}

function setActiveTheoryTab(tabId, options = {}) {
  const { focus = false, updateHash = true } = options;
  activeTheoryTab = tabId;
  renderTheoryTabButtons();
  renderTheoryTabPanel();
  if (updateHash) {
    history.replaceState(null, '', `#${tabId}`);
  }
  if (focus) {
    const activeButton = document.getElementById(`theory-tab-${tabId}`);
    activeButton?.focus();
  }
  attachTabEvents();
}

function focusTabByOffset(currentIndex, offset) {
  const nextIndex = (currentIndex + offset + theoryTabs.length) % theoryTabs.length;
  const nextTabId = theoryTabs[nextIndex].id;
  setActiveTheoryTab(nextTabId, { focus: true });
}
function attachTabEvents() {
  const buttons = Array.from(tabList.querySelectorAll('[role="tab"]'));
  buttons.forEach((button) => {
    button.addEventListener('click', () => setActiveTheoryTab(button.dataset.tabId, { focus: false }));
    button.addEventListener('keydown', (event) => {
      const index = Number(button.dataset.index);
      if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
        event.preventDefault();
        focusTabByOffset(index, 1);
      }
      if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
        event.preventDefault();
        focusTabByOffset(index, -1);
      }
      if (event.key === 'Home') {
        event.preventDefault();
        setActiveTheoryTab(theoryTabs[0].id, { focus: true });
      }
      if (event.key === 'End') {
        event.preventDefault();
        setActiveTheoryTab(theoryTabs[theoryTabs.length - 1].id, { focus: true });
      }
    });
  });
}

window.addEventListener('hashchange', () => {
  const nextTab = getInitialTheoryTabId();
  if (nextTab !== activeTheoryTab) {
    setActiveTheoryTab(nextTab, { focus: false, updateHash: false });
  }
});

if (tabList && tabPanel) {
  setActiveTheoryTab(activeTheoryTab, { focus: false, updateHash: false });
}
"""
    )


def build_asset_version() -> str:
    payload = "||".join([APP_CSS, EXPLORER_JS, ANALYSIS_JS, build_theory_js()])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:12]


def render_page(page: PageDefinition, asset_version: str | None = None) -> str:
    asset_version = asset_version or build_asset_version()
    nav_html = "".join(
        f'<a class="nav-link{" active" if item.active_route == page.active_route else ""}" href="{item.route}">{item.nav_label}</a>'
        for item in PAGE_DEFINITIONS
    )
    if page.active_route == "theory":
        main_html = _render_theory_main_html(page.main_html)
    else:
        main_html = page.main_html
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{page.title}</title>
  <link rel="stylesheet" href="/styles.css?v={asset_version}">
</head>
<body>
  <div class="page-shell">
    <header class="site-header">
      <a class="brand-mark" href="/explorer">
        <span class="brand-kicker">Dual Prime Explorer</span>
        <span class="brand-title">Twin-prime analysis for computation and theory</span>
      </a>
      <nav class="top-nav" aria-label="Primary">
        {nav_html}
      </nav>
    </header>
    {page.hero_html}
    <main class="content-stack">
      {main_html}
    </main>
  </div>
  <script src="/{page.script_name}?v={asset_version}"></script>
</body>
</html>
"""


def build_page_registry() -> dict[str, str]:
    asset_version = build_asset_version()
    return {page.route: render_page(page, asset_version=asset_version) for page in PAGE_DEFINITIONS}


