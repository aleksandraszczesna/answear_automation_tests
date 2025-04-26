import pytest
from playwright.sync_api import sync_playwright
from projekt_zaliczeniowy.serwisy.koszyk.koszyk import Cart

@pytest.mark.test
def test_remove_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        remove = Cart(page)
        remove.go_to_new_in_female()
        remove.get_first_element_from_the_site()
        remove.add_to_cart()
        remove.cart_icon_clik()
        remove.remove_from_cart()
        assert page.inner_text(".EmptyCart__emptyCartHeaderText__A-wHs") == "Twój koszyk jest pusty"

        browser.close()