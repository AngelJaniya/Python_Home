import pytest
from selenium import webdriver
from pages.FormPage import FormPage
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def driver():
    url = "https://msedgedriver.microsoft.com/LATEST_RELEASE"
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager(
            url="https://msedgedriver.microsoft.com",
            latest_release_url=url).install())
    )
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_form_submission_flow(driver):
    form_page = FormPage(driver)
    form_page.open()
    form_page.fill_form()
    form_page.submit_form()
    form_page.check_form_submission()
