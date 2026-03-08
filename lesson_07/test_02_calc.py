import pytest
from pages.CalcPage import CalcPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    page = CalcPage(driver)
    page.open()
    page.fill_delay()
    page.fill_form()
    result = page.check_result()
    assert result
