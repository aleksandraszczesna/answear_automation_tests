import allure
import pytest

from projekt_zaliczeniowy.services.logowanie.logowanie import Login
from projekt_zaliczeniowy.services.sortowanie.sortowanie import Sorting
from projekt_zaliczeniowy.services.utils.base_test_utils import wait_for_url, selenium_chrome_tests_setup, \
    WEB_WINDOW_SIZE


@pytest.fixture
def driver():
    yield from selenium_chrome_tests_setup(WEB_WINDOW_SIZE)

@pytest.mark.regression
@allure.feature("Sortowanie")
@allure.story("Sortowanie po dodanych nowościach")
def test_newest(driver):
    website = Login(driver)
    website.open_website()
    website.accept_cookies()
    most_popular = Sorting(driver)
    config_data = most_popular.config_data
    most_popular.she_button_click()
    most_popular.new_button_click()
    most_popular.filters_button_click()
    most_popular.newest_button_click()
    most_popular.submit_button_click()
    wait_for_url(driver, config_data['credentials']['expected_sort_newest_url'], 5)
    assert driver.current_url == config_data['credentials']['expected_sort_newest_url']