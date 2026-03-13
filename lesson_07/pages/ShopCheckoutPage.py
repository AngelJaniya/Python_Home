from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ShopCheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def fill_form(self):
        self.change_input('#first-name', "Helga")
        self.change_input('#last-name', "Odintsova")
        self.change_input('#postal-code', "0144")
        self.click('#continue')

    def get_total(self):
        result = self.text('.summary_total_label')
        return result.split(" ")[1]

    def change_input(self, selector, value):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).send_keys(value)

    def text(self, selector):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        return self.wait.until(pres).text

    def click(self, selector):
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
