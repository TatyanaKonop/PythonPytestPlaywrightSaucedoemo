import allure
from locators.complete_page_locator import Compete
from pages.market_page import MarketPage
import pytest
from utils.json_parser import JsonParser


@pytest.mark.regression
@pytest.mark.usefixtures('login_user')
class TestBuyProduct:

    @allure.feature("Purchase")
    @allure.story("Buy Product")
    @allure.description("""
        This end-to-end test verifies the purchase process on the website.

        Preconditions:
        - User should be logged in.

        Steps:
        
        1. Navigate to the product page.
        2. Add the desired product to the cart.
        3. Go to chart
        4. Proceed to checkout.
        5. Fill in required information.
        6. Confirm the order.
        7. Finish purchase

        Expected result:
        - User should receive a confirmation message.
    """)


    def test_buy_product(self, browser):
        market_page = MarketPage(browser)
        market_page.add_to_cart()
        chart_page = market_page.go_to_cart()
        checkout_page = chart_page.go_to_checkout()
        checkout_page.checkout()
        checkout_overview_page = checkout_page.go_to_checkout_overview_page()
        complete_page = checkout_overview_page.go_to_complete_page()
        txt_message_success = JsonParser("tests_data.json").read_from_json()['complete_page_data']['message_success_purchase']
        assert txt_message_success == complete_page.get_text(Compete.FINAL_TEXT), "there is no successful message"

