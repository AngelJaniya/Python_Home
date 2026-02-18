from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")
wait = WebDriverWait(driver, 10)
input_text = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#newButtonName"))
                        )
input_text.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
button.click()

print(button.text)
driver.quit()
