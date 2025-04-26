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