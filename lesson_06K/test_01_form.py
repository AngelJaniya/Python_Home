from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.microsoft import EdgeChromiumDriverManager


url = "https://msedgedriver.microsoft.com/LATEST_RELEASE"
driver = webdriver.Edge(
    service=EdgeService(EdgeChromiumDriverManager(
        url="https://msedgedriver.microsoft.com",
        latest_release_url=url).install())
)


def change_input(name, value):
    selector = 'input[name="' + name + '"]'
    pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, 4).until(pres).send_keys(value)


def submit():
    selector = 'button[type="submit"]'
    pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    WebDriverWait(driver, 4).until(pres).click()


def check_result(name, cls):
    selector = '#' + name
    pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
    classes = WebDriverWait(driver, 4).until(pres).get_attribute('class')
    assert cls in classes


def test_form():
    page = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(page)
    change_input('first-name', "Иван")
    change_input('last-name', "Петров")
    change_input('address', "Ленина, 55-3")
    change_input('city', "Москва")
    change_input('country', "Россия")
    change_input('e-mail', "test@skypro.com")
    change_input('phone', "+7985899998787")
    change_input('job-position', "QA")
    change_input('company', "SkyPro")

    submit()

    check_result('first-name', 'alert-success')
    check_result('last-name', 'alert-success')
    check_result('address', 'alert-success')
    check_result('city', 'alert-success')
    check_result('country', 'alert-success')
    check_result('e-mail', 'alert-success')
    check_result('phone', 'alert-success')
    check_result('job-position', 'alert-success')
    check_result('company', 'alert-success')
    check_result('zip-code', 'alert-danger')

    driver.quit()
