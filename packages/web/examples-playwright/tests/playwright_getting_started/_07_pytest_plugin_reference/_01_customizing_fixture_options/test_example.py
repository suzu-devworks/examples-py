import pytest
from playwright.sync_api import Page


@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")
def test_browser_context_args(page: Page) -> None:
    """Override browser context args."""
    # assert page.evaluate("window.navigator.userAgent") == "Europe/Berlin"
    # assert page.evaluate("window.navigator.languages") == ["de-DE"]
    assert page.evaluate("window.navigator.languages") == ["en-GB"]
    assert page.evaluate("new Date().getTimezoneOffset()") == -60


@pytest.mark.browser_context_args(timezone_id="Asia/Tokyo", locale="ja-JP")
def test_browser_context_args_ja(page: Page) -> None:
    """Override browser context args to ja-JP."""
    assert page.evaluate("window.navigator.languages") == ["ja-JP"]
    assert page.evaluate("new Date().getTimezoneOffset()") == -540
