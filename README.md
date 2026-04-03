# Dual Prime Explorer

Dual Prime Explorer is a mathematical exploration engine for studying twin primes through both computation and mathematical context.

Twin primes are pairs of primes that differ by 2, such as `(3, 5)`, `(5, 7)`, and `(11, 13)`.

## Project Goals

- Generate primes and twin-prime pairs reliably.
- Analyze modular structure and known residue patterns.
- Measure gaps, clustering, and local density behavior.
- Compare factorization properties of twin-prime centers against other even numbers.
- Contrast observed counts with simple heuristic expectations.
- Pair computation with an educational theory experience in the web app.
- Keep the web app ready for additional pages as the product grows.

## Core API

The package currently exposes:

- `primes_up_to(limit)`
- `twin_primes_up_to(limit)`
- `analyze_primes_up_to(limit, density_window=50, expected_sample_points=None)`
- `build_analysis_payload(limit, density_window=50)`
- `load_web_runtime(dev_mode=False)`
- `run_server(host="127.0.0.1", port=8000, dev_mode=False)`

## Web App

Launch the browser UI from the project root:

```powershell
$env:PYTHONPATH='src'
python -m dual_prime_explorer --serve
```

Then open:

```text
http://127.0.0.1:8000/lab
```

### Local Development Mode

For UI work, you can run the server in development mode so HTML, CSS, JavaScript, and theory-content edits are picked up on the next browser refresh without restarting the Python process:

```powershell
$env:PYTHONPATH='src'
python -m dual_prime_explorer --serve --dev
```

In `--dev` mode, the server reloads the web UI modules on each request and sends `no-store` cache headers so the browser does not hold onto stale assets.

### Web Routes

The app now uses real top-level routes:

- `/lab` for the visualization-first home experience
- `/explorer` for range setup, summary, and number-by-number classification
- `/analysis` for modular, gap, factorization, density, and expected-count views
- `/theory` for the educational/theory section
- `/glossary` for shared mathematical and product vocabulary
- `/experiments` as a future-facing placeholder route

### Web Structure

The web layer is split so additional pages are easier to add:

- `web.py`: HTTP server and routing
- `web_pages.py`: page definitions and route registry
- `web_assets.py`: shared CSS, JavaScript, and HTML rendering helpers
- `web_content.py`: structured educational content for the Theory page

### Theory Page

The Theory route contains tabbed reference material for:

- History
- Approaches
- Current Progress
- Why It's Hard

Theory now also links back into the interactive product through targeted Lab, Explorer, and Analysis entry points, while the Glossary provides lightweight return links into selected Theory topics.

The theory tabs support direct linking by URL hash, for example:

```text
http://127.0.0.1:8000/theory#approaches
```
