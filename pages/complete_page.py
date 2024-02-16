from pages.base_page import Base
from playwright.sync_api import Page


class CompletePage(Base):
    def __init__(self, page: Page):
        super().__init__(page)
