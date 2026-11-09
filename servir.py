#!/usr/bin/env python3
"""Sirve el visor y lo abre en el navegador.

Uso, desde esta carpeta:

    python3 servir.py
"""

from __future__ import annotations

import argparse
import webbrowser
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Abre el visor de comparación OCR en el navegador."
    )
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Solo sirve la página, sin abrir el navegador.",
    )
    args = parser.parse_args()

    handler = partial(SimpleHTTPRequestHandler, directory=str(ROOT))
    try:
        server = ThreadingHTTPServer(("127.0.0.1", args.port), handler)
    except OSError as exc:
        raise SystemExit(
            f"No pude escuchar en 127.0.0.1:{args.port} ({exc}). "
            "Prueba con --port 8766."
        ) from exc

    url = f"http://127.0.0.1:{args.port}/review.html"
    print(f"Visor en {url}")
    print("Ctrl+C para detenerlo.")
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDetenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
