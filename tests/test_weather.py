import pytest
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
import time

def test_weather_above_zero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        stealth_sync(page)
        page.goto("https://www.google.com/")
        time.sleep(2)

        try:
            search_input_xpath = "//*[@id=\"APjFqb\"]"
            page.wait_for_selector(f"xpath={search_input_xpath}", timeout=10000)
            page.fill(search_input_xpath, "weather Wroclaw")
            time.sleep(2)
            page.press(search_input_xpath, "Enter")
            time.sleep(2)
            page.wait_for_selector("#wob_tm")
            time.sleep(2)

            temperature = page.inner_text("#wob_tm")
            assert int(temperature) > 0, f"Expected temperature to be above 0, but got {temperature}"
        except Exception as e:
            print("Error during search or result retrieval:", e)
        finally:
            browser.close()