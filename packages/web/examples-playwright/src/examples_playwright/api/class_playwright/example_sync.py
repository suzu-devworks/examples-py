"""Playwright class(Sync).

References:
    - https://playwright.dev/python/docs/api/class-playwright

Run:

    ```shell
    python ./src/examples_playwright/api/class_playwright/example_sync.py
    ```
"""

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = chromium.launch()
    page = browser.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
