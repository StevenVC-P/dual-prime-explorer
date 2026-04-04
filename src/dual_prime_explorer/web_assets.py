"""Shared web assets and page rendering helpers."""

from __future__ import annotations

import hashlib
import html
import json
import re

from .web_content import GLOSSARY_SECTIONS, THEORY_TABS
from .web_limits import MAX_WEB_END, MAX_WEB_RANGE_SIZE
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
.hero-copy { max-width: 68ch; display: grid; gap: 12px; }
.theory-copy { max-width: 76ch; }
.theory-hero { margin-bottom: 30px; }
.lab-layout { display: grid; grid-template-columns: minmax(220px, 260px) minmax(0, 1fr) minmax(220px, 280px); gap: 16px; align-items: start; }
.explorer-lab-controls { position: sticky; top: 18px; }
.lab-visualization-card, .lab-context-card { border: 1px solid var(--line); border-radius: 20px; background: var(--panel-soft); padding: 16px; min-width: 0; }
.lab-card-header { display: flex; justify-content: space-between; gap: 10px; align-items: end; margin-bottom: 12px; }
.lab-card-copy { display: grid; gap: 6px; }
.lab-visual-tools { display: grid; gap: 10px; margin-bottom: 12px; }
.lab-view-switch { display: flex; flex-wrap: wrap; gap: 8px; }
.lab-view-button { border: 1px solid var(--line); background: rgba(255, 255, 255, 0.82); color: var(--muted); border-radius: 999px; padding: 8px 12px; cursor: pointer; }
.lab-view-button.active { background: var(--accent); border-color: var(--accent); color: white; }
.lab-view-button:hover, .lab-view-button:focus-visible { outline: none; border-color: var(--line-strong); color: var(--ink); }
.lab-view-button.active:hover, .lab-view-button.active:focus-visible { color: white; }
.lab-mode-note { color: var(--muted); font-size: 0.95rem; }
.lab-pagination { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px; padding: 10px 12px; border: 1px solid var(--line); border-radius: 14px; background: rgba(255, 255, 255, 0.72); }
.lab-pagination-status { color: var(--muted); font-size: 0.92rem; }
.lab-pagination-actions { display: flex; flex-wrap: wrap; gap: 8px; }
.lab-page-button { border: 1px solid var(--line); background: white; color: var(--ink); border-radius: 999px; padding: 8px 12px; cursor: pointer; font: inherit; }
.lab-page-button:hover, .lab-page-button:focus-visible { outline: none; border-color: var(--line-strong); }
.lab-page-button:disabled { cursor: default; opacity: 0.45; }
.visualization-stage { min-height: 420px; border: 1px solid var(--line); border-radius: 18px; background: linear-gradient(180deg, rgba(255,255,255,0.92) 0%, rgba(248,245,238,0.96) 100%); padding: 12px; overflow: auto; }
.visualization-empty { padding: 18px; border-radius: 14px; background: rgba(24, 21, 18, 0.03); color: var(--muted); }
.visualization-svg { display: block; width: 100%; min-width: 520px; height: auto; }
.lab-visual-summary { display: grid; gap: 12px; margin-top: 14px; padding: 14px 16px; border: 1px solid var(--line); border-radius: 16px; background: rgba(255, 255, 255, 0.72); }
.lab-visual-summary .definition-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px; }
.lab-visual-summary .definition-row { padding: 12px; border: 1px solid rgba(24, 21, 18, 0.08); border-radius: 14px; background: rgba(248, 245, 238, 0.9); grid-template-columns: 1fr; gap: 6px; }
.lab-visual-summary .definition-row:first-child { padding-top: 12px; }
.lab-visual-summary .definition-term { font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.06em; }
.lab-visual-summary .definition-value { font-size: 1.9rem; line-height: 1; }
.viz-bridge { fill: rgba(217, 119, 6, 0.14); stroke: rgba(217, 119, 6, 0.18); stroke-width: 1; }
.viz-cell { stroke: rgba(24, 21, 18, 0.08); stroke-width: 1; transition: transform 120ms ease, stroke-width 120ms ease, stroke 120ms ease; }
.viz-cell.composite { fill: #ebe4d9; }
.viz-cell.unit { fill: #f2ede5; }
.viz-cell.factor-simple { fill: #e8dfd3; }
.viz-cell.factor-moderate { fill: #dcccb8; }
.viz-cell.factor-rich { fill: #cab08f; }
.viz-cell.factor-dense { fill: #b08f6d; }
.viz-cell.prime { fill: #5f8f72; }
.viz-cell.twin-prime { fill: #14532d; stroke: rgba(20, 83, 45, 0.3); }
.viz-cell.twin-center { fill: #d97706; stroke: rgba(180, 83, 9, 0.3); }
.visualization-svg.mode-mod6 .viz-cell.residue-0, .visualization-svg.mode-mod6 .viz-cell.residue-2, .visualization-svg.mode-mod6 .viz-cell.residue-3, .visualization-svg.mode-mod6 .viz-cell.residue-4 { opacity: 0.72; }
.visualization-svg.mode-mod6 .viz-cell.residue-1, .visualization-svg.mode-mod6 .viz-cell.residue-5 { opacity: 1; }
.visualization-svg.mode-centers .viz-cell-group { opacity: 0.12; }
.visualization-svg.mode-centers .viz-cell-group.kind-prime { opacity: 0.32; }
.visualization-svg.mode-centers .viz-cell-group.kind-twin-prime { opacity: 0.62; }
.visualization-svg.mode-centers .viz-cell-group.kind-twin-center { opacity: 1; }
.visualization-svg.mode-centers .viz-cell-group.kind-twin-center .viz-cell { stroke: rgba(180, 83, 9, 0.6); stroke-width: 2.8; filter: drop-shadow(0 0 0 rgba(255,255,255,0)) drop-shadow(0 2px 8px rgba(180, 83, 9, 0.24)); }
.visualization-svg.mode-centers .viz-cell-label { opacity: 0.12; }
.visualization-svg.mode-centers .viz-cell-group.kind-prime .viz-cell-label { opacity: 0.38; }
.visualization-svg.mode-centers .viz-cell-group.kind-twin-prime .viz-cell-label { opacity: 0.76; }
.visualization-svg.mode-centers .viz-cell-group.kind-twin-center .viz-cell-label { opacity: 1; font-size: 12px; }
.visualization-svg.mode-centers .viz-bridge { fill: transparent; stroke: rgba(180, 83, 9, 0.24); stroke-width: 1.4; }
.viz-cell-label { font-family: Georgia, "Times New Roman", serif; font-size: 11px; text-anchor: middle; dominant-baseline: middle; pointer-events: none; }
.viz-header-label { font-family: Georgia, "Times New Roman", serif; font-size: 11px; text-anchor: middle; fill: var(--muted); }
.viz-cell-label.light { fill: #fffdf9; }
.viz-cell-label.dark { fill: #3f372f; }
.viz-cell-group { cursor: pointer; }
.viz-cell-group:hover .viz-cell, .viz-cell-group:focus-visible .viz-cell { stroke: rgba(24, 21, 18, 0.35); stroke-width: 2; }
.viz-cell-group.selected .viz-cell { stroke: #181512; stroke-width: 3; }
.lab-hover-actions { display: flex; flex-wrap: wrap; gap: 8px; }
.lab-inline-button { border: 1px solid var(--line); border-radius: 999px; padding: 8px 12px; background: transparent; color: var(--ink); font: inherit; cursor: pointer; }
.lab-inline-button:hover, .lab-inline-button:focus-visible { outline: none; border-color: var(--line-strong); background: rgba(24, 21, 18, 0.03); }
.lab-experiment-panel { margin: 0; padding: 14px; border: 1px solid var(--line); border-radius: 16px; background: rgba(255, 255, 255, 0.68); display: grid; gap: 10px; }
.lab-experiment-panel legend { padding: 0 6px; font-size: 0.82rem; letter-spacing: 0.06em; text-transform: uppercase; color: var(--muted); }
.filter-label { display: block; margin-bottom: 8px; font-size: 0.85rem; color: var(--muted); }
.mod-residue-options { display: grid; grid-template-columns: repeat(4, minmax(42px, 42px)); gap: 8px; width: 100%; max-width: 192px; }
.mod-residue-options .section-copy { grid-column: 1 / -1; max-width: 24ch; }
.mod-residue-pill { position: relative; display: grid; place-items: center; width: 42px; height: 42px; border: 1px solid var(--line); border-radius: 12px; background: white; color: var(--ink); cursor: pointer; transition: border-color 120ms ease, box-shadow 120ms ease, background 120ms ease, color 120ms ease; }
.mod-residue-pill:hover { border-color: var(--line-strong); }
.mod-residue-pill:focus-within { border-color: rgba(20, 83, 45, 0.35); box-shadow: 0 0 0 3px rgba(20, 83, 45, 0.12); }
.mod-residue-pill input { position: absolute; inset: 0; opacity: 0; margin: 0; cursor: pointer; }
.mod-residue-pill span { font-size: 0.92rem; line-height: 1; }
.mod-residue-pill.active { background: var(--accent-soft); border-color: rgba(20, 83, 45, 0.24); color: var(--accent); font-weight: 600; }
.lab-experiment-summary { padding: 10px 12px; border: 1px solid rgba(20, 83, 45, 0.12); border-radius: 12px; background: rgba(236, 246, 238, 0.58); color: var(--muted); font-size: 0.92rem; }
.lab-experiment-summary.active { color: var(--ink); border-color: rgba(20, 83, 45, 0.18); background: rgba(236, 246, 238, 0.82); }
.lab-inline-button:disabled { opacity: 0.45; cursor: default; }
.visualization-svg.mod-filter-active .viz-cell-group.mod-muted { opacity: 0.22; }
.visualization-svg.mod-filter-active .viz-cell-group.mod-match .viz-cell { stroke: rgba(20, 83, 45, 0.42); stroke-width: 2.1; }
.visualization-svg.mod-filter-active.mode-centers .viz-cell-group.mod-muted { opacity: 0.08; }
.visualization-svg.mod-filter-active.mode-centers .viz-cell-group.kind-twin-center.mod-match { opacity: 1; }
.lab-hover-card { display: grid; gap: 12px; padding: 16px; border-radius: 16px; background: rgba(255, 255, 255, 0.78); border: 1px solid var(--line); margin-bottom: 14px; }
.lab-hover-header { display: grid; gap: 6px; }
.lab-hover-number { font-size: 2rem; line-height: 1; }
.lab-hover-kicker { text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.76rem; color: var(--muted); }
.lab-hover-pair { display: inline-flex; align-items: center; gap: 6px; width: fit-content; padding: 6px 10px; border-radius: 999px; background: rgba(20, 83, 45, 0.08); color: var(--accent); border: 1px solid rgba(20, 83, 45, 0.12); font-size: 0.88rem; }
.explanation-card { display: grid; gap: 8px; padding: 12px 14px; border-radius: 16px; background: linear-gradient(180deg, rgba(236,246,238,0.68) 0%, rgba(255,255,255,0.82) 100%); border: 1px solid rgba(20, 83, 45, 0.12); }
.explanation-kicker { text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.76rem; color: var(--accent); }
.explanation-card h3 { font-size: 0.98rem; }
.explanation-card p { color: var(--muted); }
.explanation-detail-grid { display: grid; gap: 8px; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }
.explanation-detail { padding: 10px 12px; border: 1px solid rgba(20, 83, 45, 0.12); border-radius: 12px; background: rgba(255, 255, 255, 0.76); }
.explanation-detail-label { display: block; margin-bottom: 4px; font-size: 0.74rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); }
.explanation-detail-value { color: var(--ink); line-height: 1.55; }
.explanation-points { display: grid; gap: 6px; margin: 0; padding-left: 18px; color: var(--muted); }
.explanation-points li { line-height: 1.55; }
.explanation-links { display: flex; flex-wrap: wrap; gap: 10px; }
.analysis-intro-card { margin-bottom: 16px; }
.explorer-state-explanation { margin: 14px 0; }
.lab-fact-list { display: grid; gap: 10px; }
.lab-fact { display: grid; gap: 5px; padding-top: 10px; border-top: 1px solid rgba(24, 21, 18, 0.08); }
.lab-fact:first-child { border-top: 0; padding-top: 0; }
.lab-fact-label { font-size: 0.82rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }
.lab-fact-value { color: var(--ink); line-height: 1.5; word-break: break-word; }
.lab-divisor-box { max-height: 160px; overflow: auto; padding: 10px 12px; border-radius: 12px; background: rgba(24, 21, 18, 0.03); border: 1px solid rgba(24, 21, 18, 0.08); }
.lab-legend { display: grid; gap: 10px; margin-bottom: 14px; }
.lab-legend-item { display: flex; align-items: center; gap: 10px; color: var(--muted); }
.lab-swatch { width: 14px; height: 14px; border-radius: 999px; border: 1px solid rgba(24, 21, 18, 0.08); display: inline-block; }
.lab-swatch.composite { background: #ebe4d9; }
.lab-swatch.prime { background: #5f8f72; }
.lab-swatch.twin-prime { background: #14532d; }
.lab-swatch.twin-center { background: #d97706; }
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
.insight-pill-button { font: inherit; cursor: pointer; transition: border-color 120ms ease, background 120ms ease, color 120ms ease, transform 120ms ease; }
.insight-pill-button:hover, .insight-pill-button:focus-visible { outline: none; border-color: rgba(20, 83, 45, 0.28); background: rgba(20, 83, 45, 0.12); color: #0f3f22; transform: translateY(-1px); }
.definition-list { display: grid; gap: 10px; margin: 0; }
.definition-row { display: grid; grid-template-columns: minmax(110px, 160px) minmax(0, 1fr); gap: 12px; align-items: start; padding: 10px 0; border-top: 1px solid rgba(24, 21, 18, 0.08); }
.definition-row:first-child { border-top: 0; padding-top: 0; }
.definition-term { color: var(--muted); font-size: 0.92rem; }
.definition-value { font-variant-numeric: tabular-nums; }
.empty-note { padding: 14px 16px; border-radius: 16px; background: var(--panel-subtle); border: 1px dashed var(--line); color: var(--muted); }
.error { color: #8a1c1c; border: 1px solid rgba(138, 28, 28, 0.18); background: rgba(249, 115, 115, 0.08); padding: 14px; border-radius: 16px; }
.theory-layout { display: grid; grid-template-columns: minmax(250px, 300px) minmax(0, 1fr); gap: 22px; align-items: start; }
.theory-tabs-shell { align-self: start; }
.theory-tabs { display: grid; gap: 10px; }
.theory-tab { text-align: left; border: 1px solid var(--line); border-radius: 16px; padding: 16px 18px; background: transparent; color: var(--muted); cursor: pointer; }
.theory-tab:hover, .theory-tab:focus-visible { outline: none; border-color: var(--line-strong); color: var(--ink); }
.theory-tab.active { background: var(--accent-soft); border-color: rgba(20, 83, 45, 0.24); color: var(--ink); }
.theory-tab.active .theory-tab-label { color: var(--accent); }
.theory-tab-label { display: block; font-weight: 600; margin-bottom: 4px; }
.theory-tab-hint { display: block; font-size: 0.92rem; line-height: 1.45; }
.theory-content-shell { min-width: 0; }
.theory-tabpanel { display: grid; gap: 16px; outline: none; }
.theory-intro-block { display: grid; gap: 8px; padding-bottom: 4px; }
.theory-intro { max-width: 70ch; }
.theory-sections, .theory-approaches, .theory-timeline, .theory-faq-grid, .theory-reference-list, .theory-action-grid, .glossary-sections, .glossary-terms { display: grid; gap: 14px; }
.theory-section, .theory-approach, .theory-timeline-card, .theory-faq-card, .theory-reference-card, .theory-action-card, .glossary-section, .glossary-term-card { padding: 18px; }
.theory-approach dl { display: grid; gap: 8px; margin: 0; }
.theory-approach dt { font-weight: 600; }
.theory-approach dd { margin: 0; color: var(--muted); }
.theory-meta-strip { display: flex; flex-wrap: wrap; gap: 10px; }
.theory-meta-pill { padding: 8px 12px; border-radius: 999px; background: var(--accent-faint); color: var(--accent); border: 1px solid rgba(20, 83, 45, 0.12); font-size: 0.9rem; }
.theory-block { display: grid; gap: 12px; margin-bottom: 10px; }
.theory-block h3 { font-size: 1.02rem; }
.theory-timeline-card { border: 1px solid var(--line); border-radius: 18px; background: linear-gradient(180deg, rgba(255,255,255,0.95) 0%, rgba(248,245,238,0.92) 100%); }
.theory-timeline-label { display: inline-block; margin-bottom: 8px; font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); }
.theory-faq-grid { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.theory-faq-card h4, .theory-reference-card h4 { margin: 0 0 8px; font-size: 0.98rem; }
.theory-reference-note, .theory-faq-card p, .theory-timeline-card p, .theory-action-card p { color: var(--muted); }
.theory-action-grid { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.theory-action-card { border: 1px solid var(--line); border-radius: 18px; background: rgba(255,255,255,0.82); display: grid; gap: 10px; }
.theory-path-grid { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.theory-path-card { border: 1px solid var(--line); border-radius: 18px; background: rgba(255,255,255,0.72); }
.theory-action-header { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 10px; }
.theory-action-kicker { display: inline-block; font-size: 0.78rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); }
.theory-destination-badge { display: inline-flex; align-items: center; min-height: 28px; padding: 4px 10px; border-radius: 999px; border: 1px solid rgba(20, 83, 45, 0.12); background: var(--accent-faint); color: var(--accent); font-size: 0.82rem; font-weight: 600; }
.theory-action-card h4 { margin: 0 0 8px; font-size: 1rem; }
.theory-action-card .inline-link { font-weight: 600; }
.theory-reference-list { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.glossary-sections { gap: 18px; }
.glossary-section { border: 1px solid var(--line); border-radius: 18px; background: var(--panel-soft); }
.glossary-section-header { display: grid; gap: 8px; margin-bottom: 14px; }
.glossary-terms { grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); }
.glossary-term-card { border: 1px solid rgba(24, 21, 18, 0.08); border-radius: 16px; background: rgba(255,255,255,0.72); }
.glossary-term-card h3 { margin-bottom: 8px; }
.glossary-inline-link { color: var(--accent); font-weight: 600; text-decoration: none; }
.glossary-inline-link:hover, .glossary-inline-link:focus-visible { text-decoration: underline; outline: none; }
.glossary-jump-shell { display: grid; gap: 10px; margin-top: 12px; padding: 12px 14px; border: 1px solid rgba(24, 21, 18, 0.08); border-radius: 16px; background: rgba(255,255,255,0.5); }
.glossary-strip-header { display: grid; gap: 4px; }
.glossary-strip-label { font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--muted); }
.glossary-strip-copy { color: var(--muted); font-size: 0.94rem; line-height: 1.5; }
.glossary-jump-strip { display: flex; flex-wrap: wrap; gap: 10px; }
.glossary-toolbar { display: grid; gap: 14px; margin-bottom: 18px; }
.glossary-search-control { display: grid; gap: 8px; max-width: 420px; }
.glossary-search-control span { color: var(--muted); font-size: 0.9rem; }
.glossary-search-control input { width: 100%; min-height: 46px; border: 1px solid var(--line); border-radius: 12px; padding: 11px 13px; font: inherit; background: white; color: var(--ink); }
.glossary-search-control input:focus-visible { outline: none; border-color: rgba(20, 83, 45, 0.35); box-shadow: 0 0 0 3px rgba(20, 83, 45, 0.12); }
.glossary-term-card.is-hidden, .glossary-section.is-hidden { display: none; }
.glossary-term-summary { color: var(--ink); font-weight: 600; line-height: 1.55; margin-bottom: 8px; }
.glossary-term-detail { color: var(--muted); }
.glossary-term-links { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 12px; }
@media (max-width: 1024px) {
  .filter-layout { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .filter-group-grid-wide { grid-template-columns: 1fr; }
}
@media (max-width: 900px) {
  .site-header, .hero-grid, .theory-layout, .lab-layout { grid-template-columns: 1fr; display: grid; }
  .explorer-lab-controls { position: static; }
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
  visualHoverNumber: null,
  selectedVisualNumber: null,
  visualMode: 'standard',
  visualPage: 0,
  modBase: null,
  modResidues: [],
};
const analysisCache = new Map();
const maxWebRangeSize = 20000;
const ANALYSIS_TABS = ['modular', 'gaps', 'factors', 'density', 'expected'];
const maxWebEnd = 200000;
const VISUAL_PAGE_COLUMNS = 24;
const VISUAL_PAGE_ROWS = 25;
const VISUAL_PAGE_SIZE = VISUAL_PAGE_COLUMNS * VISUAL_PAGE_ROWS;

const form = document.getElementById('analysis-form');
const statusText = document.getElementById('status-text');
const summaryCards = document.getElementById('summary-cards');
const tabContent = document.getElementById('tab-content');
const tabButtons = Array.from(document.querySelectorAll('.tab-button'));
const tabShortcutButtons = Array.from(document.querySelectorAll('[data-analysis-target]'));

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

function makeExplanationCard(config, extraClass = '') {
  const detailItems = [];
  if (config.question) {
    detailItems.push({ label: 'This view answers', value: config.question });
  }
  if (config.lookFor) {
    detailItems.push({ label: 'What to look for', value: config.lookFor });
  }
  if (config.nextStep) {
    detailItems.push({ label: 'Best next step', value: config.nextStep });
  }
  const details = detailItems.length ? `<div class="explanation-detail-grid">${detailItems.map((item) => `
    <div class="explanation-detail">
      <span class="explanation-detail-label">${item.label}</span>
      <div class="explanation-detail-value">${item.value}</div>
    </div>
  `).join('')}</div>` : '';
  const points = (config.points || []).length ? `<ul class="explanation-points">${config.points.map((point) => `<li>${point}</li>`).join('')}</ul>` : '';
  const links = (config.links || []).length ? `<div class="explanation-links">${config.links.map((link) => `<a class="inline-link" href="${link.href}">${link.label}</a>`).join('')}</div>` : '';
  return `
    <article class="explanation-card ${extraClass}">
      <span class="explanation-kicker">${config.kicker}</span>
      <h3>${config.title}</h3>
      <p>${config.body}</p>
      ${details}
      ${points}
      ${links}
    </article>
  `;
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

function getAnalysisTabExplanation(analysis) {
  const gapData = analysis.gap_analysis;
  const centerAverageDivisors = analysis.factorization_analysis.center_aggregate.average_divisor_count;
  const density = analysis.density_analysis;
  const lastExpected = analysis.expected_vs_observed[analysis.expected_vs_observed.length - 1];
  const centerMod6Zero = Number(analysis.center_mod6_counts['0'] ?? analysis.center_mod6_counts[0] ?? 0);
  const structuresAfterFirst = analysis.pair_structures.filter((row) => row.pair[0] > 5);
  const sixKPatternCount = structuresAfterFirst.filter((row) => row.pair_mod6[0] === 5 && row.pair_mod6[1] === 1).length;
  const densityRatios = density.pair_density_stats.map((row) => row.local_to_global_ratio).filter((value) => typeof value === 'number');
  const averageDensityRatio = densityRatios.length ? densityRatios.reduce((total, value) => total + value, 0) / densityRatios.length : null;
  const centerRecords = analysis.factorization_analysis.center_records;
  const explanations = {
    modular: {
      kicker: 'Read this view',
      title: structuresAfterFirst.length ? 'Start here for structural patterns.' : 'This range is still in the early structural cases.',
      body: structuresAfterFirst.length
        ? 'Use Modular when you want to see whether twin-prime pairs and their centers are following the residue patterns you expect.'
        : 'Use Modular to read the bootstrap cases first. Small ranges still show the first few exceptions before the usual residue pattern fully takes over.',
      question: 'Are the pairs in this range following the usual modular structure of later twin primes?',
      lookFor: structuresAfterFirst.length
        ? `${formatValue(sixKPatternCount)} of ${formatValue(structuresAfterFirst.length)} later pairs currently match the 6k +/- 1 pattern, and ${formatValue(centerMod6Zero)} centers land at 0 mod 6.`
        : 'In very small ranges, treat the first few pairs as setup cases and watch for the later 6k +/- 1 rhythm to emerge as the range grows.',
      nextStep: 'If the residue structure looks clean here, follow it into Theory or compare the same range in the Lab Mod 6 mode.',
      points: [
        'Most later pairs should line up with the 6k +/- 1 pattern.',
        'Later twin centers should collect in the 0 class modulo 6.',
      ],
      links: [
        { href: '/glossary#glossary-term-mod-6', label: 'Glossary: Mod 6' },
        { href: '/analysis-guide', label: 'Open Analysis Guide' },
        { href: '/theory#approaches', label: 'Theory: Approaches' },
      ],
    },
    gaps: {
      kicker: 'Read this view',
      title: gapData.pair_start_gaps.length ? 'Start here for spacing.' : 'This range has too few twin-prime events for a spacing pattern.',
      body: gapData.pair_start_gaps.length
        ? 'Use Gaps when you want to see how far apart twin-prime events are appearing in the current range.'
        : 'Use Gaps once the range contains several twin-prime events. Right now the range is better for spotting individual pairs than measuring repeated spacing.',
      question: 'How much space is opening up between one twin-prime event and the next?',
      lookFor: gapData.pair_start_gaps.length
        ? `This range currently tracks ${formatValue(gapData.pair_start_gaps.length)} pair-start gaps. Repeated gap sizes matter more than the raw average.`
        : 'A stronger spacing story appears once you have several pair-start gaps to compare, not just one isolated jump.',
      nextStep: 'If repeated gap sizes start standing out, compare them with the Lab first, then use Theory when you want the bounded-gap context.',
      points: [
        `Current pair-start gaps tracked: ${formatValue(gapData.pair_start_gaps.length)}.`,
        'Look for repeated gap sizes before focusing on the averages.',
      ],
      links: [
        { href: '/glossary#glossary-term-prime-gap', label: 'Glossary: Prime Gap' },
        { href: '/lab#visualization-title', label: 'Open Lab' },
        { href: '/theory#progress', label: 'Theory: Current Progress' },
      ],
    },
    factors: {
      kicker: 'Read this view',
      title: centerRecords.length ? 'Start here for center arithmetic.' : 'This range does not yet have twin centers to compare.',
      body: centerRecords.length
        ? 'Use Factors when you want to compare twin centers against the broader even-number baseline.'
        : 'Use Factors once the range contains twin centers. Without them, the comparison is mostly a baseline for what the broader even field looks like.',
      question: 'Do twin centers look arithmetically different from other even numbers in the same range?',
      lookFor: centerRecords.length
        ? `Twin centers in this range average ${formatValue(centerAverageDivisors)} divisors. Compare that to the non-center even baseline before deciding whether the centers feel unusual.`
        : 'Expand the range until twin centers appear, then compare divisor count and squarefree frequency instead of reading this as a standalone factor table.',
      nextStep: 'Use this view after the Lab makes twin centers visually obvious and you want to test whether their arithmetic looks unusual.',
      points: [
        `Current average divisor count for centers: ${formatValue(centerAverageDivisors)}.`,
        'Squarefree frequency is often more useful than raw factor count alone.',
      ],
      links: [
        { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
        { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
        { href: '/theory#why-its-hard', label: "Theory: Why It's Hard" },
      ],
    },
    density: {
      kicker: 'Read this view',
      title: density.pair_density_stats.length ? 'Start here for clustering.' : 'This range needs more pair neighborhoods before density says much.',
      body: density.pair_density_stats.length
        ? 'Use Density when you want to compare each local twin-prime neighborhood with the overall range baseline.'
        : 'Use Density once the range contains enough twin-prime neighborhoods to compare locally against the global baseline.',
      question: 'Are twin-prime events appearing in locally denser prime neighborhoods than the full range would suggest?',
      lookFor: density.pair_density_stats.length
        ? `The current average local-to-global density ratio is ${averageDensityRatio !== null ? formatValue(averageDensityRatio) : 'N/A'}. Ratios above 1 signal locally denser neighborhoods.`
        : 'This view becomes more informative once multiple pair neighborhoods can be compared across the same window size.',
      nextStep: 'Use Density after you already recognize the pair locations and want to know whether those neighborhoods are actually richer than the full range.',
      points: [
        `Current window radius: +/-${density.window_radius}.`,
        'A ratio above 1 means the local window is denser than the global baseline.',
      ],
      links: [
        { href: '/glossary#glossary-term-bounded-gaps-between-primes', label: 'Glossary: Bounded Gaps Between Primes' },
        { href: '/theory#progress', label: 'Theory: Current Progress' },
      ],
    },
    expected: {
      kicker: 'Read this view',
      title: 'Start here for heuristic comparison.',
      body: 'Use Expected when you want a benchmark, not a proof. It compares the observed count with a common heuristic estimate.',
      question: 'How does the observed twin-prime count compare with a rough heuristic baseline at this range?',
      lookFor: `At the largest checkpoint, the actual / expected ratio is ${lastExpected && lastExpected.ratio !== null ? formatValue(lastExpected.ratio) : 'N/A'}. Read this as a rough calibration, not as evidence that a structural pattern has been explained.`,
      nextStep: 'Use this last, after you already understand the structure and spacing, so the heuristic stays in the right supporting role.',
      points: [
        `Final actual / expected ratio: ${lastExpected && lastExpected.ratio !== null ? formatValue(lastExpected.ratio) : 'N/A'}.`,
        'Treat this as a benchmark, not as structural evidence on its own.',
      ],
      links: [
        { href: '/analysis-guide', label: 'Open Analysis Guide' },
        { href: '/theory#progress', label: 'Theory: Current Progress' },
      ],
    },
  };
  return explanations[state.activeTab];
}

function getRequestedAnalysisTab() {
  const params = new URLSearchParams(window.location.search);
  const requested = params.get('view');
  return ANALYSIS_TABS.includes(requested) ? requested : null;
}

function getRequestedAnalysisRange() {
  const params = new URLSearchParams(window.location.search);
  const start = Number(params.get('start'));
  const end = Number(params.get('end'));
  return Number.isInteger(start) && Number.isInteger(end) ? { start, end } : null;
}

function getAnalysisViewHref(view, analysis = state.analysis) {
  const url = new URL('/analysis', window.location.origin);
  url.searchParams.set('view', view);
  if (analysis) {
    url.searchParams.set('start', analysis.start);
    url.searchParams.set('end', analysis.limit);
  }
  url.hash = 'analysis-views-title';
  return `${url.pathname}${url.search}${url.hash}`;
}

function syncAnalysisUrlState() {
  if (window.location.pathname !== '/analysis') {
    return;
  }
  const url = new URL(window.location.href);
  url.searchParams.set('view', state.activeTab);
  if (state.analysis) {
    url.searchParams.set('start', state.analysis.start);
    url.searchParams.set('end', state.analysis.limit);
  }
  if (!url.hash) {
    url.hash = 'analysis-views-title';
  }
  window.history.replaceState({}, '', url.toString());
}

function getRangeValidationMessage(start, end) {
  if (!Number.isInteger(start) || !Number.isInteger(end)) {
    return 'Range values must be whole numbers.';
  }
  if (start < 1) {
    return 'Range start must be at least 1.';
  }
  if (end < 2) {
    return 'Range end must be at least 2.';
  }
  if (start > end) {
    return 'Range start must be less than or equal to range end.';
  }
  if (end > maxWebEnd) {
    return `Range end must be ${formatValue(maxWebEnd)} or lower in the web app.`;
  }
  if ((end - start + 1) > maxWebRangeSize) {
    return `Range size must be ${formatValue(maxWebRangeSize)} numbers or fewer.`;
  }
  return null;
}

function showRangeValidationError(message) {
  if (statusText) {
    statusText.textContent = 'Range limit reached.';
  }
  if (visualizationRangeLabel) {
    visualizationRangeLabel.textContent = 'Range limit reached.';
  }
  if (visualizationStage) {
    visualizationStage.innerHTML = `<div class="error">${message}</div>`;
  }
  if (tabContent) {
    tabContent.innerHTML = `<div class="error">${message}</div>`;
  }
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
  const explanation = getAnalysisTabExplanation(state.analysis);
  tabContent.innerHTML = makeExplanationCard(explanation, 'analysis-intro-card') + renderers[state.activeTab](state.analysis);
  tabButtons.forEach((button) => {
    button.classList.toggle('active', button.dataset.tab === state.activeTab);
  });
  syncAnalysisUrlState();
}

async function fetchAnalysis(start, end, onSuccess) {
  const cacheKey = `${start}-${end}`;
  if (statusText) {
    statusText.textContent = 'Analyzing...';
  }
  try {
    let analysis = analysisCache.get(cacheKey);
    if (!analysis) {
      const response = await fetch(`/api/analyze?start=${encodeURIComponent(start)}&end=${encodeURIComponent(end)}`);
      if (!response.ok) {
        const errorPayload = await response.json();
        throw new Error(errorPayload.error || 'Request failed.');
      }
      analysis = await response.json();
      analysisCache.set(cacheKey, analysis);
    }
    state.analysis = analysis;
    renderSummary(analysis);
    if (onSuccess) {
      onSuccess(analysis);
    }
    renderAnalysisTabs();
    if (statusText) {
      statusText.textContent = `Computed ${analysis.twin_pairs.length} twin-prime pairs in ${analysis.start}-${analysis.limit}.`;
    }
  } catch (error) {
    const message = error instanceof Error ? error.message : 'Unknown error';
    if (statusText) {
      statusText.textContent = 'Analysis failed.';
    }
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
const tableStateExplanation = document.getElementById('table-state-explanation');
const visualizationStage = document.getElementById('visualization-stage');
const visualizationHover = document.getElementById('visualization-hover');
const visualizationRangeLabel = document.getElementById('visualization-range-label');
const explorerVisualSummary = document.getElementById('explorer-visual-summary');
const visualizationModeButtons = Array.from(document.querySelectorAll('[data-visual-mode]'));
const visualizationModeNote = document.getElementById('visualization-mode-note');
const visualizationPagination = document.getElementById('visualization-pagination');
const startInput = document.getElementById('start-input');
const endInput = document.getElementById('end-input');
const modBaseInput = document.getElementById('mod-base-input');
const modResidueOptions = document.getElementById('mod-residue-options');
const clearModFilterButton = document.getElementById('clear-mod-filter');
const modFilterSummary = document.getElementById('mod-filter-summary');
let explorerRangeTimer = null;

function getNormalizedResidue(number, modulus) {
  return ((number % modulus) + modulus) % modulus;
}

function hasActiveModFilter() {
  return Number.isInteger(state.modBase) && state.modBase >= 2 && state.modResidues.length > 0;
}

function getResidueFilterLabel() {
  if (!hasActiveModFilter()) {
    return 'No mod filter';
  }
  return `mod ${state.modBase}: ${state.modResidues.join(', ')}`;
}

function renderModResidueOptions() {
  if (!modResidueOptions) {
    return;
  }
  const modulus = Number(modBaseInput?.value);
  if (!Number.isInteger(modulus) || modulus < 2 || modulus > 60) {
    modResidueOptions.innerHTML = '<p class="section-copy">Enter a modulus to generate residues.</p>';
    state.modBase = null;
    state.modResidues = [];
    renderModFilterSummary();
    return;
  }
  state.modBase = modulus;
  state.modResidues = state.modResidues.filter((value) => value < modulus);
  modResidueOptions.innerHTML = Array.from({ length: modulus }, (_, residue) => `
    <label class="mod-residue-pill${state.modResidues.includes(residue) ? ' active' : ''}"><input type="checkbox" value="${residue}" ${state.modResidues.includes(residue) ? 'checked' : ''} aria-label="Residue ${residue}"> <span>${residue}</span></label>
  `).join('');
  renderModFilterSummary();
  Array.from(modResidueOptions.querySelectorAll('input[type="checkbox"]')).forEach((input) => {
    input.addEventListener('change', () => {
      state.modResidues = Array.from(modResidueOptions.querySelectorAll('input[type="checkbox"]:checked')).map((item) => Number(item.value)).sort((left, right) => left - right);
      Array.from(modResidueOptions.querySelectorAll('.mod-residue-pill')).forEach((pill) => {
        const checkbox = pill.querySelector('input');
        pill.classList.toggle('active', Boolean(checkbox?.checked));
      });
      renderModFilterSummary();
      if (state.analysis) {
        renderExplorerVisualization(state.analysis);
      }
    });
  });
}

function renderModFilterSummary() {
  if (!modFilterSummary) {
    return;
  }
  const active = hasActiveModFilter();
  modFilterSummary.classList.toggle('active', active);
  modFilterSummary.textContent = active
    ? `Active filter: ${getResidueFilterLabel()}`
    : 'No mod filter active.';
  if (clearModFilterButton) {
    clearModFilterButton.disabled = !active && !(modBaseInput && modBaseInput.value);
  }
}

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

function getSelectedNeighborhoodFilters() {
  return filterNeighborhoodOptions.filter((option) => option.checked).map((option) => option.value);
}

function getExplorerTableExplanation(analysis, filteredRows) {
  const divisorValues = parseDivisorFilterValues();
  const selectedNeighborhoods = getSelectedNeighborhoodFilters();
  const activeFilters = [];
  if (filterRole && filterRole.value !== 'all') {
    activeFilters.push(`prime role: ${formatPrimeRole({ prime_role: filterRole.value })}`);
  }
  if (selectedNeighborhoods.length) {
    activeFilters.push(`neighborhood: ${selectedNeighborhoods.map((value) => formatAdjacentPrimeRole({ number_type: value === 'prime' || value === 'prime_edge_case' ? 'prime' : 'composite', adjacent_prime_role: value === 'twin_center' ? 'between_two_primes' : value, is_edge_case: value === 'prime_edge_case' })).join(', ')}`);
  }
  if (divisorValues.length) {
    activeFilters.push(`divisors: ${divisorValues.join(', ')} (${(filterDivisorLogic?.value || 'or').toUpperCase()})`);
  }
  if (filterMin?.value || filterMax?.value) {
    activeFilters.push(`numeric slice: ${filterMin?.value || analysis.start}-${filterMax?.value || analysis.limit}`);
  }

  if (!filteredRows.length) {
    const noResultLinks = divisorValues.length
      ? [
          { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
          { href: '/glossary#glossary-term-prime-neighborhood', label: 'Glossary: Prime Neighborhood' },
        ]
      : [
          { href: '/glossary#glossary-term-prime-neighborhood', label: 'Glossary: Prime Neighborhood' },
        ];
    return {
      kicker: 'Current table state',
      title: 'No numbers match the current filter combination.',
      body: activeFilters.length
        ? `The current slice is too narrow: ${activeFilters.join(' | ')}.`
        : 'No numbers are visible right now.',
      question: 'Which filter should you relax first to recover a meaningful comparison set?',
      lookFor: 'Clear one filter at a time, especially divisor requirements or narrow numeric slices, until a useful comparison group returns.',
      nextStep: 'Reset the table filters or remove the most restrictive filter first, then use Analysis once the slice contains enough structure to interpret.',
      links: noResultLinks,
    };
  }

  if (selectedNeighborhoods.includes('twin_center') && divisorValues.length) {
    const logicLabel = (filterDivisorLogic?.value || 'or').toUpperCase();
    return {
      kicker: 'Current table state',
      title: 'You are isolating twin centers through a divisor rule.',
      body: `This slice is combining twin-center structure with a divisor filter: ${divisorValues.join(', ')} (${logicLabel}).`,
      question: 'Do the twin centers that survive this arithmetic slice still look representative of the range, or are you narrowing down to a special sub-pattern?',
      lookFor: `${formatValue(filteredRows.length)} twin-center rows currently satisfy the divisor rule. Compare whether the survivors still look spread across the full range or collapse into a much tighter arithmetic subset.`,
      nextStep: 'Use Factors in Analysis next if the arithmetic slice looks meaningful, and use Theory only after you know the pattern is worth explaining.',
      links: [
        { href: getAnalysisViewHref('factors', analysis), label: 'Open Factors in Analysis' },
        { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
        { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
      ],
    };
  }

  if (filterRole?.value === 'prime_in_twin_pair') {
    return {
      kicker: 'Current table state',
      title: 'You are isolating twin-prime members.',
      body: `This slice shows only primes that belong to twin-prime pairs in ${analysis.start}-${analysis.limit}.`,
      question: 'Where are the pair members, and how dense or sparse do they feel in this range?',
      lookFor: `${formatValue(filteredRows.length)} twin-prime rows are visible. Compare their spacing here, then open Gaps when you want the distance pattern summarized.`,
      nextStep: 'Use this table to inspect exact rows, then jump to Gaps in Analysis for the spacing story across the same range.',
      links: [
        { href: getAnalysisViewHref('gaps', analysis), label: 'Open Gaps in Analysis' },
        { href: '/glossary#glossary-term-twin-prime', label: 'Glossary: Twin Prime' },
      ],
    };
  }

  if (selectedNeighborhoods.includes('twin_center')) {
    return {
      kicker: 'Current table state',
      title: 'You are isolating twin centers.',
      body: 'This slice centers the table on the numbers that sit between paired primes.',
      question: 'Do these centers look arithmetically or locally different from the broader field?',
      lookFor: `${formatValue(filteredRows.length)} twin-center rows are visible. Compare divisor patterns here, then use Factors in Analysis when you want the center-vs-even baseline.`,
      nextStep: 'Use Factors in Analysis next if you want to test whether the center arithmetic feels unusual rather than just visually obvious.',
      links: [
        { href: getAnalysisViewHref('factors', analysis), label: 'Open Factors in Analysis' },
        { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
      ],
    };
  }

  if (divisorValues.length) {
    const logicLabel = (filterDivisorLogic?.value || 'or').toUpperCase();
    return {
      kicker: 'Current table state',
      title: `You are filtering by divisors: ${divisorValues.join(', ')} (${logicLabel}).`,
      body: 'This slice is testing a divisibility idea directly against the current range rather than just reading the full field.',
      question: 'Does this divisor pattern line up with prime neighborhoods, twin centers, or the broader composite background?',
      lookFor: `${formatValue(filteredRows.length)} rows currently satisfy the divisor rule. Compare their roles and neighborhoods before deciding whether the pattern is structural or incidental.`,
      nextStep: 'If the slice feels meaningful, compare it with the Lab Factors mode or move into Factors in Analysis for the larger arithmetic context.',
      links: [
        { href: getAnalysisViewHref('factors', analysis), label: 'Open Factors in Analysis' },
        { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
      ],
    };
  }

  if (activeFilters.length) {
    return {
      kicker: 'Current table state',
      title: 'You are reading a filtered inspection slice.',
      body: `The table is no longer showing the full analyzed range. Active focus: ${activeFilters.join(' | ')}.`,
      question: 'What does this narrower slice reveal that the full range would hide?',
      lookFor: `${formatValue(filteredRows.length)} of ${formatValue(analysis.number_classifications.length)} rows are still visible. Watch whether the remaining rows cluster around one role, neighborhood, or divisor story.`,
      nextStep: 'Use the table for exact row inspection first, then move into the matching Analysis view once the pattern is clear enough to summarize.',
      links: [
        { href: '/analysis', label: 'Open Analysis' },
        { href: '/glossary', label: 'Open Glossary' },
      ],
    };
  }

  return {
    kicker: 'Current table state',
    title: 'This is the baseline inspection view.',
    body: 'The table is currently showing the full analyzed range without any table filters applied.',
    question: 'Which numbers in this range are twin primes, single primes, twin centers, or composite background?',
    lookFor: `${formatValue(filteredRows.length)} rows are visible across ${analysis.start}-${analysis.limit}. Start broad here, then add one filter at a time when you want to test a narrower idea.`,
    nextStep: 'Begin with a prime role, neighborhood, divisor, or numeric slice only after you know what the unfiltered range looks like.',
    links: [
      { href: '/glossary#glossary-term-prime-neighborhood', label: 'Glossary: Prime Neighborhood' },
      { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
    ],
  };
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

function getVisualizationKind(row) {
  if (row.is_pair_center) {
    return 'twin-center';
  }
  if (row.prime_role === 'prime_in_twin_pair') {
    return 'twin-prime';
  }
  if (row.number_type === 'prime') {
    return 'prime';
  }
  if (row.number_type === 'unit') {
    return 'unit';
  }
  return 'composite';
}

function getVisualizationLabel(row) {
  const labels = {
    'twin-center': 'Twin center',
    'twin-prime': 'Twin prime',
    prime: 'Prime',
    unit: 'Unit',
    composite: 'Composite',
  };
  return labels[getVisualizationKind(row)] || 'Number';
}

function getFactorBand(row) {
  if (row.number_type !== 'composite') {
    return null;
  }
  const divisorCount = row.divisor_count || 0;
  if (divisorCount <= 4) {
    return 'factor-simple';
  }
  if (divisorCount <= 6) {
    return 'factor-moderate';
  }
  if (divisorCount <= 9) {
    return 'factor-rich';
  }
  return 'factor-dense';
}

function getFactorBandLabel(row) {
  const band = getFactorBand(row);
  const labels = {
    'factor-simple': 'Simple composite',
    'factor-moderate': 'Moderately divisible composite',
    'factor-rich': 'Divisor-rich composite',
    'factor-dense': 'Highly divisible composite',
  };
  return labels[band] || '';
}

function buildVisualizationModel(analysis) {
  const rows = analysis.number_classifications;
  const isMod6 = state.visualMode === 'mod6';
  const isFactors = state.visualMode === 'factors';
  const isCenters = state.visualMode === 'centers';
  const pageCount = Math.max(1, Math.ceil(rows.length / VISUAL_PAGE_SIZE));
  const currentPage = Math.min(state.visualPage, pageCount - 1);
  if (state.visualPage !== currentPage) {
    state.visualPage = currentPage;
  }
  const pageStartIndex = currentPage * VISUAL_PAGE_SIZE;
  const pageRows = rows.slice(pageStartIndex, pageStartIndex + VISUAL_PAGE_SIZE);
  const columns = VISUAL_PAGE_COLUMNS;
  const pageRowCount = Math.max(1, Math.ceil(pageRows.length / VISUAL_PAGE_COLUMNS));
  const pageSlotCount = pageRowCount * VISUAL_PAGE_COLUMNS;

  const placements = pageRows.map((row, localIndex) => {
    if (isMod6) {
      const subgroup = Math.floor((localIndex % VISUAL_PAGE_COLUMNS) / 6);
      const residue = ((row.number % 6) + 6) % 6;
      const rowIndex = Math.floor(localIndex / VISUAL_PAGE_COLUMNS);
      const layoutIndex = rowIndex * VISUAL_PAGE_COLUMNS + subgroup * 6 + residue;
      return { row, layoutIndex };
    }
    return { row, layoutIndex: localIndex };
  });

  const rowIndexByNumber = new Map(placements.map((item) => [item.row.number, item.layoutIndex]));
  const sequences = analysis.twin_pairs.map((pair) => {
    const [left, right] = pair;
    const center = (left + right) / 2;
    const leftIndex = rowIndexByNumber.get(left);
    const centerIndex = rowIndexByNumber.get(center);
    const rightIndex = rowIndexByNumber.get(right);
    const rowBand = leftIndex === undefined ? null : Math.floor(leftIndex / columns);
    const sameRow = leftIndex !== undefined && centerIndex !== undefined && rightIndex !== undefined
      && Math.floor(centerIndex / columns) === rowBand
      && Math.floor(rightIndex / columns) === rowBand;
    return { pair, center, leftIndex, centerIndex, rightIndex, sameRow };
  }).filter((item) => item.sameRow);

  const residueHeaders = isMod6 ? Array.from({ length: VISUAL_PAGE_COLUMNS }, (_, index) => index % 6) : [];
  const factorBandCounts = pageRows.reduce((counts, row) => {
    const band = getFactorBand(row);
    if (band) {
      counts[band] = (counts[band] || 0) + 1;
    }
    return counts;
  }, {});
  const pageStartNumber = pageRows.length ? pageRows[0].number : analysis.start;
  const pageEndNumber = pageRows.length ? pageRows[pageRows.length - 1].number : analysis.limit;

  return {
    rows,
    pageRows,
    columns,
    placements,
    slotCount: pageSlotCount,
    sequences,
    isMod6,
    isFactors,
    isCenters,
    residueHeaders,
    factorBandCounts,
    currentPage,
    pageCount,
    pageStartNumber,
    pageEndNumber,
  };
}

function syncVisualizationSelectionStyles() {
  if (!visualizationStage) {
    return;
  }
  const groups = Array.from(visualizationStage.querySelectorAll('[data-number-cell]'));
  groups.forEach((group) => {
    const number = Number(group.getAttribute('data-number-cell'));
    group.classList.toggle('selected', state.selectedVisualNumber === number);
  });
}

function renderVisualizationContext(analysis) {
  if (!visualizationHover || !explorerVisualSummary) {
    return;
  }
  const byNumber = new Map(analysis.number_classifications.map((row) => [row.number, row]));
  const focusedNumber = state.selectedVisualNumber ?? state.visualHoverNumber;
  const focused = focusedNumber ? byNumber.get(focusedNumber) : null;
  const twinCenterCount = analysis.number_classifications.filter((row) => row.is_pair_center).length;
  const highlyDivisibleCount = analysis.number_classifications.filter((row) => getFactorBand(row) === 'factor-dense').length;

  explorerVisualSummary.innerHTML = makeDefinitionList([
    { term: 'Prime count', value: formatValue(analysis.primes.length) },
    { term: 'Twin primes', value: formatValue(analysis.paired_primes.length) },
    { term: 'Twin centers', value: formatValue(twinCenterCount) },
    { term: hasActiveModFilter() ? 'Residue matches' : state.visualMode === 'factors' ? 'Highly divisible' : 'Page size', value: formatValue(hasActiveModFilter() ? analysis.number_classifications.filter((row) => state.modResidues.includes(getNormalizedResidue(row.number, state.modBase))).length : state.visualMode === 'factors' ? highlyDivisibleCount : Math.min(VISUAL_PAGE_SIZE, analysis.limit - analysis.start + 1)) },
  ]);

  const modeExplanation = state.visualMode === 'mod6'
    ? {
        kicker: 'Active mode',
        title: 'Mod 6 makes the residue pattern visible.',
        body: 'Primes greater than 3 must land in the 1 or 5 columns, while twin centers fall in the 0 column. That makes the structure easier to read quickly.',
        points: [
          'Use this mode when structure matters more than exact row-by-row reading.',
          'The first pair region is still exceptional, so treat early values with care.',
        ],
        links: [
          { href: '/glossary#glossary-term-mod-6', label: 'Glossary: Mod 6' },
          { href: getAnalysisViewHref('modular', analysis), label: 'Open Modular in Analysis' },
        ],
      }
    : state.visualMode === 'factors'
      ? {
          kicker: 'Active mode',
          title: 'Factors reveals divisor-heavy composites.',
          body: 'This view keeps twin primes and twin centers visible while showing which composite numbers are simple, moderate, divisor-rich, or highly divisible.',
          points: [
            'Darker composites have more divisors and usually more arithmetic structure packed into them.',
            'Twin centers stay distinct so you can compare pair structure against composite density at the same time.',
          ],
          links: [
            { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
            { href: getAnalysisViewHref('factors', analysis), label: 'Open Factors in Analysis' },
          ],
        }
      : state.visualMode === 'centers'
        ? {
            kicker: 'Active mode',
            title: 'Twin Centers isolates where pairs occur.',
            body: 'This view pulls the background back so the numbers between twin primes become the main landmarks in the field.',
            points: [
              'Use this mode when the main question is where twin primes occur across the range.',
              'Twin primes remain visible as supporting context around each highlighted center.',
            ],
            links: [
              { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
              { href: getAnalysisViewHref('factors', analysis), label: 'Open Factors in Analysis' },
            ],
          }
        : {
            kicker: 'Active mode',
            title: 'Standard is the fastest way to scan the field.',
            body: 'This compact layout is best when you want a quick read of where primes, twin primes, and twin centers start to cluster.',
            points: [
              'Use this view first when you want a quick visual read of the field.',
              'Pin a number when you want to stop the hover preview and inspect it in place.',
            ],
            links: [
              { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
              { href: getAnalysisViewHref('modular', analysis), label: 'Open Modular in Analysis' },
            ],
          };

  const modFilterNote = hasActiveModFilter() ? makeExplanationCard(state.visualMode === 'centers' && state.modBase === 6 ? {
    kicker: 'Active experiment',
    title: 'Twin centers inside Mod 6.',
    body: 'This combined state narrows the field to one residue system while keeping twin centers as the main landmarks.',
    question: 'Do the center positions still collect where the Mod 6 structure suggests they should?',
    lookFor: 'Twin centers should remain the main anchors while the chosen residue slice clarifies which numbers belong to the same modular lane.',
    nextStep: 'Use Modular in Analysis next if the residue pattern looks clean enough to summarize.',
    links: [
      { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
      { href: '/glossary#glossary-term-mod-6', label: 'Glossary: Mod 6' },
      { href: getAnalysisViewHref('modular', analysis), label: 'Open Modular in Analysis' },
    ],
  } : state.visualMode === 'factors' ? {
    kicker: 'Active experiment',
    title: `Divisor pressure inside ${getResidueFilterLabel()}.`,
    body: 'This combined state lets you compare divisor-heavy composites against one modular slice at a time.',
    question: 'Are the divisor-rich composites in this residue slice behaving like broad background, or do they seem to crowd around the same local structures?',
    lookFor: 'Watch whether the darker composites cluster near the same twin-center or twin-prime landmarks, or whether they stay more evenly spread through the slice.',
    nextStep: 'Move into Factors in Analysis only after you know whether the modular slice changes the arithmetic story in a visible way.',
    links: [
      { href: '/glossary#glossary-term-residue-class', label: 'Glossary: Residue Class' },
      { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
      { href: getAnalysisViewHref('factors', analysis), label: 'Open Factors in Analysis' },
    ],
  } : {
    kicker: 'Active experiment',
    title: `Watching ${getResidueFilterLabel()}.`,
    body: 'The field is currently emphasizing one modular slice so you can test whether a residue pattern lines up with twin-prime structure.',
    question: 'Which kinds of numbers stay prominent inside this residue slice, and which patterns fade away?',
    lookFor: 'Matching numbers stay prominent while non-matching numbers recede into the background. Watch whether twin primes and twin centers remain easy to spot inside the slice.',
    nextStep: 'Use Modular in Analysis if the slice looks structural rather than incidental.',
    links: [
      { href: '/glossary#glossary-term-residue-class', label: 'Glossary: Residue Class' },
      { href: getAnalysisViewHref('modular', analysis), label: 'Open Modular in Analysis' },
    ],
  }) : '';

  if (!focused) {
    visualizationHover.innerHTML = `
      ${modFilterNote}
      ${makeExplanationCard(modeExplanation)}
      <span class="lab-hover-kicker">Hover or select a number</span>
      <div class="lab-hover-number">${analysis.start}-${analysis.limit}</div>
      <p>Prime numbers, twin-prime members, and twin centers are all visible in the field. Hover to browse, or click a number to pin it here.</p>
    `;
    return;
  }

  const divisors = focused.all_divisors?.length ? focused.all_divisors.join(', ') : 'None';
  const selectionMode = state.selectedVisualNumber === focused.number ? 'Pinned selection' : 'Hover preview';
  const pairBadge = focused.center_of_pair ? `<div class="lab-hover-pair">Pair ${focused.center_of_pair.join(' - ')}</div>` : '';
  const selectionExplanation = focused.is_pair_center
    ? {
        kicker: 'Why this matters',
        title: `${focused.number} is the center of a twin-prime pair.`,
        body: 'Twin centers sit exactly between twin primes, so they often make local pair structure easier to spot than the primes alone.',
        points: [
          `Current pair: ${focused.center_of_pair.join(' - ')}.`,
          'In Mod 6, twin centers usually collect in the 0 column after the early exceptions.',
        ],
        links: [
          { href: '/glossary#glossary-term-twin-center', label: 'Glossary: Twin Center' },
          { href: getAnalysisViewHref('factors', analysis), label: 'Analyze centers in Factors' },
        ],
      }
    : focused.prime_role === 'prime_in_twin_pair'
      ? {
          kicker: 'Why this matters',
          title: `${focused.number} belongs to a twin-prime pair.`,
          body: 'Twin primes are the main structural event in the Lab. This number is one side of a prime pair separated by exactly 2.',
          points: [
            'Compare it with the center between the pair to see the surrounding local structure.',
          ],
          links: [
            { href: '/glossary#glossary-term-twin-prime', label: 'Glossary: Twin Prime' },
            { href: getAnalysisViewHref('gaps', analysis), label: 'Trace spacing in Gaps' },
          ],
        }
      : focused.number_type === 'prime'
        ? {
            kicker: 'Why this matters',
            title: `${focused.number} is a single prime here.`,
            body: 'Single primes show where primes appear without forming a twin-prime event in the current selection.',
            points: [
              'They provide the baseline against which twin-prime structure becomes visually meaningful.',
            ],
            links: [
              { href: '/glossary#glossary-term-single-prime', label: 'Glossary: Single Prime' },
              { href: getAnalysisViewHref('density', analysis), label: 'Compare with Density' },
            ],
          }
        : {
            kicker: 'Why this matters',
            title: `${focused.number} is not prime in this view.`,
            body: 'Composite numbers and the unit 1 create the background that primes must avoid. Their divisor structure helps shape where prime patterns can appear in the field.',
            points: [
              `Prime neighborhood: ${formatAdjacentPrimeRole(focused)}.`,
              ...(state.visualMode === 'factors' && getFactorBandLabel(focused) ? [`Factor view: ${getFactorBandLabel(focused)}.`] : []),
            ],
            links: [
              { href: '/glossary#glossary-term-not-prime', label: 'Glossary: Not Prime' },
              { href: '/glossary#glossary-term-divisor', label: 'Glossary: Divisor' },
              { href: getAnalysisViewHref('factors', analysis), label: 'Compare in Factors' },
            ],
          };
  visualizationHover.innerHTML = `
    ${modFilterNote}
    ${makeExplanationCard(selectionExplanation)}
    <div class="lab-hover-header">
      <span class="lab-hover-kicker">${selectionMode}</span>
      <div class="lab-hover-number">${focused.number}</div>
      <p>${focused.is_pair_center ? 'This number sits exactly between two twin primes.' : formatPrimeRole(focused)}</p>
      ${pairBadge}
    </div>
    <div class="lab-fact-list">
      <div class="lab-fact">
        <span class="lab-fact-label">Number type</span>
        <div class="lab-fact-value">${formatNumberType(focused)}</div>
      </div>
      <div class="lab-fact">
        <span class="lab-fact-label">Neighborhood</span>
        <div class="lab-fact-value">${formatAdjacentPrimeRole(focused)}</div>
      </div>
      <div class="lab-fact">
        <span class="lab-fact-label">Prime divisors</span>
        <div class="lab-fact-value">${formatDivisibility(focused)}</div>
      </div>
      <div class="lab-fact">
        <span class="lab-fact-label">All divisors</span>
        <div class="lab-fact-value lab-divisor-box">${divisors}</div>
      </div>
    </div>
    ${state.selectedVisualNumber === focused.number ? '<div class="lab-hover-actions"><button id="clear-visual-selection" class="lab-inline-button" type="button">Clear selection</button></div>' : ''}
  `;

  const clearButton = document.getElementById('clear-visual-selection');
  clearButton?.addEventListener('click', () => {
    state.selectedVisualNumber = null;
    syncVisualizationSelectionStyles();
    renderVisualizationContext(analysis);
  });
}

function renderExplorerVisualization(analysis) {
  if (!visualizationStage) {
    return;
  }
  const model = buildVisualizationModel(analysis);
  const slotCount = model.slotCount;
  const columns = model.columns;
  const cellSize = model.isMod6 ? 30 : 30;
  const gap = model.isMod6 ? 5 : 5;
  const padding = 16;
  const headerHeight = model.isMod6 ? 24 : 0;
  const rows = Math.ceil(slotCount / columns);
  const svgWidth = padding * 2 + columns * cellSize + (columns - 1) * gap;
  const svgHeight = padding * 2 + headerHeight + rows * cellSize + (rows - 1) * gap;

  function cellPosition(index) {
    const col = index % columns;
    const row = Math.floor(index / columns);
    return {
      x: padding + col * (cellSize + gap),
      y: padding + headerHeight + row * (cellSize + gap),
      row,
      col,
    };
  }

  const headerMarkup = model.residueHeaders.map((residue, index) => {
    const x = padding + index * (cellSize + gap) + cellSize / 2;
    return `<text class="viz-header-label" x="${x}" y="${padding + 10}">${residue}</text>`;
  }).join('');

  const bridgeMarkup = model.sequences.map((sequence) => {
    const left = cellPosition(sequence.leftIndex);
    return `<rect class="viz-bridge" x="${left.x - 3}" y="${left.y - 4}" width="${cellSize * 3 + gap * 2 + 6}" height="${cellSize + 8}" rx="${Math.floor(cellSize / 2)}"></rect>`;
  }).join('');

  const cellMarkup = model.placements.map(({ row, layoutIndex }) => {
    const position = cellPosition(layoutIndex);
    const kind = getVisualizationKind(row);
    const factorClass = model.isFactors ? getFactorBand(row) : null;
    const labelTone = kind === 'composite' || kind === 'unit' ? 'dark' : 'light';
    const selectedClass = state.selectedVisualNumber === row.number ? ' selected' : '';
    const residueClass = model.isMod6 ? ` residue-${row.number % 6}` : '';
    const modClass = hasActiveModFilter() && state.modBase ? (state.modResidues.includes(getNormalizedResidue(row.number, state.modBase)) ? ' mod-match' : ' mod-muted') : '';
    return `
      <g class="viz-cell-group kind-${kind}${selectedClass}${modClass}" data-number-cell="${row.number}" role="button" tabindex="0" aria-label="Inspect ${row.number}">
        <title>${row.number}: ${getVisualizationLabel(row)}${factorClass ? `, ${getFactorBandLabel(row)}` : ''}</title>
        <rect class="viz-cell ${kind}${residueClass}${factorClass ? ` ${factorClass}` : ''}" x="${position.x}" y="${position.y}" width="${cellSize}" height="${cellSize}" rx="${Math.max(8, Math.floor(cellSize / 3))}"></rect>
        <text class="viz-cell-label ${labelTone} kind-${kind}" x="${position.x + cellSize / 2}" y="${position.y + cellSize / 2 + 0.5}">${row.number}</text>
      </g>
    `;
  }).join('');

  const svgModeClass = `${model.isMod6 ? ' mode-mod6' : model.isFactors ? ' mode-factors' : model.isCenters ? ' mode-centers' : ''}${hasActiveModFilter() ? ' mod-filter-active' : ''}`;
  visualizationStage.innerHTML = `
    <svg class="visualization-svg${svgModeClass}" viewBox="0 0 ${svgWidth} ${svgHeight}" role="img" aria-label="Twin prime visualization for ${model.pageStartNumber} to ${model.pageEndNumber}">
      ${headerMarkup}
      ${bridgeMarkup}
      ${cellMarkup}
    </svg>
  `;

  if (visualizationPagination) {
    visualizationPagination.innerHTML = `
      <div class="lab-pagination-status">Page ${model.currentPage + 1} of ${model.pageCount} | ${model.pageStartNumber}-${model.pageEndNumber}</div>
      <div class="lab-pagination-actions">
        <button type="button" class="lab-page-button" data-page-action="prev" ${model.currentPage === 0 ? 'disabled' : ''}>Previous</button>
        <button type="button" class="lab-page-button" data-page-action="next" ${model.currentPage >= model.pageCount - 1 ? 'disabled' : ''}>Next</button>
      </div>
    `;
    visualizationPagination.querySelector('[data-page-action="prev"]')?.addEventListener('click', () => {
      if (state.visualPage > 0) {
        state.visualPage -= 1;
        renderExplorerVisualization(analysis);
      }
    });
    visualizationPagination.querySelector('[data-page-action="next"]')?.addEventListener('click', () => {
      if (state.visualPage < model.pageCount - 1) {
        state.visualPage += 1;
        renderExplorerVisualization(analysis);
      }
    });
  }

  const cellGroups = Array.from(visualizationStage.querySelectorAll('[data-number-cell]'));
  cellGroups.forEach((group) => {
    const number = Number(group.getAttribute('data-number-cell'));
    group.addEventListener('mouseenter', () => {
      state.visualHoverNumber = number;
      renderVisualizationContext(analysis);
    });
    group.addEventListener('click', () => {
      state.selectedVisualNumber = state.selectedVisualNumber === number ? null : number;
      syncVisualizationSelectionStyles();
      renderVisualizationContext(analysis);
    });
    group.addEventListener('keydown', (event) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        state.selectedVisualNumber = state.selectedVisualNumber === number ? null : number;
        syncVisualizationSelectionStyles();
        renderVisualizationContext(analysis);
      }
    });
  });
  visualizationStage.onmouseleave = () => {
    state.visualHoverNumber = null;
    renderVisualizationContext(analysis);
  };

  syncVisualizationSelectionStyles();
  if (visualizationRangeLabel) {
    visualizationRangeLabel.textContent = `Range ${analysis.start}-${analysis.limit} | Page ${model.currentPage + 1}/${model.pageCount}`;
  }
  if (visualizationModeNote) {
    const baseNote = state.visualMode === 'mod6'
      ? 'Mod 6 view arranges each page into repeating residue blocks so prime structure stays visible across 24 columns.'
      : state.visualMode === 'factors'
        ? 'Factors view darkens composites as their divisor counts grow, while twin primes and twin centers stay visually distinct.'
        : state.visualMode === 'centers'
          ? 'Twin Centers view pulls the background back so the centers between paired primes become the main landmarks in the field.'
          : 'Standard view keeps each page to 24 columns by 25 rows so prime, twin-prime, and twin-center clusters are easy to scan.';
    visualizationModeNote.textContent = hasActiveModFilter() ? `${baseNote} Active filter: ${getResidueFilterLabel()}.` : baseNote;
  }
  visualizationModeButtons.forEach((button) => {
    const isActive = button.dataset.visualMode === state.visualMode;
    button.classList.toggle('active', isActive);
    button.setAttribute('aria-pressed', String(isActive));
  });
  renderVisualizationContext(analysis);
}

function renderNumberTable(analysis) {
  if (!numberTable) {
    return;
  }
  const filteredRows = getFilteredRows(analysis.number_classifications);
  if (tableStateExplanation) {
    tableStateExplanation.innerHTML = makeExplanationCard(getExplorerTableExplanation(analysis, filteredRows));
  }
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

function renderExplorerSurface(analysis) {
  renderExplorerVisualization(analysis);
  renderNumberTable(analysis);
}

function rerenderExplorerTable() {
  if (state.analysis) {
    renderNumberTable(state.analysis);
  }
}

function tryFetchExplorerRange() {
  if (!startInput || !endInput) {
    return;
  }
  const startValue = Number(startInput.value);
  const endValue = Number(endInput.value);
  const validationMessage = getRangeValidationMessage(startValue, endValue);
  if (validationMessage) {
    showRangeValidationError(validationMessage);
    return;
  }
  state.visualPage = 0;
  fetchAnalysis(startValue, endValue, renderExplorerSurface);
}

function scheduleExplorerRangeUpdate() {
  clearTimeout(explorerRangeTimer);
  explorerRangeTimer = setTimeout(tryFetchExplorerRange, 140);
}

if (form) {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    tryFetchExplorerRange();
  });

  [startInput, endInput].forEach((control) => {
    control?.addEventListener('input', scheduleExplorerRangeUpdate);
    control?.addEventListener('change', tryFetchExplorerRange);
  });

  modBaseInput?.addEventListener('input', () => {
    renderModResidueOptions();
    if (state.analysis) {
      renderExplorerVisualization(state.analysis);
    }
  });
  clearModFilterButton?.addEventListener('click', () => {
    if (modBaseInput) {
      modBaseInput.value = '';
    }
    state.modBase = null;
    state.modResidues = [];
    renderModResidueOptions();
    renderModFilterSummary();
    if (state.analysis) {
      renderExplorerVisualization(state.analysis);
    }
  });
  renderModResidueOptions();
  renderModFilterSummary();

  visualizationModeButtons.forEach((button) => {
    button.addEventListener('click', () => {
      const nextMode = button.dataset.visualMode || 'standard';
      if (state.visualMode !== nextMode) {
        state.visualMode = nextMode;
        if (state.analysis) {
          renderExplorerVisualization(state.analysis);
        }
      }
    });
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

  tryFetchExplorerRange();
}
"""

ANALYSIS_JS = COMMON_ANALYSIS_JS + """
if (form && statusText) {
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(form);
    const start = Number(formData.get('start'));
    const end = Number(formData.get('end'));
    const validationMessage = getRangeValidationMessage(start, end);
    if (validationMessage) {
      showRangeValidationError(validationMessage);
      return;
    }
    fetchAnalysis(start, end);
  });

  const requestedAnalysisTab = getRequestedAnalysisTab();
  if (requestedAnalysisTab) {
    state.activeTab = requestedAnalysisTab;
  }
  const requestedAnalysisRange = getRequestedAnalysisRange();

  tabButtons.forEach((button) => {
    button.addEventListener('click', () => {
      state.activeTab = button.dataset.tab;
      renderAnalysisTabs();
    });
  });

  tabShortcutButtons.forEach((button) => {
    button.addEventListener('click', () => {
      state.activeTab = button.dataset.analysisTarget;
      renderAnalysisTabs();
    });
  });

  const initialStart = requestedAnalysisRange ? requestedAnalysisRange.start : 1;
  const initialEnd = requestedAnalysisRange ? requestedAnalysisRange.end : 100;
  const validationMessage = getRangeValidationMessage(initialStart, initialEnd);
  if (validationMessage) {
    showRangeValidationError(validationMessage);
  } else {
    if (startInput) {
      startInput.value = initialStart;
    }
    if (endInput) {
      endInput.value = initialEnd;
    }
    fetchAnalysis(initialStart, initialEnd);
  }
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
    explore_items = tab.get("explore_next", [])
    explore = ""
    if explore_items:
        explore_rows = "".join(
            """<article class="theory-action-card">
      <div class="theory-action-header">
        <span class="theory-action-kicker">Explore this next</span>
        <span class="theory-destination-badge">{destination}</span>
      </div>
      <h4>{title}</h4>
      <p>{body}</p>
      <p><a class="inline-link" href="{href}">{link_label}</a></p>
    </article>""".format(
                destination=html.escape(item.get("destination", "Next")),
                title=html.escape(item["title"]),
                body=html.escape(item["body"]),
                href=html.escape(item["href"], quote=True),
                link_label=html.escape(item["link_label"]),
            )
            for item in explore_items
        )
        explore = '<section class="theory-block"><h3>Take this into the product</h3><div class="theory-action-grid">{}</div></section>'.format(explore_rows)
    return (
        '<div class="theory-intro-block"><h2>{}</h2><p class="theory-intro">{}</p>{}</div>'.format(label, intro, meta)
        + explore
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


def _glossary_term_id(term: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", term.lower()).strip("-")
    return f"glossary-term-{slug}"


def _render_glossary_main_html(main_html: str) -> str:
    sections_html = []
    for section in GLOSSARY_SECTIONS:
        term_cards = []
        for item in section["terms"]:
            term_id = _glossary_term_id(item["term"])
            theory_link = item.get("theory_link")
            theory_link_html = ""
            if theory_link:
                theory_link_html = '<div class="glossary-term-links"><a class="inline-link" href="{href}">{label}</a></div>'.format(
                    href=html.escape(theory_link["href"], quote=True),
                    label=html.escape(theory_link["label"]),
                )
            term_cards.append(
                '<article id="{term_id}" class="glossary-term-card" data-glossary-term data-term-label="{label}"><h3>{term}</h3><p class="glossary-term-summary">{summary}</p><p class="glossary-term-detail">{detail}</p>{links}</article>'.format(
                    term_id=html.escape(term_id),
                    label=html.escape(item["term"].lower()),
                    term=html.escape(item["term"]),
                    summary=html.escape(item["summary"]),
                    detail=html.escape(item["detail"]),
                    links=theory_link_html,
                )
            )
        sections_html.append(
            '<section class="glossary-section" data-glossary-section><div class="glossary-section-header"><h3>{title}</h3><p>{intro}</p></div><div class="glossary-terms">{terms}</div></section>'.format(
                title=html.escape(section["title"]),
                intro=html.escape(section["intro"]),
                terms="".join(term_cards),
            )
        )
    return main_html.replace(
        '<div id="glossary-sections"></div>',
        '<div id="glossary-sections" class="glossary-sections">{}</div>'.format("".join(sections_html)),
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
  const explore = (tab.explore_next || []).length ? `
    <section class="theory-block">
      <h3>Take this into the product</h3>
      <div class="theory-action-grid">
        ${(tab.explore_next || []).map((item) => `
          <article class="theory-action-card">
            <div class="theory-action-header">
              <span class="theory-action-kicker">Explore this next</span>
              <span class="theory-destination-badge">${item.destination || 'Next'}</span>
            </div>
            <h4>${item.title}</h4>
            <p>${item.body}</p>
            <p><a class="inline-link" href="${item.href}">${item.link_label}</a></p>
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
    ${explore}
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

const glossarySearch = document.getElementById('glossary-search');
const glossarySections = Array.from(document.querySelectorAll('[data-glossary-section]'));
const glossaryTermCards = Array.from(document.querySelectorAll('[data-glossary-term]'));

function applyGlossaryFilter() {
  if (!glossarySearch || !glossaryTermCards.length) {
    return;
  }
  const query = glossarySearch.value.trim().toLowerCase();
  glossaryTermCards.forEach((card) => {
    const text = card.textContent.toLowerCase();
    const label = card.dataset.termLabel || '';
    const visible = !query || text.includes(query) || label.includes(query);
    card.classList.toggle('is-hidden', !visible);
  });
  glossarySections.forEach((section) => {
    const visibleCards = section.querySelectorAll('[data-glossary-term]:not(.is-hidden)').length;
    section.classList.toggle('is-hidden', visibleCards === 0);
  });
}

if (glossarySearch && glossaryTermCards.length) {
  glossarySearch.addEventListener('input', applyGlossaryFilter);
  applyGlossaryFilter();
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
        if item.include_in_nav
    )
    if page.active_route == "theory":
        main_html = _render_theory_main_html(page.main_html)
    elif page.active_route == "glossary":
        main_html = _render_glossary_main_html(page.main_html)
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
      <a class="brand-mark" href="/lab">
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


