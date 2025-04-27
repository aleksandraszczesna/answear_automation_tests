from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from selenium import webdriver
import yaml
import tempfile

def chrome_tests_setup():
    # Tworzy obiekt opcji dla Chrome, który pozwala skonfigurować sposób uruchomienia przeglądarki
    options = webdriver.ChromeOptions()
    # --headless=new: Uruchamia Chrome w trybie headless (bez interfejsu graficznego).
    # Opcja 'new' jest nowym, bardziej stabilnym trybem headless, wprowadzonym w Chrome 109.
    # Jest to szczególnie przydatne w środowiskach CI (np. GitHub Actions), gdzie nie ma dostępu do GUI.
    options.add_argument('--headless=new')
    # --no-sandbox: Wymagana jest dla środowisk CI (np. GitHub Actions, Linux).
    # Sandbox to mechanizm izolacji, który w niektórych środowiskach (np. w CI) może powodować problemy.
    # Wyłączenie sandboxa pozwala na uruchomienie Chrome bez tych restrykcji.
    # options.add_argument('--no-sandbox')
    # --disable-dev-shm-usage: Wyłącza używanie pamięci współdzielonej (SHM) dla aplikacji.
    # W CI lub kontenerach Docker ta opcja jest potrzebna, ponieważ /dev/shm (gdzie przechowywana jest pamięć współdzielona)
    # może mieć ograniczoną wielkość, co może prowadzić do problemów z uruchamianiem Chrome.
    # options.add_argument('--disable-dev-shm-usage')
    # --user-data-dir: Ustala unikalny katalog danych użytkownika dla każdej sesji przeglądarki.
    # Dzięki temu unikamy konfliktów z danymi sesji w środowiskach wielo-testowych.
    # `tempfile.mkdtemp()` tworzy tymczasowy katalog w systemie plików.
    # options.add_argument(f'--user-data-dir={tempfile.mkdtemp()}')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

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