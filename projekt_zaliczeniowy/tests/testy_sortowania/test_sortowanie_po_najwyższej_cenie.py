import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.sortowanie.sortowanie import Sorting
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import selenium_chrome_tests_setup


@pytest.fixture
def driver():
    # to run it with gui interface pass False as arg
    yield from selenium_chrome_tests_setup()


def test_highest_price(driver):
    website = Login(driver)
    website.open_website()
    website.accept_cookies()
    highest_price = Sorting(driver)
    highest_price.she_button_click()
    highest_price.new_button_click()
    highest_price.filters_button_click()
    highest_price.highest_button_click()
    highest_price.submit_button_click()
    produkty = highest_price.product_list()
    for i in range(len(produkty)):
        cena = float(produkty[i].text.removesuffix(" zł"))
        if i + 1 < len(produkty):
            nizsza_cena = float(produkty[i + 1].text.removesuffix(" zł"))
            print(f"Cena wynosi: {cena}, a następna wynosi: {nizsza_cena}")
            assert cena >= nizsza_cena