from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/login")
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")

password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

login_buttom = driver.find_element(By.CSS_SELECTOR, ".radius")
login_buttom.click()

alert = driver.find_element(By.CSS_SELECTOR, "#flash")
print(alert.text)
sleep(1)
driver.quit()
