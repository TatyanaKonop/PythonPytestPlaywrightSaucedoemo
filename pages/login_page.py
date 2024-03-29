import allure

from pages.base_page import Base
from data.constants import Constants
from locators.login_page_locator import Auth
from playwright.sync_api import Page


class Main(Base):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

    @allure.step("Login user")
    def user_login(self):
        self.open('')
        self.input(Auth.USERNAME_INPUT, Constants.login)
        self.input(Auth.PASSWORD_INPUT, Constants.password)
        self.click(Auth.LOGIN_BTN)
