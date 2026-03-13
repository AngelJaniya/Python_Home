from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShopMainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def add(self, name):
        self.click('#add-to-cart-sauce-labs-' + name)

    def go_to_basket(self):
        self.click('.shopping_cart_link')

    def click(self, selector):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
