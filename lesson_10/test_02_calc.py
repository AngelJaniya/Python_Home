import pytest
import allure
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


@allure.title("Вычисления калькулятора с искусственной задержкой")
@allure.description("Тест проверяет корректность расчета " +
                    "суммы двух чисел после установки таймера задержки.")
@allure.feature("Calculator")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_submission_flow(driver):
    page = CalcPage(driver)

    with allure.step("Открытие страницы калькулятора"):
        page.open()

    with allure.step("Установка времени задержки выполнения"):
        page.fill_delay()

    with allure.step("Ввод данных для вычисления"):
        page.fill_form()

    with allure.step("Ожидание и проверка результата вычисления"):
        result = page.check_result()
        assert result
