from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from projekt_zaliczeniowy.serwisy.utils.base_test_utils import load_configuration


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.user_icon = (By.CSS_SELECTOR, '[data-test="my_account_icon"]')
        self.logout_button = (By.CSS_SELECTOR, '[class="MyAccount__logout__Nbfd1 active"]')
        self.config_data = load_configuration()

    def website(self):
        self.driver.get('https://answear.com/moje-konto')

    def user_icon_function(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.user_icon))
            user_icon_element = self.driver.find_element(*self.user_icon)
            action = ActionChains(self.driver)
            action.move_to_element(user_icon_element).perform()
        except TimeoutException:
            print("Ikona konta użytkownika nie jest widoczna.")

    def logout_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.logout_button))
            self.driver.find_element(*self.logout_button).click()
        except TimeoutException:
            print("Ikona wylogowania nie jest klikalna.")
