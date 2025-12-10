from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

blue_button_locator = "[class='btn class2 btn-primary btn-test']"
searh_blue_button = driver.find_element(By.CSS_SELECTOR, blue_button_locator)
print("Я нашел голубую кнопку!!!")
searh_blue_button.click()
print("Я кликнула на голубую кнопку!!!")

sleep(10)
