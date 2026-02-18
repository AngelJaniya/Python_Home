from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

result = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '.bg-success'))
).text
print(result)
driver.quit()
