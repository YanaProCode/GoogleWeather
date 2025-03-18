import pytest
import time
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync
from PO.search import SearchPage
from PO.weather import WeatherPage


def test_weather_above_zero(browser_context):
    page = browser_context.new_page()
    search_page = SearchPage(page)
    weather_page = WeatherPage(page)
    search_page.navigate()
    search_page.search_weather("weather Wroclaw")
    temperature = weather_page.get_temperature()
    assert temperature > 0, f"Expected temperature to be above 0, but got {temperature}"

def test_correct_city_displayed(browser_context):
    page = browser_context.new_page()
    search_page = SearchPage(page)
    weather_page = WeatherPage(page)
    search_page.navigate()
    search_page.search_weather("weather Wroclaw")
    city = weather_page.get_city()
    assert "Wrocław" in city, f"Expected city to be Wroclaw, but got {city}"

def test_forecast_for_multiple_days(browser_context):
    page = browser_context.new_page()
    search_page = SearchPage(page)
    weather_page = WeatherPage(page)
    search_page.navigate()
    search_page.search_weather("weather Wroclaw")
    forecast = weather_page.get_forecast_days()
    assert forecast == 8, f"Expected forecast to be 8 days, but got {forecast}"

def test_weather_icons_displayed(browser_context):
    page = browser_context.new_page()
    search_page = SearchPage(page)
    weather_page = WeatherPage(page)
    search_page.navigate()
    search_page.search_weather("weather Wroclaw")
    icons = weather_page.get_weather_icons()
    assert icons == 8, f"Expected 8 icons, but got {icons}"

