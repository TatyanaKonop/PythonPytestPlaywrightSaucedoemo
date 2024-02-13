import pytest
from pages.login_page import Main

@pytest.fixture(scope = 'class')
def login_user(browser):
    m = Main(browser)
    m.user_login()

