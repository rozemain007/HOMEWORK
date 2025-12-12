from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

class Shop:
    
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def login(self, login: str, password: str):
        """
        Авторизация пользователя
        """
        user_name = self.driver.find_element(By.ID, "user-name")
        password_var = self.driver.find_element(By.ID, "password")
        user_name.send_keys(login)
        password_var.send_keys(password)
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

    def add_items(self, item_id: str):
        """
        Добавление товара в корзину
        """
        self.driver.find_element(By.ID, item_id).click()

    def user_info(self, user_info_id: str, user_info: str):
        """
        Добавление информации о клиенте для совершения доставки
        """
        self.driver.find_element(By.ID, user_info_id).send_keys(user_info)

    def assert_result(self) -> str:
        """
        Получение итоговой суммы после добавления товаров в корзину
        """
        total = self.driver.find_element(By.CSS_SELECTOR, "summary_total_label")
        total_sum = f"{total}"
        return  total_sum

