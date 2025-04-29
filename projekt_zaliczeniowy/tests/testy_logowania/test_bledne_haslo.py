import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import selenium_chrome_tests_setup


@pytest.fixture
def driver():
    # to run it with gui interface pass False as arg
    yield from selenium_chrome_tests_setup("1920,1080")

def test_wrong_password(driver):
    wrong_password = Login(driver)
    config_data = wrong_password.config_data
    wrong_password.open_website()
    wrong_password.accept_cookies()
    wrong_password.user_account()
    wrong_password.insert_email(config_data['credentials']['email'])
    wrong_password.insert_password(config_data['false_credentials']['password'])
    wrong_password.login_button()
    password_error_tekst = wrong_password.password_error()
    assert wrong_password.config_data['false_credentials']['expected_password_error_msg'] in password_error_tekst