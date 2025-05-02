import allure
import pytest
from playwright.sync_api import sync_playwright

from projekt_zaliczeniowy.services.koszyk.koszyk import Cart
from projekt_zaliczeniowy.services.utils.base_test_utils import load_configuration


@pytest.mark.regression
@allure.feature("Koszyk")
@allure.story("Zmiana ilości produktów w koszyku")
def test_product_quantity_change():
    with sync_playwright() as p:
        # Uruchamianie przeglądarki w trybie headless
        config = load_configuration()
        is_headless = config['headless']
        browser = p.chromium.launch(headless=is_headless)
        # Nowa strona
        page = browser.new_page()
        # Ustawienie rozmiaru okna (viewport)
        page.set_viewport_size({"width": 1280, "height": 800})

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