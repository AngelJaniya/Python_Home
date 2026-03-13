from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))


def change_input(selector, value):
    pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, 4).until(pres).send_keys(value)


def click(selector):
    pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, 4).until(pres).click()


def text(selector):
    pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    return WebDriverWait(driver, 4).until(pres).text


def test_form():
    driver.get("https://www.saucedemo.com/")

    change_input('#user-name', "standard_user")
    change_input('#password', "secret_sauce")
    click('#login-button')

    click('#add-to-cart-sauce-labs-backpack')
    click('#add-to-cart-sauce-labs-bolt-t-shirt')
    click('#add-to-cart-sauce-labs-onesie')
    click('.shopping_cart_link')
    click('#checkout')

    change_input('#first-name', "Helga")
    change_input('#last-name', "Odintsova")
    change_input('#postal-code', "0144")
    click('#continue')

    result = text('.summary_total_label')
    print(result)

    driver.quit()

    assert result.split(" ")[1] == "$58.29"
