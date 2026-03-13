import pytest
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


def test_form_submission_flow(driver):
    auth = ShopAuthPage(driver)
    auth.open()
    auth.auth()

    main = ShopMainPage(driver)
    main.add('backpack')
    main.add('bolt-t-shirt')
    main.add('onesie')
    main.go_to_basket()

    basket = ShopBasketPage(driver)
    basket.checkout()

    checkout = ShopCheckoutPage(driver)
    checkout.fill_form()
    result = checkout.get_total()

    driver.quit()

    assert result == "$58.29"
