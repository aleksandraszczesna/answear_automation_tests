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
# ctr + alt + o usuwa nieuzywane import
# ctr + ? wstawia komentarz
# ctr + alt + l formatuje kod wciecia itp