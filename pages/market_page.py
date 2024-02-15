import allure

from pages.base_page import Base
from locators.market_page_locator import Market
from data.assertions import Assertions
from playwright.sync_api import Page


class MarketPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step('Add product to chart')
    def add_to_cart(self):
        self.click_element_by_index(Market.ADD_TO_CART, 0) #кликаем по индексу, 0 это значит, что кликаем по первой карточке
        self.click(Market.FOLLOW_TO_BASKET)


