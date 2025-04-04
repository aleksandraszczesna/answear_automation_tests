from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import yaml

# jezeli jakas metoda powtarza sie w wiecej niz jednej klasie testowej powinna trafiac tutaj
def wait_for_url(driver, url, time):
    WebDriverWait(driver, time).until(EC.url_to_be(url))

def load_configuration():
    # Pobierz katalog, w którym znajduje się skrypt(ten plik)
    # Określamy katalog główny projektu czyli projekt_zaliczeniowy
    # cofamy sie do logowanie -> serwisy -> projekt zaliczeniowy i doklejamy katalog i nazwe pliku
    current_directory = Path(__file__).parent.parent.parent
    # Zbuduj pełną ścieżkę do pliku config.yaml w katalogu configuration
    file_path = current_directory/ 'configuration' / 'config.yaml'
    with open(file_path, 'r', encoding='utf-8') as file: # encoding='utf-8' by były polskie znaki zaczytane z pliku
        return yaml.full_load(file)