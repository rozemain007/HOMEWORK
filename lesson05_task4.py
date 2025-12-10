from selenium import webdriver
from selenium.webdriver import Firefox
driver = Firefox()
driver.maximize_window()

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver.get("http://the-internet.herokuapp.com/login")

locator_username = '[name = "username"]'
locator_password = '[name = "password"]'
locator_button = 'button'


search_username = driver.find_element(By.CSS_SELECTOR, locator_username)
search_password = driver.find_element(By.CSS_SELECTOR, locator_password)
search_button = driver.find_element(By.CSS_SELECTOR, locator_button)

username = "tomsmith"
password = "SuperSecretPassword!"

search_username.send_keys(username)
search_password.send_keys(password)
search_button.click()

locator_green_board = "[id = 'flash']"
search_green_board = driver.find_element(By.CSS_SELECTOR, locator_green_board)

print(search_green_board.text)

driver.quit()