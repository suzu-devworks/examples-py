import re

from playwright.sync_api import Page


def test_emulation_info(page: Page) -> None:
    assert re.search(
        r"Mozilla/5.0 \(iPhone; CPU iPhone OS 17_5 like Mac OS X\) AppleWebKit\/605\.1\.15 \(KHTML, like Gecko\).*",
        page.evaluate("window.navigator.userAgent"),
    )

    assert page.evaluate("window.screen.width") == 393
    assert page.evaluate("window.screen.height") == 659
