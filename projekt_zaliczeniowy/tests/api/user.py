import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.test
def test_manu_success():
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

@pytest.mark.test
def test_products_failure():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        request_body = {
            "sort": "",
            "filters": {},
            "productsPerPage": 20,
            "category": "ona",
            "page": 1,
            "urlParams": "",
            "categoryTreeRequired": True,
            "pseudocategory": "nowosci-menu"
        }

        response = request_context.post("https://answear.com/api/products", data=request_body)

        status = response.status
        assert status == 400

        response_body = response.json()
        assert response_body["success"] == False
        assert response_body["title"] == 'missing Tamago header in request'
        assert response_body["type"] == "missingTamagoHeaderException"