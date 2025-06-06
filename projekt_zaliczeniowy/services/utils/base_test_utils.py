from pathlib import Path

import yaml
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# jezeli jakas metoda powtarza sie w wiecej niz jednej klasie testowej powinna trafiac tutaj

WEB_WINDOW_SIZE = "1920,1080"
MOBILE_WINDOW_SIZE = "430,932"

def selenium_chrome_tests_setup(windows_size):
    # Tworzy obiekt opcji dla Chrome, który pozwala skonfigurować sposób uruchomienia przeglądarki
    options = webdriver.ChromeOptions()
    # --headless=new: Uruchamia Chrome w trybie headless (bez interfejsu graficznego).
    # Opcja 'new' jest nowym, bardziej stabilnym trybem headless, wprowadzonym w Chrome 109.
    # Jest to szczególnie przydatne w środowiskach CI (np. GitHub Actions), gdzie nie ma dostępu do GUI.
    config = load_configuration()
    if config['headless']:
        options.add_argument('--headless=new')
    # Ustawienie windows-size
    options.add_argument(f"--window-size={windows_size}")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def wait_for_url(driver, url, time):
    WebDriverWait(driver, time).until(EC.url_to_be(url))

def load_configuration():
    # Pobierz katalog, w którym znajduje się skrypt(ten plik)
    # Określamy katalog główny projektu czyli projekt_zaliczeniowy
    # cofamy sie do logowanie -> services -> projekt zaliczeniowy i doklejamy katalog i nazwe pliku
    current_directory = Path(__file__).parent.parent.parent
    # Zbuduj pełną ścieżkę do pliku config.yaml w katalogu configuration
    file_path = current_directory/ 'configuration' / 'config.yaml'
    with open(file_path, 'r', encoding='utf-8') as file: # encoding='utf-8' by były polskie znaki zaczytane z pliku
        return yaml.full_load(file)