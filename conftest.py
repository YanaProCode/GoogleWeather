import pytest
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        stealth_sync(page)
        yield context
        browser.close()