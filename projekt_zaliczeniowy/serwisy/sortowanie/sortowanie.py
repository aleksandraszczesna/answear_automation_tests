from selenium.common import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from projekt_zaliczeniowy.serwisy.utils.base_test_utils import load_configuration


class SortingByTheLowestPrice:
    def __init__(self, driver):
        self.driver = driver
        self.she_button = (By.CSS_SELECTOR, '[href="/c/ona"]')
        self.new_button = (By.CSS_SELECTOR, '[data-test="newInFemale"]')
        self.filters_button = (By.CSS_SELECTOR, '[data-test="mobileFiltersTriggerButtonWrapper"]')
        self.sorting_button = (By.CSS_SELECTOR, '[data-test="sortFilter"]')
        self.lowest_button = (By.CSS_SELECTOR, '[for="price_asc_radio_0"]')
        self.back_button = (By.CSS_SELECTOR, '[data-test="mobileFiltersBackButton"]')
        self.view_products = (By.CSS_SELECTOR, '[data-test="mobileFiltersSubmitButton"]')
        self.regular_price = (By.CLASS_NAME, "ProductItemPrice__priceRegular__uGJHk")

    def website(self):
        self.driver.get('https://answear.com')

    def she_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.she_button))
            self.driver.find_element(*self.she_button ).click()
        except TimeoutException:
            print("Przycisk Ona nie jest klikalny.")

    def new_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.new_button))
            self.driver.find_element(*self.new_button).click()
        except TimeoutException:
            print("Przycisk Nowości nie jest klikalny.")

    def filters_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.filters_button))
            self.driver.find_element(*self.filters_button).click()
        except TimeoutException:
            print("Przycisk filtr nie jest klikalny.")

    def sorting_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sorting_button))
            self.driver.find_element(*self.sorting_button).click()
        except TimeoutException:
            print("Przycisk sortowania nie jest klikalny.")

    def lowest_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.lowest_button))
            self.driver.find_element(*self.lowest_button).click()
        except TimeoutException:
            print("Przycisk sortowania od najtańszych nie jest klikalny.")

    def back_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.back_button))
            self.driver.find_element(*self.back_button).click()
        except TimeoutException:
            print("Przycisk cofania nie jest klikalny.")

    def view_products_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.view_products))
            self.driver.find_element(*self.view_products).click()
        except TimeoutException:
            print("Przycisk pokaż produkty nie jest klikalny.")

    def products_list(self):
        try:
           WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.regular_price))
           return self.driver.find_elements(*self.regular_price)
        except Exception as e:
            print(f"Ceny produktów nie są dostępne: {e}")