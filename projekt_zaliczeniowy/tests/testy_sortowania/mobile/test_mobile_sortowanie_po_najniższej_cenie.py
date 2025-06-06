import allure
import pytest

from projekt_zaliczeniowy.services.logowanie.logowanie import Login
from projekt_zaliczeniowy.services.sortowanie.sortowanie import Sorting
from projekt_zaliczeniowy.services.utils.base_test_utils import selenium_chrome_tests_setup, MOBILE_WINDOW_SIZE


@pytest.fixture
def driver():
    yield from selenium_chrome_tests_setup(MOBILE_WINDOW_SIZE)

@pytest.mark.regression
@allure.feature("Sortowanie")
@allure.story("Sortowanie po najniższej cenie")
def test_lowest_price(driver):
    website = Login(driver)
    website.open_website()
    website.accept_cookies()
    lowest_price = Sorting(driver)
    lowest_price.she_button_click()
    lowest_price.new_button_click()
    lowest_price.mobile_filters_button_click()
    lowest_price.sorting_button_click()
    lowest_price.lowest_button_click()
    lowest_price.submit_button_click()
    lowest_price.view_products_click()
    produkty = lowest_price.product_list()
    poprzednia_cena = 0
    for produkt in produkty:
        cena_zl = produkt.text
        cena_bez_zl = cena_zl.removesuffix(" zł")
        cena = float(cena_bez_zl)
        print(f"Poprzednia cena wynosi: {poprzednia_cena}, a następna wynosi: {cena}")
        assert poprzednia_cena <= cena
        poprzednia_cena = cena