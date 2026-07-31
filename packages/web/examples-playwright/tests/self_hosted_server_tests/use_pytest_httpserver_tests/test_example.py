from playwright.sync_api import Page, expect
from pytest_httpserver import HTTPServer


def test_use_https_server(page: Page, httpserver: HTTPServer) -> None:
    # goto self signed site
    assert httpserver.is_running()

    page.goto("https://127.0.0.1:58882/")
    expect(page).to_have_url("https://127.0.0.1:58882/")
