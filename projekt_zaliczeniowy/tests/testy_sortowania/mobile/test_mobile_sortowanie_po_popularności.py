import allure
import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.sortowanie.sortowanie import Sorting
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import wait_for_url, selenium_chrome_tests_setup, \
    MOBILE_WINDOW_SIZE


@pytest.fixture
def driver():
    yield from selenium_chrome_tests_setup(MOBILE_WINDOW_SIZE)

@pytest.mark.regression
@allure.feature("Sortowanie")
@allure.story("Sortowanie po popularności prosuktów")
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
    most_popular.popular_button_click()
    most_popular.submit_button_click()
    most_popular.view_products_click()
    wait_for_url(driver, config_data['credentials']['expected_sort_popularity_url'], 20)
    assert driver.current_url == config_data['credentials']['expected_sort_popularity_url']