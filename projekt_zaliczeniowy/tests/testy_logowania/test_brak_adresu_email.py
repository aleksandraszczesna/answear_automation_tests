import pytest
from selenium import webdriver

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login


@pytest.fixture
def driver():
    # by nie zapisywac danych sesji pusty options
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_without_email(driver):
    without_email = Login(driver)
    without_email.open_website()
    without_email.accept_cookies()
    without_email.user_account()
    without_email.login_button()
    error_text = without_email.email_error()
    assert without_email.config_data['without_email']['expected_error_msg'] in error_text

