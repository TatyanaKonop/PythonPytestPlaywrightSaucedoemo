
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("Создать первый сценарий playwright")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.pause()
def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label('Email address').fill("qa@example.com")
    page.get_by_title('username').fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()