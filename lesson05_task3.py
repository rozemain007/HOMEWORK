from selenium import webdriver
from selenium.webdriver import Firefox
from time import sleep
driver = Firefox()
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/inputs")
sleep(10)
input_locator = "input"
search_input = driver.find_element(By.CSS_SELECTOR, input_locator)

search_input.send_keys("Sky")
sleep(5)
search_input.clear()
search_input.send_keys("Pro")
sleep(5)
driver.quit()