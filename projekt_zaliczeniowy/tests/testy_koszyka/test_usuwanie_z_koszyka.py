import allure
import pytest
from playwright.sync_api import sync_playwright
from projekt_zaliczeniowy.serwisy.koszyk.koszyk import Cart
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import load_configuration


@pytest.mark.regression
@allure.feature("Koszyk")
@allure.story("Usuwanie produktów do koszyka")
def test_remove_product_to_cart():
    with sync_playwright() as p:
        # Uruchamianie przeglądarki w trybie headless
        config = load_configuration()
        is_headless = config['headless']
        browser = p.chromium.launch(headless=is_headless)
        # Nowa strona
        page = browser.new_page()
        # Ustawienie rozmiaru okna (viewport)
        page.set_viewport_size({"width": 1280, "height": 800})

        remove = Cart(page)
        remove.go_to_new_in_female()
        remove.get_first_element_from_the_site()
        remove.add_to_cart()
        remove.cart_icon_clik()
        remove.remove_from_cart()
        assert page.inner_text(".EmptyCart__emptyCartHeaderText__A-wHs") == "Twój koszyk jest pusty"

        browser.close()