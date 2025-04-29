import time
from playwright.sync_api import TimeoutError


class Cart:
    def __init__(self, page):
        self.page = page

    def go_to_new_in_female(self):
        self.page.goto("https://answear.com/")
        # Bezpieczne kliknięcie w ciasteczka
        try:
            self.page.click('[data-test="cookiesAcceptButton"]', timeout=3000)  # 3 sekundy na pojawienie się przycisku
        except TimeoutError:
            print("Przycisk cookies nie pojawił się – kontynuuję dalej.")
        self.page.click('[href="/c/ona"]')
        self.page.click('[data-test="newInFemale"]')

    def get_first_element_from_the_site(self):
        self.page.wait_for_selector('[data-test="outfitProduct"]')
        all_elements = self.page.query_selector_all('[data-test="outfitProduct"]')
        elements_with_positions = [(el.bounding_box()["y"], el) for el in all_elements if el.bounding_box() is not None]
        elements_with_positions.sort(key=lambda x: x[0])
        top_element = elements_with_positions[0][1]
        top_element.click()

    def add_to_cart(self):
        self.page.click('[data-test="modal-close-button"]')  # zamykanie okna zapisu do newslettera
        self.page.wait_for_selector('[data-test="size_dropdown"]')
        self.page.click('[data-test="size_dropdown"]')
        locator_xs = self.page.locator('li[data-test=available_size]:has(span.BaseSelectItem__selectItemLabel__jxiCx)',
                                       has_text="XS")
        locator_s = self.page.locator('li[data-test=available_size]:has(span.BaseSelectItem__selectItemLabel__jxiCx)',
                                      has_text="S")
        locator_m = self.page.locator('li[data-test=available_size]:has(span.BaseSelectItem__selectItemLabel__jxiCx)',
                                      has_text="M")
        locator_l = self.page.locator('li[data-test=available_size]:has(span.BaseSelectItem__selectItemLabel__jxiCx)',
                                      has_text="L")
        locator_xl = self.page.locator('li[data-test=available_size]:has(span.BaseSelectItem__selectItemLabel__jxiCx)',
                                       has_text="XL")
        if locator_xs.is_visible():
            locator_xs.click()
        elif locator_s.is_visible():
            locator_s.click()
        elif locator_m.is_visible():
            locator_m.click()
        elif locator_l.is_visible():
            locator_l.click()
        elif locator_xl.is_visible():
            locator_xl.click()
        else:
            self.wait_for_add_item()
        self.wait_for_add_item()

    def wait_for_add_item(self):
        counter = 0
        while not self.page.locator('[data-test="notificationSuccess"]').is_visible() and counter < 5:
            self.page.click('[data-test="add_to_cart"]')
            time.sleep(1)
            counter += 1

    def cart_icon_clik(self):
        self.page.click('[data-test="cart_icon"]')

    def return_cart_info(self):
        self.page.wait_for_selector('[data-test="quantitySelectorTemplateCounter"]')
        cart_count = self.page.inner_text('[data-test="quantitySelectorTemplateCounter"]')
        cart_item = self.page.locator('[data-test="cartRemoveItem"]')
        cart_info = CartInfo(cart_count, cart_item)
        return cart_info

    def increase_quantity(self):
        self.page.click('[data-test="quantitySelectorTemplateIncreaseButton"]')

    def decrease_quantity(self):
        self.page.click('[data-test="quantitySelectorTemplateDecreaseButton"]')

    def remove_from_cart(self):
        self.page.click('[data-test="cartRemoveItem"]')


class CartInfo:
    def __init__(self, cart_count, cart_item):
        self.cart_count = cart_count
        self.cart_item = cart_item
