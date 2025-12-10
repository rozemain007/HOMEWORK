from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from page_hw.calculator import Calculator
edge_driver_path = r"C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Chrome()

def test_02_calc():

    calculator = Calculator(driver)
    calculator.delay("1")
    calculator.click_button("7")
    calculator.click_button("+")
    calculator.click_button("8")
    calculator.click_button("=")
    result = calculator.return_result("15")
    assert result == "15"

    driver.quit()

