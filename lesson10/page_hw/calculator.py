from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay(self, delay):
        """
        Находим элемент по локатору "delay" и отправляем в него нужное значение
        """
        element = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        element.clear()
        element.send_keys(delay)

    def click_button(self, button):
        f"""
        Находим кнопку {button} и кликаем на неё
        """
        xpath = f"//span[text()='{button}']"
        self.driver.find_element(By.XPATH, xpath).click()

    def return_result(self, result) -> str:
        """
        Получаем результат работы калькулятора
        """
        WebDriverWait(self.driver, 46).until(

            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), f'{result}')

        )

        act_result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text

        return act_result


