import allure
import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import selenium_chrome_tests_setup, WEB_WINDOW_SIZE


@pytest.fixture
def driver():
    yield from selenium_chrome_tests_setup(WEB_WINDOW_SIZE)

@pytest.mark.regression
@allure.feature("Logowanie")
@allure.story("Logowanie z użyciem błędnego adresu email")
def test_wrong_email(driver):
    wrong_email = Login(driver)
    config_data = wrong_email.config_data
    wrong_email.open_website()
    wrong_email.accept_cookies()
    wrong_email.user_account()
    wrong_email.insert_email(config_data['false_credentials']['email'])
    wrong_email.login_button()
    error_text = wrong_email.email_error()
    assert wrong_email.config_data['false_credentials']['expected_error_msg'] in error_text