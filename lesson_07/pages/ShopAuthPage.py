from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShopAuthPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def auth(self):
        self.change_input('#user-name', "standard_user")
        self.change_input('#password', "secret_sauce")
        self.click('#login-button')

    def change_input(self, selector, value):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).send_keys(value)

    def click(self, selector):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
