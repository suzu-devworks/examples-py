"""Playwright class(Async).

References:
    - https://playwright.dev/python/docs/api/class-playwright

Run:

    ```shell
    python ./src/examples_playwright/api/class_playwright/example_async.py
    ```
"""

import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    chromium = playwright.chromium  # or "firefox" or "webkit".
    browser = await chromium.launch()
    page = await browser.new_page()
    await page.goto("http://example.com")
    # other actions...
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
