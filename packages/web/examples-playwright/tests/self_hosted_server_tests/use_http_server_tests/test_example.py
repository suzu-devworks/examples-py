from http.server import HTTPServer

from playwright.sync_api import Page, expect


def test_use_https_server(page: Page, http_server: HTTPServer) -> None:
    # goto self signed site
    # assert http_server

    page.goto("https://127.0.0.1:58001/")
    expect(page).to_have_url("https://127.0.0.1:58001/")
