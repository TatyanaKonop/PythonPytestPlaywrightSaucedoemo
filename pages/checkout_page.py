import allure

from pages.base_page import Base
from locators.checkout_page_locator import Checkout

from data.assertions import Assertions
from playwright.sync_api import Page


class CheckoutPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step('Fill checkout form')
    def checkout(self):
        self.input(Checkout.FIRST_NAME, "Ivan")
        self.input(Checkout.LAST_NAME, "Ivanov")
        self.input(Checkout.ZIP, "123456")
        self.click(Checkout.CNT_BTN)

