from typing import Any

import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict[str, Any], playwright: Playwright) -> dict[str, Any]:
    """
    For a list of available devices see:
        - https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json
    """  # noqa: E501

    iphone = playwright.devices["iPhone 15 Pro"]
    return {
        **browser_context_args,
        **iphone,
    }
