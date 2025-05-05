# Automatyczne testy strony sklepu odzieżowego
Ten projekt zawiera zestaw testów automatycznych dla strony internetowej sklepu odzieżowego. Testy obejmują procesy takie jak logowanie, filtrowanie produktów i inne funkcje typowe dla sklepu internetowego.

## Spis treści
1. [Opis](#opis)
2. [Wymagania](#wymagania)
3. [Instalacja](#instalacja)
4. [Uruchamianie testów](#uruchamianie-testów)
5. [Struktura projektu](#struktura-projektu)
6. [Integracja ciągła (CI) i raportowanie](#integracja-ciągła-ci-i-raportowanie)

## Opis
Testy automatyczne służą do sprawdzania poprawności działania różnych funkcji sklepu internetowego. 
Testy obejmują m.in. logowanie, wylogowanie, filtrowanie produktów oraz interakcje z koszykiem.
Testy zostały napisane z wykorzystaniem dwóch różnych frameworków:
- Playwright
- Selenium

Testy są uruchamiane z wykorzystaniem frameworka pytest i skonfigurowane za pomocą osobnego pliku konfiguracyjnego.
- projekt_zaliczeniowy/configuration/config.yaml

## Wymagania
Aby uruchomić testy, potrzebujesz:
- [Python 3.7+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [pytest](https://pytest.org/)
- [Selenium](https://www.selenium.dev/)
- [Playwright](https://playwright.dev/)
- Przeglądarka Chrome

## Instalacja
- Aby uruchomić testy, upewnij się, że masz zainstalowane:
  - Python 3.7 lub nowszy
  - pip 
  - Google Chrome (wymagany przez Selenium)
- Sklonuj repozytorium
   ```bash
  git clone https://github.com/aleksandraszczesna/answear_automation_tests.git
   ```
- Zainstaluj wymagane biblioteki
   ```bash
  pip install -r requirements.txt
   ```
- Zainstaluj przeglądarki wymagane przed playwright
   ```bash
  playwright install
   ```

## Uruchamianie testów
Testy są uruchamiane za pomocą "pytest" i mogą być kategoryzowane za pomocą markerów: "api", "smoke" i "regression". Dzięki temu można uruchamiać konkretne zestawy testów w zależności od potrzeb.

Aby uruchomić wszystkie testy w projekcie, należy uruchomić "pytest" bez żadnych parametrów:
   ```bash
   pytest
   ```

Aby uruchomić testy z określonym markerem, np API:
```bash
pytest -m api
```
## Struktura projektu
**`answear-automation-tests/`**
   - `.github/` `Katalog zawierający pliki konfiguracyjne dla GitHub Actions (workflow CI/CD).`
     - `workflows/`
       - `tests.yml`
   - `projekt_zaliczeniowy/`
     - `configuration/`
       - `config.yaml` `Plik konfiguracyjny, w którym przechowywane są ustawienia testów, np. dane do logowania, konfiguracja przeglądarek itp.`
     - `screenshots/`
       - `komunikat_bledu_email.png.py`'
     - `services/`
       - `koszyk/`
         - `koszyk.py`
       - `logowanie/`
         - `logowanie.py`
       - `sortowanie/`
         - `sortowanie.py`
       - `utils/`
         - `base_test_utils.py`
       - `wylogowanie/`
         - `wylgoowanie.py`
     - `tests/` `Folder zawierający same testy automatyczne, podzielone na różne kategorie.`
       - `api/` `Testy związane z API sklepu.`
         - `test_products.py`
         - `test_user.py`
       - `testy_koszyka/`
         - `test_dodawania_do_koszyka.py`
         - `test_usuwania_z_koszyka.py`
         - `test_zmiana_ilości_w_koszyku.py`
       - `testy_logowania/`
         - `test_bledne_haslo.py`
         - `test_bledny_adres_email.py`
         - `test_brak_adresu_eamil.py`
         - `test_brak_hasla.py`
         - `test_poprawne_dane.py`
       - `testy_sortowania/`
         - `test_sortowanie_po_najniższej_cenie.py`
         - `test_sortowanie_po_najwyższej_cenie.py`
         - `test_sortowanie_po_nowości.py`
         - `test_sortowanie_po_popularności.py`
         - `mobile/` `Testy dostosowane do wersji mobilnej strony.`
           - `test_mobile_sortowanie_po_najniższej_cenie.py`
           - `test_mobile_sortowanie_po_najwyższej_cenie.py`
           - `test_mobile_sortowanie_po_nowości.py`
           - `test_mobile_sortowanie_po_popularności.py`
       - `testy_wylogowania/`
         - `test_wylogowanie.py`
   - `requirements.txt` `Zależności projektu`
   - `pytest.ini` `Konfiguracja pytest`
   - `README.md`

## Integracja ciągła (CI) i raportowanie
Testy automatyczne są uruchamiane w ramach GitHub Actions w następujących przypadkach:
na każde wypchnięcie zmian (push) do repozytorium,
przy otwarciu lub aktualizacji Pull Requesta (pull_request),
codziennie o godzinie 9:00 UTC (11:00 czasu polskiego),
ręcznie z poziomu interfejsu GitHub (workflow_dispatch) z możliwością wyboru markera testowego.

### Obsługiwane markery testów:
- regression – domyślny zestaw testów regresyjnych,
- smoke – podstawowe testy sprawdzające stabilność środowiska,
- api – testy REST API.

### Raport z testów
Po każdym przebiegu CI generowany jest raport w formacie Allure, który automatycznie publikowany jest na GitHub Pages:
  - [Kliknij tutaj, aby zobaczyć najnowszy raport Allure](https://aleksandraszczesna.github.io/answear_automation_tests/)

Raport zawiera wyniki wszystkich uruchomionych testów wraz ze statystykami, logami oraz ewentualnymi błędami.