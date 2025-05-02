import allure
import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.test
@allure.feature("API")
@allure.story("Poprawne pobranie informacji czy uzytkownik jest zalogowany")
def test_user_success():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        request_body = {
            "userType": "not logged in"
        }
        headers = {"x-tamago-api-version": "3.8", "x-tamago-app": "frontApp", "x-tamago-locale": "pl"}
        response = request_context.get("https://answear.com/api/user", data=request_body, headers=headers)

        status = response.status
        assert status == 200
        response_body = response.json()
        assert response_body["userType"] == "not logged in"


@pytest.mark.test
@allure.feature("API")
@allure.story("Błędne pobranie informacji czy uzytkownik jest zalogowany")
def test_user_failure():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        request_body = {}
        # nie przekazujemy wymaganych headerów w request
        response = request_context.get("https://answear.com/api/user", data=request_body)

        status = response.status
        assert status == 400

        response_body = response.json()
        assert response_body["success"] == False
        assert response_body["title"] == 'missing Tamago header in request'
        assert response_body["type"] == "missingTamagoHeaderException"
