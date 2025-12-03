from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(50)
driver.get("https://www.saucedemo.com")

User_name = driver.find_element(By.ID, "user-name")
password = driver.find_element(By.ID, "password")

User_name.send_keys("standard_user")
password.send_keys("secret_sauce")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
