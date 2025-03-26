from playwright.sync_api import Page

class WeatherPage:
    def __init__(self, page: Page):
        self.page = page
        self.temperature_selector = "#wob_tm"
        self.city_selector = ".BBwThe"
        self.forecast_selector = "#wob_dp"
        self.weather_icon_selector = "#wob_dp .wob_df"

    def get_temperature(self) -> int:
        self.page.wait_for_selector(self.temperature_selector)
        return int(self.page.inner_text(self.temperature_selector))

    def get_city(self) -> str:
        return self.page.wait_for_selector(self.city_selector).inner_text()

    def get_forecast_days(self) -> int:
        self.page.wait_for_selector(self.forecast_selector)
        return len(self.page.query_selector_all(f"{self.forecast_selector} .wob_df"))

    def get_weather_icons(self) -> int:
        self.page.wait_for_selector(self.weather_icon_selector)
        return len(self.page.query_selector_all(self.weather_icon_selector))