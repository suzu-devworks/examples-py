from collections.abc import Generator
from typing import Any

import pytest
from playwright.sync_api import Page, expect


@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(page: Page) -> Generator[None, Any, None]:
    print("beforeEach")

    # Go to the starting url before each test.
    page.goto("https://playwright.dev/")
    yield

    print("afterEach")


def test_main_navigation(page: Page) -> None:
    # Assertions use the expect API.
    expect(page).to_have_url("https://playwright.dev/")
