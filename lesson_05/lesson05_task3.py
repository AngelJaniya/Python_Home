from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/inputs")
input_elem = driver.find_element(By.CSS_SELECTOR, "input")
input_elem.send_keys("Sky")
sleep(1)
input_elem.clear()
sleep(1)
input_elem.send_keys("Pro")
sleep(1)
driver.quit()
