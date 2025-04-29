import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.sortowanie.sortowanie import Sorting
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import wait_for_url, selenium_chrome_tests_setup


@pytest.fixture
def driver():
    # to run it with gui interface pass False as arg
    yield from selenium_chrome_tests_setup("1920,1080")


def test_most_popular(driver):
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