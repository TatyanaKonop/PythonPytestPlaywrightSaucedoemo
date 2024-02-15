import allure

from pages.base_page import Base
from locators.check_overview_page_locator import CheckOverview
from data.assertions import Assertions
from playwright.sync_api import Page


class CheckoutOverviewPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step('Click finish button')
    def finish_purchase(self):
        self.click(CheckOverview.FINISH_BTN)
