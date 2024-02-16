import allure
import random
import pytest
from pages.market_page import MarketPage


@pytest.mark.regression
@pytest.mark.usefixtures('login_user')
class TestCheckoutOverviewName:
    @allure.feature("Checkout")
    @allure.story("Order Overview")
    @allure.description("""
                This end-to-end test verifies that added product are displayed on the checkout overview page

                Preconditions:
                - User should be logged in.

                Steps:

                1. Navigate to the product page.
                2. Add n random  desired products to the cart.
                3. Go to chart
                4. Proceed to checkout.
                5.Fill in required information.
                6. Confirm the order
                


                Expected result:
                -  names of added products on the checkout overview page are correct.
            """)

    def test_random_number_products_added_displayed_in_checkout_overview(self, browser):
        n = random.randint(1, 6)
        market_page = MarketPage(browser)
        market_page.add_to_cart(n)
        list_of_chosen_products = market_page.get_list_of_products_added_to_chart(n)
        chart_page = market_page.go_to_cart()
        checkout_page = chart_page.go_to_checkout()
        checkout_page.checkout()
        checkout_overview_page = checkout_page.go_to_checkout_overview_page()
        list_of_products_in_checkout_overview = checkout_overview_page.get_list_of_products_in_checkout_overview_page()
        assert list_of_products_in_checkout_overview == list_of_chosen_products, "names of added products on the checkout overview page are incorrect"

