import allure
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.api
@allure.feature("API")
@allure.story("Poprawne pobranie danych o dostępnych produktach")
def test_products_success():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        request_body = {
            "sort": "",
            "filters": {},
            "productsPerPage": 80,
            "category": "ona",
            "page": 1,
            "urlParams": "",
            "categoryTreeRequired": True,
            "pseudocategory": "nowosci-menu"
        }
        headers = {"x-tamago-api-version": "3.8", "x-tamago-app": "frontApp", "x-tamago-locale": "pl"}
        response = request_context.post("https://answear.com/api/products", data=request_body, headers=headers)

        status = response.status
        assert status == 200

        response_body = response.json()
        assert response_body["category"]["name"] == "Ona"
        assert len(response_body["items"]) == 80
        assert response_body["pseudocategory"]["name"] == "Nowo\u015bci w answear"

@pytest.mark.api
@pytest.mark.regression
@allure.feature("API")
@allure.story("Błędne pobranie danych o dostępnych produktach")
def test_products_failure():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        # ustawiamy niedozwoloną liczbę produktów na stronie
        request_body = {
            "sort": "",
            "filters": {},
            "productsPerPage": 200,
            "category": "ona",
            "page": 1,
            "urlParams": "",
            "categoryTreeRequired": True,
            "pseudocategory": "nowosci-menu"
        }
        headers = {"x-tamago-api-version": "3.8", "x-tamago-app": "frontApp", "x-tamago-locale": "pl"}
        response = request_context.post("https://answear.com/api/products", data=request_body, headers=headers)

        status = response.status
        assert status == 422

        response_body = response.json()
        print(response_body)
        assert response_body["type"] == "requestValidationFailed"
        assert response_body["title"] == 'error in request validation'
        assert response_body["errors"]["children"]['productsPerPage']['errors'] == ['Ta wartość powinna być mniejsza bądź równa 80.']