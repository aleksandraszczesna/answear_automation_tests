import pytest

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import wait_for_url, chrome_tests_setup
from projekt_zaliczeniowy.serwisy.wylogowanie.wylogowanie import Logout


@pytest.fixture
def driver():
    yield from chrome_tests_setup()

def test_logout(driver):
    login = Login(driver)
    config_data = login.config_data
    login.open_website()
    login.accept_cookies()
    login.user_account()
    login.insert_email(config_data['credentials']['email'])
    login.insert_password(config_data['credentials']['password'])
    login.login_button()
    wait_for_url(driver, config_data['credentials']['expected_url'], 5)
    assert driver.current_url == config_data['credentials']['expected_url']
    logout = Logout(driver)
    config_data = logout.config_data
    logout.website()
    logout.user_icon_function()
    logout.logout_button_click()
    wait_for_url(driver, config_data['credentials']['expected_logout_url'], 5)
    assert driver.current_url == config_data['credentials']['expected_logout_url']