import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from projekt_zaliczeniowy.serwisy.logowanie.logowanie import Login
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import selenium_chrome_tests_setup, WEB_WINDOW_SIZE


@pytest.fixture
def driver():
    yield from selenium_chrome_tests_setup(WEB_WINDOW_SIZE)

@pytest.mark.regression
@allure.feature("Logowanie")
@allure.story("Logowanie z użyciem poprawnych danych")
def test_correct(driver):
    correct = Login(driver)
    config_data = correct.config_data
    correct.open_website()
    correct.accept_cookies()
    correct.user_account()
    correct.insert_email(config_data['credentials']['email'])
    correct.insert_password(config_data['credentials']['password'])
    correct.login_button()
    WebDriverWait(driver, 5).until(EC.url_to_be(config_data['credentials']['expected_url']))
    assert driver.current_url == config_data['credentials']['expected_url']

# ctr + alt + o usuwa nieuzywane import
# ctr + ? wstawia komentarz
# ctr + alt + l formatuje kod wciecia itpt