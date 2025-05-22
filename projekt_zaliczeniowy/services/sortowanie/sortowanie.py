from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from projekt_zaliczeniowy.services.utils.base_test_utils import load_configuration

class Sorting:
    def __init__(self, driver):
        self.driver = driver
        self.she_button = (By.CSS_SELECTOR, '[href="/c/ona"]')
        self.new_button = (By.CSS_SELECTOR, '[data-test="newInFemale"]')
        self.mobile_filters_button = (By.CSS_SELECTOR, '[data-test="mobileFiltersTriggerButton"]')
        self.filters_button = (By.CSS_SELECTOR, '[data-test="productSortDropdown"]')
        self.sorting_button = (By.CSS_SELECTOR, '[data-test="sortFilter"]')
        self.lowest_button = (By.CSS_SELECTOR, '[for="price_asc_radio_0"]')
        self.highest_button = (By.CSS_SELECTOR, '[for="price_desc_radio_0"]')
        self.popular_button = (By.CSS_SELECTOR, '[for="popularity_radio_0"]')
        self.newest_button = (By.CSS_SELECTOR, '[for="date_desc_radio_0"]')
        self.back_button = (By.CSS_SELECTOR, '[data-test="mobileFiltersCloseButton"]')
        self.submit_button = (By.CSS_SELECTOR, '[data-test="selectSubmit"]')
        self.view_products = (By.CSS_SELECTOR, '[data-test="mobileFiltersSubmitButton"]')
        self.regular_price = (By.CSS_SELECTOR, '[data-test="regularPrice"]')

        self.config_data = load_configuration()

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

    def mobile_filters_button_click(self):
        try:
            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.mobile_filters_button))
            self.driver.find_element(*self.mobile_filters_button).click()
        except TimeoutException:
            print("Przycisk filtr nie jest klikalny.")

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

    def highest_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.highest_button))
            self.driver.find_element(*self.highest_button).click()
        except TimeoutException:
            print("Przycisk sortowania od najdroższych nie jest klikalny.")

    def popular_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.popular_button))
            self.driver.find_element(*self.popular_button).click()
        except TimeoutException:
            print("Przycisk sortowania od popularności nie jest klikalny.")

    def newest_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.newest_button))
            self.driver.find_element(*self.newest_button).click()
        except TimeoutException:
            print("Przycisk sortowania od najnowszych nie jest klikalny.")

    def back_button_click(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.back_button))
            self.driver.find_element(*self.back_button).click()
        except TimeoutException:
            print("Przycisk cofania filtrów nie jest klikalny.")

    def submit_button_click(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.submit_button))
            self.driver.find_element(*self.submit_button).click()
        except TimeoutException:
            print("Przycisk zapisywania filtrów nie jest klikalny.")

    def view_products_click(self):
        try:
            # Czekamy aż loader zniknie, jeśli taki istnieje
            WebDriverWait(self.driver, 20).until(
                EC.invisibility_of_element_located((By.CLASS_NAME, "Filters__filtersLoader__qVvBU"))
            )

            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.view_products))
            self.driver.find_element(*self.view_products).click()
        except TimeoutException:
            print("Przycisk pokaż produkty nie jest klikalny.")
        except ElementClickInterceptedException:
            print("Kliknięcie w przycisk 'Pokaż produkty' zostało przechwycone przez inny element.")

    def product_list(self):
        try:
           WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(self.regular_price))
           return self.driver.find_elements(*self.regular_price)
        except Exception as e:
            print(f"Ceny produktów nie są dostępne: {e}")