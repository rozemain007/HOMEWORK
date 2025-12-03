from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from time import sleep

edge_driver_path = r"C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Chrome()

def test_02_calc():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    element = driver.find_element(By.CSS_SELECTOR, "#delay")
    element.clear()
    element.send_keys("45")
    xpath = f"//span[text()='7']"
    driver.find_element(By.XPATH, xpath).click()

    xpath = f"//span[text()='+']"
    driver.find_element(By.XPATH, xpath).click()

    xpath = f"//span[text()='8']"
    driver.find_element(By.XPATH, xpath).click()

    xpath = f"//span[text()='=']"
    driver.find_element(By.XPATH, xpath).click()

    result = WebDriverWait(driver, 46).until(

        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")

    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text

    assert result

