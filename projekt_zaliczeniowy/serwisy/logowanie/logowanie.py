import os
from pathlib import Path

from selenium import webdriver
from selenium.common import TimeoutException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from projekt_zaliczeniowy.serwisy.utils.base_test_utils import load_configuration

screenshots_directory = Path(__file__).parent.parent.parent / 'screenshots'

class Login:
    def __init__(self, driver):
        self.driver = driver
        self.accept_cookies_button = (By.CSS_SELECTOR, '[data-test="cookiesAcceptButton"]')
        self.user_account_icon = (By.CSS_SELECTOR, '[data-test="my_account_icon"]')
        self.email_field = (By.ID, '_username')
        self.password_field = (By.ID, '_password')
        self.login_button_click = (By.CSS_SELECTOR, '[class="btn xs-12 l-12 btnPrimary btn--fluid Button__buttonContainerFontWeight__3oaib"]')
        self.error_message_email = (By.CSS_SELECTOR, '[class="fieldError FieldError__error__eoDKL"]')
        self.error_message_password = (By.XPATH, '//*[@id="root"]/main/div/div/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/form/div[2]/span[2]')
        self.config_data = load_configuration()



    def open_website(self):
        self.driver.get('https://answear.com/')

    def get_element_from_shadow_root(self, by, locator):
        # dostęp do shadow host - dodatkowe opakowanie w html
        shadow_host = WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(
            EC.presence_of_element_located((By.ID, 'usercentrics-root'))
        )
        # Uzyskanie dostępu do Shadow DOM - czyli struktury html w tym shadow
        shadow_root = self.driver.execute_script('return arguments[0].shadowRoot', shadow_host)

        # Poczekaj, aż element będzie dostępny w shadowRoot
        element = WebDriverWait(shadow_root, self.config_data['timeout']['log_in']).until(
            EC.presence_of_element_located((by, locator))
        )
        return element

    def accept_cookies(self):
        try:
            WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.element_to_be_clickable(self.accept_cookies_button))
            self.driver.find_element(*self.accept_cookies_button).click()
        except TimeoutException:
            print("Przycisk akceptacji cookies nie został znaleziony.")

    def user_account(self):
        try:
            WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.element_to_be_clickable(self.user_account_icon))
            self.driver.find_element(*self.user_account_icon).click()
        except TimeoutException:
            print("Ikona konta użytkownika nie jest klikalna.")

    def insert_email(self, email_input):
        try:
            WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.presence_of_element_located(self.email_field))
            self.driver.find_element(*self.email_field).send_keys(email_input)
        except TimeoutException:
            print("Pole 'Adres e-mail' nie jest klikalne.")

    def insert_password(self, password_input): # element to be clickable
        try:
            WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.element_to_be_clickable(self.password_field))
            self.driver.find_element(*self.password_field).send_keys(password_input)
        except TimeoutException:
            print("Pole 'Hasło' nie zostało znalezione w oczekiwanym czasie.")
        except ElementNotInteractableException:
            print("Pole 'Hasło' nie jest interaktywne.")

    def login_button(self):
        try:
            WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.visibility_of_element_located(self.login_button_click))
            self.driver.find_element(*self.login_button_click).click()
        except TimeoutException:
            print("Przycisk 'Zaloguj się' nie jest klikalny.")

    def email_error(self):
        try:
            error_element = WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.visibility_of_element_located(self.error_message_email))
            # pobranie textu z error_element
            error_text = error_element.text
            print(f"Komunikat błędu: {error_text}")
            screenshot_path = self.path('komunikat_bledu_email.png')
            self.driver.save_screenshot(screenshot_path)
            return error_text
        except TimeoutException:
            print("Brak komunikatu błędu.")
        except Exception as e:
            print(f"Błąd przy próbie znalezienia komunikatu błędu: {e}")
            screenshot_path = self.path("email_failed.png")
            self.driver.save_screenshot(screenshot_path)

    def password_error(self):
        try:
            password_error_element = WebDriverWait(self.driver, self.config_data['timeout']['log_in']).until(EC.visibility_of_element_located(self.error_message_password))
            # pobranie textu z password error_element
            password_error_text = password_error_element.text
            print(f"Komunikat błędu: {password_error_text}")
            screenshot_path = self.path("komunikat_bledu_hasla.png")
            self.driver.save_screenshot(screenshot_path)
            return password_error_text
        except TimeoutException:
            print("Brak komunikatu błędu hasła.")
        except Exception as e:
            print(f"Błąd przy próbie znalezienia komunikatu błędu hasła: {e}")
            screenshot_path = self.path("password_failed.png")
            self.driver.save_screenshot(screenshot_path)

    def path(self, file_name):
        return os.path.join(screenshots_directory, file_name)

    #self.error_message_password = (
    #By.CSS_SELECTOR, '[class="goVnUa m3OCL3 voFjEy S3xARh _9bYLON n4kyHD _3LATVU _3laWWw J7qafN"]')

    def webDriverWithUserAgent(self):
        # Tworzenie instancji ChromeOptions
        chrome_options = Options()
        service = Service(executable_path="D:\Workspace\project\zalando_automation_tests\chromedriver.exe")
        # Ustawienie User-Agent na standardowy nagłówek przeglądarki
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.execute_cdp_cmd('Network.enable', {})
        # Dodanie nagłówka 'Authorization'
        driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
            'headers': {
                'cookie': 'X-Zalando-Client-Id=944dd548-8c3d-4a93-aa2a-9d78092ab68f; csrf-token=3ecdd407-885f-40fd-9e6d-7633280f4830; _ga=GA1.3.1597896020.1743531809; _ga=GA1.1.1597896020.1743531809; ak_bmsc=FA21023A243C5D424A30AB957E8CDFC2~000000000000000000000000000000~YAAQONAXAni0/K2VAQAAgB+Y8htuXUcnn1mL0In91MpSQifrqzGz0XzI1sOp1sc+qusXGExNXCRhcq53H/iYz18sxhu1AhqOy+k36GCx1MSbbaTwtqA57kRfBFwy437heCSN64c8Fcc7baT1q9tVv71OYiQCvF1O1/ONzHx+oZ8BjJju8Ebem9stVpeUF9Q1wWdXtPvjqrNodgy6xAPwM0NvCBihF9RWGSD4w/ZlYgiJnpb2ItQ18ivgcLXFiRZ21wHqT89pRsAp/1lET2MC24zazdxst83GrOBAanGigxQSe7AUGeoFdW886yAv5LDMq0aVtnz2MEN6RCRsue8K4Zk6bTq3aQ0uZC3gY5dsmeKytCCJwfcPbsOA9pDxz4xgStpQ23FtUc2ObWtGtEvYXdp3rk0XNna0g3rGvuRgvBPWofXPRItviQKVnjTfhZlPZRI4A3ApJY7oSQjesC8hZY0umPTBwCwnPrVv42yGT4rSVlUHLOQLa4prOrNQZOj0UTp5UsCAE962kbtZpoLqG2NpVc7Gw/ox; FPID=FPID2.2.TjY%2Br4YNIXd1Z5nIhgfASOuA2yY%2F96QjXYeIDD%2Bm%2BNI%3D.1743531809; FPLC=NQ9A%2B6I6b0aI%2BPYuSj0buuF%2FDWtr0sp9zcY%2FpDB12bo%2BAWD78kz85x9dhHyroBSj89EIUqAI2%2FZvvPRk0%2FYAauEFPukHd9BGn9xKZX64FEv68%2BZQEm3PaktmMEDBNA%3D%3D; bm_sv=D2B42D1632E50359AFC9D249FDB2CD60~YAAQONAXAny0/K2VAQAAiCCY8hsNXyc8Rybk8CzqTWF4sMNutgPFukYF2Hm4cbxQCqZqR8az4VjDFzefiZMQ//QC1A971bYOVTxqInoSkhQhuR44MzS1oAFAnynSqRU3Mx6QZhjGUh01kFgZy2LTAYhP8RMwraZyllwMbi4FXipydWLKVsRMLhhUChRFsD+Wf4uaCVrS/1FL21UARuxuRMaCAuHzgaXD2iDns3oIMMlWKU70CMXbuQGHhzjHIIbFYw==~1; _abck=44A447775744497CB8AC1481EF61ADB1~-1~YAAQONAXAva0/K2VAQAAajqY8g2JfIR6n60kq5GzRS3ypJ9solCZUgWRnzEFURTLTfFqKsTWOemEIrPxVGebHZIMYU42jPinmQbLT9Ysap3Jd9VlXkLAX20VbpZhNoK6neat73Ddetki6wwVoqsfQsocM62T4fwYsVWrOmOII+mOPL2f1NHFmaHmBrTxFFi2Ze9bB0cUA1Lr1WQz8k8DFXtneS/6Zw8kysTGJOHKDCQQGjZnjwSaaNCCt2hCBLBOLaXk6vlFduVWd7mJt7Xo071liW0fEl+/4Th9bbOuvQyrfEu3xEdKEP32l6YHZl06rCa+Jk3s/0i6MN4CGg7wdLN5aOX8WkYogq28Vk5Z8+we17x6PkAdDZiORm0xoLmls916NXPLRJDORsyMNPJ4pbqxL6S4B6WidaChNMws2dK+wPR8eRasednczFxSOSm/Skgcdr3ckl5oTaYdRaP8Tdk9/5XDnLFLh3NXLQicMQYvWWoePCQy44i1ksGw9gfVFNSNZCX8BOnClbEk+vcwTuAJ9/DwfIPI3Ns4N3RG5/FG26kO+3GHs13Rg0gdgjsqaCSVqj8AFiQcgSaHRxwHHxnLxM/dkXyI9OzmviUmgdyX1ZHtPBGGf00z5RULOvuRO5PpWi4vE5D/OyKYXakrT/xYtthL5hzGcGDrsvI0hu0w1TN8amxPwSlPgEFwLH5Y553cdm1FylITXugOl4/sv4lrsj70IUSoyeoUx73kb1nUMynhzFu+qy5NvNUfpur7bcsqWSJEXU+B/nBsNNevuA/tFZZrj+7oznGrGBCuYPgfP4q335x7zDIPsSWvzuhcOnwixwIaud7t3LXvQDusJNs7FdO2J0i4aYccOVU8cL1RX31ZbrLV/k8wgZ/rQd4vYhUpPc6o2rcq1BZpGKWzavzqxe8Alpfxe+PGpsGgiX+PPRMu8EF1UeA0qEc4+5EbnN4=~-1~-1~1743535410; bm_sz=8E9425FDB33EEBFD035FFFB0711CAB53~YAAQONAXAve0/K2VAQAAajqY8huwRjN9DMNdqAgrpthMmVdPUAphYAPiVHOlyFEkF7NnYPlX4Pb3w+TEkyTIkoeBJanteVWQlcCF+9Syk3An+aMMRpxymiyxTz+fm3YjGuV364z95WeGwtfGVm5Ne9F7xxvNhv+BMZOn3eXDsQsu1NEcQULiQnQIh47Yg9MvYHqiWrCtXiOnjJsBh6Mi2BDx2ECAz1CKQFZJC9pS5yDgc1lR7ERD1nXHeNuiUjFfA3jUisUB8xxzuHeUGKLfgvPe7ZI4dXgE6FlsgS4JIWHFR5SlJu0wrjt2x32QTxSMN6zfKaK76LYwzFiAKXh1uhzaRFaJjeCJHabS67m4nc4FF2Guyy8R+nZsF9g7SYZ/CYvb2Bny5+++08LBUbonMVq8CiUSxplSrkKIi2kb9Olj4fv58AvEtpuByk60Ra+KdtQ3PalZSJEeG2e21sl3fDc7l1s0~3621939~3491125; _ga_8XX5HBC4Q8=GS1.1.1743531808.1.1.1743531821.0.0.1912538494'
            }
        })
