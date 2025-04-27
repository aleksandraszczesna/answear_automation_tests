import pytest
from selenium import webdriver

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.sortowanie.sortowanie import Sorting


@pytest.fixture
def driver():
    # by nie zapisywac danych sesji pusty options
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


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