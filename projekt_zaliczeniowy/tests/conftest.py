import pytest
import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    print("screen1")
    if report.when == "call" and report.failed:
        print("screen2")
        driver = item.funcargs.get("browser")
        if driver:
            print("screen3")
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="Failure Screenshot",
                attachment_type=allure.attachment_type.PNG
            )