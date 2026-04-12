"""Minimal web application for exploring twin-prime analysis."""

from __future__ import annotations

import importlib
import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import parse_qs, urlparse

from .web_runtime import WebRuntime


class DualPrimeThreadingHTTPServer(ThreadingHTTPServer):
    """Threading HTTP server that carries local development settings."""

    dev_mode: bool


def _load_web_runtime_module(dev_mode: bool = False) -> Any:
    runtime_module = importlib.import_module("dual_prime_explorer.web_runtime")
    if dev_mode:
        runtime_module = importlib.reload(runtime_module)
    return runtime_module


def build_analysis_payload(
    end: int,
    density_window: int = 50,
    *,
    start: int = 1,
    dev_mode: bool = False,
) -> dict[str, Any]:
    """Return a JSON-ready payload for the web UI."""
    runtime_module = _load_web_runtime_module(dev_mode)
    return runtime_module.build_analysis_payload(
        end,
        density_window=density_window,
        start=start,
        dev_mode=dev_mode,
    )


def load_web_runtime(dev_mode: bool = False) -> WebRuntime:
    """Load the current web pages and static assets."""
    runtime_module = _load_web_runtime_module(dev_mode)
    return runtime_module.load_web_runtime(dev_mode=dev_mode)


class DualPrimeRequestHandler(BaseHTTPRequestHandler):
    """Serve the twin-prime browser UI and JSON API."""

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        runtime = load_web_runtime(self._is_dev_mode())

        if parsed.path in runtime["page_by_route"]:
            self._send_response(runtime["page_registry"][parsed.path], content_type="text/html; charset=utf-8")
            return
        if parsed.path == "/styles.css":
            self._send_response(runtime["app_css"], content_type="text/css; charset=utf-8")
            return
        if parsed.path == "/ads.txt":
            self._send_response(runtime["ads_txt"], content_type="text/plain; charset=utf-8")
            return
        if parsed.path == "/robots.txt":
            self._send_response(runtime["robots_txt"], content_type="text/plain; charset=utf-8")
            return
        if parsed.path == "/sitemap.xml":
            self._send_response(runtime["sitemap_xml"], content_type="application/xml; charset=utf-8")
            return
        if parsed.path == "/googlee310ecf193a6916e.html":
            self._send_response(runtime["google_site_verification_html"], content_type="text/html; charset=utf-8")
            return
        if parsed.path == "/favicon.ico":
            self.send_response(HTTPStatus.NO_CONTENT)
            self._set_cache_headers()
            self.end_headers()
            return
        if parsed.path == "/explorer.js":
            self._send_response(runtime["explorer_js"], content_type="application/javascript; charset=utf-8")
            return
        if parsed.path == "/analysis.js":
            self._send_response(runtime["analysis_js"], content_type="application/javascript; charset=utf-8")
            return
        if parsed.path == "/theory.js":
            self._send_response(runtime["theory_js"], content_type="application/javascript; charset=utf-8")
            return
        if parsed.path == "/experiments.js":
            self._send_response(runtime["experiments_js"], content_type="application/javascript; charset=utf-8")
            return
        if parsed.path == "/api/analyze":
            self._handle_analyze_request(parse_qs(parsed.query))
            return
        self._send_response(runtime["not_found_html"], content_type="text/html; charset=utf-8", status=HTTPStatus.NOT_FOUND)

    def log_message(self, format: str, *args: object) -> None:  # noqa: A003
        return

    def _handle_analyze_request(self, query: dict[str, list[str]]) -> None:
        try:
            start = int(query.get("start", ["1"])[0])
            end = int(query.get("end", query.get("limit", ["100"]))[0])
            window = int(query.get("window", ["50"])[0])
            if window < 0:
                raise ValueError("window must be non-negative")
            payload = build_analysis_payload(end, density_window=window, start=start, dev_mode=self._is_dev_mode())
        except ValueError as error:
            self._send_json({"error": str(error)}, status=HTTPStatus.BAD_REQUEST)
            return

        self._send_json(payload)

    def _is_dev_mode(self) -> bool:
        return bool(getattr(self.server, "dev_mode", False))

    def _set_cache_headers(self) -> None:
        if not self._is_dev_mode():
            return
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")

    def _send_json(self, payload: dict[str, Any], status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self._set_cache_headers()
            self.end_headers()
            self.wfile.write(body)
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
            return

    def _send_response(self, body: str, *, content_type: str, status: HTTPStatus = HTTPStatus.OK) -> None:
        encoded = body.encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(encoded)))
            self._set_cache_headers()
            self.end_headers()
            self.wfile.write(encoded)
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
            return

    def _redirect(self, location: str, *, status: HTTPStatus = HTTPStatus.PERMANENT_REDIRECT) -> None:
        try:
            self.send_response(status)
            self.send_header("Location", location)
            self._set_cache_headers()
            self.end_headers()
        except (BrokenPipeError, ConnectionAbortedError, ConnectionResetError):
            return


def run_server(host: str = "127.0.0.1", port: int = 8000, dev_mode: bool = False) -> None:
    """Run the built-in twin-prime exploration web server."""
    server = DualPrimeThreadingHTTPServer((host, port), DualPrimeRequestHandler)
    server.dev_mode = dev_mode
    mode_label = " with live UI reloads" if dev_mode else ""
    print(f"Twin Prime Explorer web app running at http://{host}:{port}/{mode_label}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
