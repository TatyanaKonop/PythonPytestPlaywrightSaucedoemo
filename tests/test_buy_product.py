import allure
import pytest

from fixtures import page
from locators.complete_page_locator import Compete
from tests.base_test import BaseTest
import pytest


@allure.description("Test e2e")
@allure.title("Test successful purchase of one product")
@pytest.mark.regression
@pytest.mark.usefixtures('login_user')
class TestBuyProduct(BaseTest):
    def test_buy_product(self):
        self.pages['market_page'].add_to_cart()
        self.pages['chart_page'].go_to_checkout()
        self.pages['checkout_page'].checkout()
        self.pages['checkout_overview_page'].finish_purchase()
        txt_message_success = self.json_reader.read_from_json()['complete-page_data']['message_success_purchase']
        self.pages['complete_page'].assertions.have_text(Compete.FINAL_TEXT, txt_message_success, "no")