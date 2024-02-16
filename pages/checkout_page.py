import allure

from pages.base_page import Base
from locators.checkout_page_locator import Checkout
from playwright.sync_api import Page

from pages.checkout_overview_page import CheckoutOverviewPage


class CheckoutPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step('Fill checkout form')
    def checkout(self):
        with allure.step('Fill in first name field'):
            self.input(Checkout.FIRST_NAME, "Ivan")
        with allure.step('Fill in last name field'):
            self.input(Checkout.LAST_NAME, "Ivanov")
        with allure.step('Fill in zip field'):
            self.input(Checkout.ZIP, "123456")

    @allure.step('Click button checkout')
    def go_to_checkout_overview_page(self):
        self.click(Checkout.CNT_BTN)
        return CheckoutOverviewPage(self.page)
