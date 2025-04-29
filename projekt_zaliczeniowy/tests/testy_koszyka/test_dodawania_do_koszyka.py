import pytest
from playwright.sync_api import sync_playwright

from projekt_zaliczeniowy.serwisy.koszyk.koszyk import Cart


@pytest.mark.test
def test_add_product_to_cart():
    with sync_playwright() as p:
        # ustawiac headless z configa
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        add = Cart(page)
        add.go_to_new_in_female()
        add.get_first_element_from_the_site()
        add.add_to_cart()
        add.cart_icon_clik()
        cart_info = add.return_cart_info()
        cart_item = cart_info.cart_item
        cart_count = cart_info.cart_count
        assert cart_item.is_visible()
        assert int(cart_count) > 0
        browser.close()