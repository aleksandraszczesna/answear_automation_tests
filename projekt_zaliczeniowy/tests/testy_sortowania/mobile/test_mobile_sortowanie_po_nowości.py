import pytest
from selenium import webdriver

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.sortowanie.sortowanie import Sorting
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import wait_for_url


@pytest.fixture
def driver():
    # by nie zapisywac danych sesji pusty options
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(430, 932)
    yield driver
    driver.quit()


def test_most_popular(driver):
    website = Login(driver)
    website.open_website()
    website.accept_cookies()
    most_popular = Sorting(driver)
    config_data = most_popular.config_data
    most_popular.she_button_click()
    most_popular.new_button_click()
    most_popular.mobile_filters_button_click()
    most_popular.sorting_button_click()
    most_popular.newest_button_click()
    most_popular.back_button_click()
    most_popular.view_products_click()
    wait_for_url(driver, config_data['credentials']['expected_sort_newest_url'], 5)
    assert driver.current_url == config_data['credentials']['expected_sort_newest_url']