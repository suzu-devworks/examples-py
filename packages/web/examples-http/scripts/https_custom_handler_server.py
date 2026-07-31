#!/usr/bin/env python
"""Tiny HTTPS custom handler server using `http.server`."""

import argparse
import contextlib
import ssl
from collections.abc import Callable
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import BaseRequestHandler
from typing import Any


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Tiny HTTPS custom handler server")
    p.add_argument("port", type=int, nargs="?", default=8443, help="The server listens to port")
    p.add_argument("-b", "--bind", default="127.0.0.1", help="Address to bind")
    p.add_argument("--tls-cert", default="/etc/ssl/local/localhost.crt", help="TLS certificate file")
    p.add_argument("--tls-key", default="/etc/ssl/local/localhost.key", help="Private key file")
    return p.parse_args()


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html_context = (
            '<html lang="ja">'
            '<meta charset="UTF-8">'
            '<form method="POST" action="/"><input type="submit" value="送信"></form>'
            "</html>"
        )
        self.wfile.write(html_context.encode())

    def do_POST(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        html_context = "送信完了"
        self.wfile.write(html_context.encode())


def run(
    host: str, port: int, context: ssl.SSLContext, handler: Callable[[Any, Any, HTTPServer], BaseRequestHandler]
) -> None:
    with HTTPServer((host, port), handler) as server:
        server.socket = context.wrap_socket(server.socket)

        print(f"Listening to port: {port} (https://{host}:{port})")

        with contextlib.suppress(KeyboardInterrupt):
            server.serve_forever()

        server.server_close()
        print("Server stopped")


if __name__ == "__main__":
    args = parse_args()
    host = args.bind
    port = args.port
    cert_file = args.tls_cert
    key_file = args.tls_key

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3
    context.load_cert_chain(cert_file, key_file)

    handler = CustomHTTPRequestHandler
    run(host, port, context, handler)
