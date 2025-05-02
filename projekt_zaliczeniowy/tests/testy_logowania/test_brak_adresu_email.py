import allure
import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import selenium_chrome_tests_setup, WEB_WINDOW_SIZE


@pytest.fixture
@allure.feature("Logowanie")
@allure.story("Logowanie bez uzupełnienia pola adres email")
def driver():
    yield from selenium_chrome_tests_setup(WEB_WINDOW_SIZE)

def test_without_email(driver):
    without_email = Login(driver)
    without_email.open_website()
    without_email.accept_cookies()
    without_email.user_account()
    without_email.login_button()
    error_text = without_email.email_error()
    assert without_email.config_data['without_email']['expected_error_msg'] in error_text

