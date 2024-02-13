import time
from playwright.sync_api import Playwright, sync_playwright, expect


def test_button_locator(page):

    page.goto('https://ecommerce-playground.lambdatest.io/index.php?route=product/category&path=57')
    page.mouse.wheel(0, 300)
    page.get_by_role("link", name="HTC Touch HD HTC Touch HD HTC").hover()
    page.locator('button:nth-child(3)').first.click()

    page.get_by_role('button', name='Increase quantity').click()

    page.get_by_role('button',  name= 'Increase quantity').click(click_count = 3)


    #page.locator('.btn.btn-dark .fas.fa-plus-circle').click()
    page.click('.btn.btn-dark .fas.fa-plus-circle')
    text = page.get_by_text("Product 1").inner_text()
    assert text == ('Product 1')
    expect(page.get_by_label("Qty")).to_have_value("6")
    page.pause()
    expect(page.locator('#image-gallery-212946').get_by_role('link', name= 'HTC Touch HD')).to_have_count(5)
    print('kk')






    time.sleep(10)

    #page.get_by_label("Incre)ase quantity").click(clickCount=5)


