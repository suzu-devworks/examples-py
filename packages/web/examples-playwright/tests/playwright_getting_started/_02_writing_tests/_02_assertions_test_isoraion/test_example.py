from playwright.sync_api import Page, expect


def test_example_test(page: Page) -> None:
    # Pages are isolated between tests due to the Browser Context.
    expect(page).to_have_url("about:blank")

    page.goto("https://playwright.dev/")
    expect(page).to_have_url("https://playwright.dev/")

    pass
    # "page" belongs to an isolated BrowserContext, created for this specific test.


def test_another_test(page: Page) -> None:
    # Pages are isolated between tests due to the Browser Context.
    expect(page).to_have_url("about:blank")

    page.goto("https://playwright.dev/python/docs/writing-tests")
    expect(page).to_have_url("https://playwright.dev/python/docs/writing-tests")

    pass
    # "page" in this second test is completely isolated from the first test.
