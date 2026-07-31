from playwright.sync_api import Page


def test_viewport_size(page: Page) -> None:
    # with scrollbar
    assert page.evaluate("window.innerWidth") == 1920
    assert page.evaluate("window.innerHeight") == 1080
    # without scrollbar
    assert page.evaluate("document.documentElement.clientWidth") == 1920
    assert page.evaluate("document.documentElement.clientHeight") == 1080
