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
@allure.story("Sortowanie po najwyższej cenie")
def test_highest_price(driver):
    website = Login(driver)
    website.open_website()
    website.accept_cookies()
    highest_price = Sorting(driver)
    highest_price.she_button_click()
    highest_price.new_button_click()
    highest_price.mobile_filters_button_click()
    highest_price.sorting_button_click()
    highest_price.highest_button_click()
    highest_price.submit_button_click()
    highest_price.view_products_click()
    produkty = highest_price.product_list()
    for i in range(len(produkty)):
        cena = float(produkty[i].text.removesuffix(" zł"))
        if i + 1 < len(produkty):
            nizsza_cena = float(produkty[i + 1].text.removesuffix(" zł"))
            print(f"Cena wynosi: {cena}, a następna wynosi: {nizsza_cena}")
            assert cena >= nizsza_cena