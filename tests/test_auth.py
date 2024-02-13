import pytest
from pages.login_page import Main
from data.assertions import Assertions
from tests.base_test import BaseTest


@pytest.mark.smoke
class TestLogin(BaseTest):
    def test_user_login(self):
        self.pages['login_page'].user_login()
        self.pages['login_page'].assertion.check_URL("inventory.html", "Wrong URL")
