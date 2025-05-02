import allure
import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import selenium_chrome_tests_setup, WEB_WINDOW_SIZE


@pytest.fixture
@pytest.mark.regression
@allure.feature("Logowanie")
@allure.story("Logowanie z użyciem błędnego hasła")
def driver():
    # to run it with gui interface pass False as arg
    yield from selenium_chrome_tests_setup(WEB_WINDOW_SIZE)

def test_without_password(driver):
    without_password = Login(driver)
    config_data = without_password.config_data
    without_password.open_website()
    without_password.accept_cookies()
    without_password.user_account()
    without_password.insert_email(config_data['credentials']['email'])
    without_password.login_button()
    password_error_tekst = without_password.password_error()
    assert without_password.config_data['without_password']['expected_error_msg'] in password_error_tekst

# ctr + alt + o usuwa nieuzywane import
# ctr + ? wstawia komentarz
# ctr + alt + l formatuje kod wciecia itpt