from typing import Any

import pytest
import trustme


@pytest.fixture(scope="session")
def ca() -> trustme.CA:
    return trustme.CA()  # with ECDSA


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, Any]) -> dict[str, Any]:
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }
