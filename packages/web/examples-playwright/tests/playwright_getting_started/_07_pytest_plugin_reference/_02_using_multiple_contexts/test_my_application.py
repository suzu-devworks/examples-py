from playwright.sync_api import Page, expect
from pytest_playwright.pytest_playwright import CreateContextCallback


def test_foo(page: Page, new_context: CreateContextCallback) -> None:
    # page.goto("https://example.com")
    page.goto("https://playwright.dev/")

    context = new_context()
    page2 = context.new_page()

    # page and page2 are in different contexts
    expect(page).to_have_url("https://playwright.dev/")
    expect(page2).to_have_url("about:blank")
