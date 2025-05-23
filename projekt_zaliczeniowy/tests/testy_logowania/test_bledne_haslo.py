import allure
import pytest
from projekt_zaliczeniowy.services.logowanie.logowanie import Login
from projekt_zaliczeniowy.services.utils.base_test_utils import selenium_chrome_tests_setup, WEB_WINDOW_SIZE


@pytest.fixture
def driver():
    yield from selenium_chrome_tests_setup(WEB_WINDOW_SIZE)

@pytest.mark.regression
@allure.feature("Logowanie")
@allure.story("Logowanie z użyciem błędnego hasła")
def test_wrong_password(driver):
    wrong_password = Login(driver)
    config_data = wrong_password.config_data
    wrong_password.open_website()
    wrong_password.accept_cookies()
    #wrong_password.user_account()
    wrong_password.insert_email(config_data['credentials']['email'])
    wrong_password.insert_password(config_data['false_credentials']['password'])
    wrong_password.login_button()
    password_error_tekst = wrong_password.password_error()
    assert wrong_password.config_data['false_credentials']['expected_password_error_msg'] in password_error_tekst