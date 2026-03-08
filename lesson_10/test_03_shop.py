import pytest
import allure
from pages.ShopAuthPage import ShopAuthPage
from pages.ShopBasketPage import ShopBasketPage
from pages.ShopCheckoutPage import ShopCheckoutPage
from pages.ShopMainPage import ShopMainPage
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    # Рекомендуется добавить driver.quit() сюда для консистентности


@allure.title("Оформление заказа в интернет-магазине")
@allure.description("Сквозной тест (e2e): авторизация пользователя, " +
                    "добавление нескольких товаров " +
                    "в корзину, заполнение данных " +
                    "для доставки и проверка итоговой суммы.")
@allure.feature("E-commerce Shop")
@allure.severity(allure.severity_level.BLOCKER)
def test_form_submission_flow(driver):
    auth = ShopAuthPage(driver)
    with allure.step("Открытие страницы магазина и авторизация"):
        auth.open()
        auth.auth()

    main = ShopMainPage(driver)
    with allure.step("Добавление товаров в корзину " +
                     "(backpack, bolt-t-shirt, onesie)"):
        main.add('backpack')
        main.add('bolt-t-shirt')
        main.add('onesie')

    with allure.step("Переход в корзину"):
        main.go_to_basket()

    basket = ShopBasketPage(driver)
    with allure.step("Переход к оформлению заказа (Checkout)"):
        basket.checkout()

    checkout = ShopCheckoutPage(driver)
    with allure.step("Заполнение формы доставки"):
        checkout.fill_form()

    with allure.step("Получение итоговой стоимости заказа"):
        result = checkout.get_total()

    with allure.step("Проверка совпадения итоговой суммы"):
        assert result == "$58.29"

    driver.quit()
