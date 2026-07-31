from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

import pytest
from playwright.sync_api import Page


@pytest.mark.browser_context_args(timezone_id="Europe/Berlin", locale="en-GB")
def test_browser_context_args(page: Page, request: pytest.FixtureRequest) -> None:
    """Override browser context args."""
    # 1. Dynamically get timezone_id from kwargs passed to decorator
    marker = request.node.get_closest_marker("browser_context_args")
    timezone_id = marker.kwargs.get("timezone_id")

    # 2. Calculate the current offset using the obtained timezone_id
    now = datetime.now(ZoneInfo(timezone_id))
    offset = now.utcoffset()
    seconds = offset.total_seconds() if offset is not None else 0
    expected_offset = -int(seconds / 60)
    print(f"Current timezone offset for {timezone_id}: {expected_offset} minutes")

    # 3. Adjust for daylight saving time if applicable
    is_dst = now.dst() != timedelta(0)
    expected_offset = -120 if is_dst else -60  # Adjust for daylight saving time
    print(f"Adjusted timezone offset for {timezone_id}: {expected_offset} minutes")

    # assert page.evaluate("window.navigator.userAgent") == "Europe/Berlin"
    # assert page.evaluate("window.navigator.languages") == ["de-DE"]
    assert page.evaluate("window.navigator.languages") == ["en-GB"]
    assert page.evaluate("new Date().getTimezoneOffset()") == expected_offset


@pytest.mark.browser_context_args(timezone_id="Asia/Tokyo", locale="ja-JP")
def test_browser_context_args_ja(page: Page) -> None:
    """Override browser context args to ja-JP."""
    assert page.evaluate("window.navigator.languages") == ["ja-JP"]
    assert page.evaluate("new Date().getTimezoneOffset()") == -540
