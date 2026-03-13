from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShopBasketPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def checkout(self):
        self.click('#checkout')

    def click(self, selector):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
