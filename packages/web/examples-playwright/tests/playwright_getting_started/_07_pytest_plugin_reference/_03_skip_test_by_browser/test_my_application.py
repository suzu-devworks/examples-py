import pytest
from playwright.sync_api import Page


@pytest.mark.skip_browser("firefox")
def test_visit_example(page: Page, browser_name: str, is_firefox: bool) -> None:
    # page.goto("https://example.com")
    # ...
    assert not is_firefox
    assert browser_name != "firefox"
