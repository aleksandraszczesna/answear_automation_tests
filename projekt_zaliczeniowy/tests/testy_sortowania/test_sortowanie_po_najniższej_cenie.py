import pytest
from selenium import webdriver
from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.sortowanie.sortowanie import Sorting


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_lowest_price(driver):
    website = Login(driver)
    website.open_website()
    website.accept_cookies()
    lowest_price = Sorting(driver)
    lowest_price.she_button_click()
    lowest_price.new_button_click()
    lowest_price.filters_button_click()
    lowest_price.sorting_button_click()
    lowest_price.lowest_button_click()
    lowest_price.back_button_click()
    lowest_price.view_products_click()
    produkty = lowest_price.products_list()
    poprzednia_cena = 0
    for produkt in produkty:
        cena_zl = produkt.text
        cena_bez_zl = cena_zl.removesuffix(" zł")
        cena = float(cena_bez_zl)
        print(f"Poprzednia cena wynosi: {poprzednia_cena}, a następna wynosi: {cena}")
        assert poprzednia_cena <= cena
        poprzednia_cena = cena