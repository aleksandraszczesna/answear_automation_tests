import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.test
def test_add_product_to_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://answear.com/")
        page.click('[data-test="cookiesAcceptButton"]')
        page.click('[href="/c/ona"]')
        page.click('[data-test="newInFemale"]')
        #pobranie pierwszego elementu ze strony
        page.wait_for_selector('[data-test="outfitProduct"]')
        all_elements = page.query_selector_all('[data-test="outfitProduct"]')
        elements_with_positions = [(el.bounding_box()["y"], el) for el in all_elements if el.bounding_box() is not None]
        elements_with_positions.sort(key=lambda x: x[0])

        top_element = elements_with_positions[0][1]
        top_element.click()
        #dalej test dodawania do koszyka
        page.click('[data-test="modal-close-button"]')  #zamykanie okna zapisu do newslettera
        page.click('[data-test="size_dropdown"]')
        locator = page.locator('span.BaseSelectItem__selectItemLabel__jxiCx', has_text="XS")
        locator.click()
        page.click('[data-test="add_to_cart"]')
        #sprawdzenie koszyka
        page.click('[data-test="cart_icon"]')
        #sprawdzenie czy w koszyku liczba produktów jest większa od 0
        page.wait_for_selector('[data-test="quantitySelectorTemplateCounter"]')
        cart_count = page.inner_text('[data-test="quantitySelectorTemplateCounter"]')
        cart_item = page.locator('[data-test="cartRemoveItem"]')
        assert cart_item.is_visible()
        assert len(cart_count) > 0
        browser.close()