from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/dynamicid")
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
blue_button.click()

sleep(1)
