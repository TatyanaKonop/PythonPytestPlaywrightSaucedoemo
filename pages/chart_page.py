import allure

from pages.base_page import Base
from locators.chart_page_locator import Chart
from data.assertions import Assertions
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage


class ChartPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step('Click checkout button')
    def go_to_checkout(self):
        self.click(Chart.CHECKOUT_BTN)
        return CheckoutPage(self.page)

