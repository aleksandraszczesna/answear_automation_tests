import pytest
from playwright.sync_api import sync_playwright

from projekt_zaliczeniowy.serwisy.koszyk.koszyk import Cart


@pytest.mark.test
def test_product_quantity_change():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        change = Cart(page)
        change.go_to_new_in_female()
        change.get_first_element_from_the_site()
        change.add_to_cart()
        change.cart_icon_clik()
        change.increase_quantity()
        cart_info_before = change.return_cart_info()
        cart_count_before = cart_info_before.cart_count
        assert int(cart_count_before) == 2
        change.decrease_quantity()
        cart_info_after = change.return_cart_info()
        cart_count_after = cart_info_after.cart_count
        assert int(cart_count_after) == 1
        browser.close()