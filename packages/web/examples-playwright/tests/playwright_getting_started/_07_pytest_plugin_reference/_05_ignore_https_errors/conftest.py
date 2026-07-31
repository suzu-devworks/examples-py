import ssl
from typing import Any

import pytest
import trustme


@pytest.fixture(scope="session")
def ca() -> trustme.CA:
    return trustme.CA()


@pytest.fixture(scope="session")
def httpserver_ssl_context(ca: trustme.CA) -> ssl.SSLContext:
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.minimum_version = ssl.TLSVersion.TLSv1_2
    context.maximum_version = ssl.TLSVersion.TLSv1_3

    localhost_cert = ca.issue_cert("localhost")
    localhost_cert.configure_cert(context)

    return context


@pytest.fixture(scope="session")
def httpserver_listen_address() -> tuple[str, int]:
    return ("127.0.0.1", 8888)


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, Any]) -> dict[str, Any]:
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }
