import pytest
import allure
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


@allure.title("Заполнение и отправка веб-формы")
@allure.description("Тест проверяет корректность заполнения " +
                    "обязательных полей формы и успешность её отправки.")
@allure.feature("Web Forms")
@allure.severity(allure.severity_level.NORMAL)
def test_form_submission_flow(driver):
    form_page = FormPage(driver)

    with allure.step("Открытие страницы с формой"):
        form_page.open()

    with allure.step("Заполнение полей формы"):
        form_page.fill_form()

    with allure.step("Отправка формы"):
        form_page.submit_form()

    with allure.step("Проверка результата отправки формы"):
        form_page.check_form_submission()
