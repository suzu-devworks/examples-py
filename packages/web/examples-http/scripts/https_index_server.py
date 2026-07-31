#!/usr/bin/env python
"""Tiny HTTPS index server using `http.server`."""

import argparse
import contextlib
import ssl
from collections.abc import Callable
from http.server import HTTPServer, SimpleHTTPRequestHandler
from socketserver import BaseRequestHandler
from typing import Any


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Tiny HTTPS server")
    p.add_argument("port", type=int, nargs="?", default=8443, help="The server listens to port")
    p.add_argument("-b", "--bind", default="127.0.0.1", help="Address to bind")
    p.add_argument("--tls-cert", default="/etc/ssl/local/localhost.crt", help="TLS certificate file")
    p.add_argument("--tls-key", default="/etc/ssl/local/localhost.key", help="Private key file")
    return p.parse_args()


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

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(cert_file, key_file)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    # context.maximum_version = ssl.TLSVersion.TLSv1_3
    # context.set_alpn_protocols(["h2", "http/1.1"])  # HTTP/2.0 505 ?

    # ciphers = context.get_ciphers()
    # for cipher in ciphers:
    #     print("  enabled:", cipher["description"])

    handler = SimpleHTTPRequestHandler
    run(host, port, context, handler)
