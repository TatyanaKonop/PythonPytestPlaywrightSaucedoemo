import allure
import pytest
from data.environment import host
from pages.login_page import Main



@pytest.mark.smoke
class TestLogin:
    @allure.feature("Login")
    @allure.story("Login")
    @allure.description("""
           This smoke test verifies the successful login

           Steps:

           1. Input correct username.
           2. Input correct password.
           3. Confirm login.

           Expected result:
           - URl match "https://www.saucedemo.com/inventory.html".
       """)
    def test_user_login(self, browser):
        URI = "inventory.html"
        login_page = Main(browser)
        login_page.user_login()
        assert login_page.current_url() == f"{host.get_base_url()}{URI}", "Wrong URL"


