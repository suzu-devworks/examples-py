import ssl
import threading
from collections.abc import Generator
from http.server import HTTPServer, SimpleHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

import pytest
import trustme

# CERTFILE = "/etc/ssl/local/localhost.crt"
# KEYFILE = "/etc/ssl/local/localhost.key"


@pytest.fixture()
def http_server(ca: trustme.CA) -> Generator[HTTPServer, Any, None]:
    host, port = "127.0.0.1", 58001

    server = ThreadingHTTPServer((host, port), SimpleHTTPRequestHandler)

    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    localhost_cert = ca.issue_cert("localhost")
    localhost_cert.configure_cert(context)
    # context.load_cert_chain(CERTFILE, KEYFILE)
    server.socket = context.wrap_socket(server.socket)

    thread = threading.Thread(None, server.serve_forever)
    thread.start()

    yield server

    server.shutdown()
    thread.join()
