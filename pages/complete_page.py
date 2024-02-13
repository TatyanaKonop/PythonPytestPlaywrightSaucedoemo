from pages.base_page import Base
from data.assertions import Assertions
from playwright.sync_api import Page


class CompletePage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)



