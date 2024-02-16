import allure

from pages.base_page import Base
from locators.check_overview_page_locator import CheckOverview
from playwright.sync_api import Page

from pages.complete_page import CompletePage
from utils.api import find_sum_elements, extract_number


class CheckoutOverviewPage(Base):
    def __init__(self, page: Page):
        super().__init__(page)

    @allure.step('Click finish button')
    def go_to_complete_page(self):
        self.click(CheckOverview.FINISH_BTN)
        return CompletePage(self.page)

    @allure.step('Count sum of purchase with tax')
    def count_sum_of_purchase_with_tax(self):
        sum_items = find_sum_elements(self.get_several_elements(CheckOverview.PRICE_FOR_ONE_ITEM))
        tax = extract_number(self.get_text(CheckOverview.TAXES))
        sum_items_with_tax = round((sum_items + tax), 2)
        return sum_items_with_tax

    def get_list_of_products_in_checkout_overview_page(self):
        return self.get_text_all_elements(CheckOverview.NAME_PRODUCT)
