from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/" +
            "selenium-webdriver-java/slow-calculator.html")

    def fill_delay(self):
        delay_field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.send_keys("45")

    def fill_form(self):
        self.driver.find_element(By.XPATH, "//*[text()='7']").click()
        self.driver.find_element(By.XPATH, "//*[text()='+']").click()
        self.driver.find_element(By.XPATH, "//*[text()='8']").click()
        self.driver.find_element(By.XPATH, "//*[text()='=']").click()

    def check_result(self):
        result = self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.screen'), '15')
        )

        return result
