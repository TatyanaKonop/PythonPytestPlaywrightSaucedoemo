import allure

from locators.check_overview_page_locator import CheckOverview
from pages.base_page import Base
from locators.market_page_locator import Market
from data.assertions import Assertions
from playwright.sync_api import Page

from pages.chart_page import ChartPage


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)



    @allure.step('Add n number of unrepeated products to chart ')
    def add_to_cart(self, n=1,
                    index=0):  # n - number of products, index - index product , if index is 0 it's mean that click first card
        if n == 1:
            self.click_element_by_index(Market.ADD_TO_CART,
                                        index)
        else:
            for i in range(n):
                self.click_element_by_index(Market.ADD_TO_CART,
                                            index=i)

    @allure.step('Click button chart')
    def go_to_cart(self):
        self.click(Market.FOLLOW_TO_BASKET)
        return ChartPage(self.page)

    def get_list_of_products_added_to_chart(self, n=0):
        return self.list_names_for_defined_number_elements(Market.NAME_PRODUCT, n)
