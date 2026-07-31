import pytest
from playwright.sync_api import Page


@pytest.mark.only_browser("chromium")
def test_visit_example(page: Page, browser_name: str, is_chromium: bool) -> None:
    page.goto("https://example.com")
    # ...
    assert is_chromium
    assert browser_name == "chromium"
