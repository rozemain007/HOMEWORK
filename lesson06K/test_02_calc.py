from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from time import sleep

edge_driver_path = r"C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()
element = driver.find_element(By.CSS_SELECTOR, "#delay")
element.clear()
element.send_keys(45)
sleep(5)
seven = driver.find_element(By.LINK_TEXT, '#7')
seven.click()
sleep(5)