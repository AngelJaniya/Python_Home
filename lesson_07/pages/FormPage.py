from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def change_input(self, name, value):
        selector = 'input[name="' + name + '"]'
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).send_keys(value)

    def submit_form(self):
        selector = 'button[type="submit"]'
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()

    def check_result(self, name, cls):
        selector = '#' + name
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        classes = self.wait.until(pres).get_attribute('class')
        assert cls in classes

    def open(self):
        page = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.driver.get(page)

    def fill_form(self):
        for f, v in self.fields.items():
            self.change_input(f, v)

    def check_form_submission(self):
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for f in fields:
            self.check_result(f, 'alert-success')

        self.check_result('zip-code', 'alert-danger')
