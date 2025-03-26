from playwright.sync_api import Page
from playwright_stealth import stealth_sync

class SearchPage:
    def __init__(self, page:Page):
        self.page = page
        self.search_input_xpath = "//*[@id=\"APjFqb\"]"

    def navigate(self):
        self.page.goto("https://www.google.com/")
        return self


    def search_weather(self, location: str):
        self.page.wait_for_selector(self.search_input_xpath, timeout=10000)
        self.page.fill(self.search_input_xpath, location)
        self.page.press(self.search_input_xpath, "Enter")
        return self
