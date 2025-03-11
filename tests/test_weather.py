import pytest
from playwright.sync_api import sync_playwright
import time

def test_weather_above_zero():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        #time.sleep(2)
        try:
            page.wait_for_selector("text=Zaakceptuj wszystko", timeout=10000)
            page.click("text=Zaakceptuj wszystko")
            print("Clicked on the cookie consent button.")
            page.screenshot(path="after_click.png")
        except Exception as e:
            print("Cookie consent button not found or not clickable:", e)
            page.screenshot(path="error.png")
        #time.sleep(5)
        try:
            search_input_xpath = "/html/body/div[1]/div[3]"
            page.wait_for_selector(f"xpath={search_input_xpath}", timeout=10000)
            page.fill(f"xpath={search_input_xpath}", "weather Wroclaw")
            page.press(f"xpath={search_input_xpath}", "Enter")
            page.wait_for_selector("#wob_tm")

            temperature = page.inner_text("#wob_tm")
            assert int(temperature) > 0, f"Expected temperature to be above 0, but got {temperature}"
        except Exception as e:
            print("Error during search or result retrieval:", e)
        finally:
            browser.close()