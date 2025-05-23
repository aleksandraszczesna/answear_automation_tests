import allure
import pytest
from playwright.sync_api import sync_playwright

from projekt_zaliczeniowy.services.koszyk.koszyk import Cart
from projekt_zaliczeniowy.services.utils.base_test_utils import load_configuration

@pytest.mark.regression
@allure.feature("Koszyk")
@allure.story("Dodawnie produktów do koszyka")
def test_add_product_to_cart():
    with sync_playwright() as p:
        # Uruchamianie przeglądarki w trybie headless
        config = load_configuration()
        is_headless = config['headless']
        browser = p.chromium.launch(headless=is_headless)
        # Nowa strona
        page = browser.new_page()
        # Ustawienie rozmiaru okna (viewport)
        page.set_viewport_size({"width": 1280, "height": 800})

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