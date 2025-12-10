from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

gecko_driver_path: str = r'C:\Users\user\Downloads\gecko_driver\geckodriver.exe'
service: Service = Service(executable_path=gecko_driver_path)
driver = webdriver.Firefox()

class Shop:
    
    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.saucedemo.com/")

    def login(self, login, password):
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        user_name.send_keys(login)
        password.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def add_items(self, item_id):
        self.driver.find_element(By.ID, item_id).click()

    def user_info(self, user_info_id, user_info):
        self.driver.find_element(By.ID, user_info_id).send_keys(user_info)

    def assert_result(self):
         total = self.driver.find_element(By.CSS_SELECTOR, "summary_total_label")
         total_sum = f"{total}"
         return  total_sum

