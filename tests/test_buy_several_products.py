import allure
import random
import pytest
from locators.check_overview_page_locator import CheckOverview
from pages.market_page import MarketPage
from utils.api import extract_number


@pytest.mark.regression
@pytest.mark.usefixtures('login_user')
class TestCheckoutOverviewTotalSum:
    @allure.feature("Checkout")
    @allure.story("Order Overview")
    @allure.description("""
            This end-to-end test verifies the correctness of tax calculation, item count, and total amount on the checkout overview page

            Preconditions:
            - User should be logged in.

            Steps:

            1. Navigate to the product page.
            2. Add n random  desired products to the cart.
            3. Go to chart
            4. Proceed to checkout.
            5.Fill in required information.
            6. Confirm the order
            7. Count sum of all products and tax.
            

            Expected result:
            -  total amount on the checkout overview page is correct.
        """)
    def test_sum_random_number_products_and_tax_equal_total_sum(self, browser):
        n = random.randint(1, 6)
        market_page = MarketPage(browser)
        market_page.add_to_cart(n)
        chart_page = market_page.go_to_cart()
        checkout_page = chart_page.go_to_checkout()
        checkout_page.checkout()
        checkout_overview_page = checkout_page.go_to_checkout_overview_page()
        sum_all_products_in_chart_with_tax = checkout_overview_page.count_sum_of_purchase_with_tax()
        total_price = extract_number(checkout_overview_page.get_text(CheckOverview.TOTAL_WITH_TAX))
        assert sum_all_products_in_chart_with_tax == total_price, "total sum incorrect"
