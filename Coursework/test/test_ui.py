import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from page_object.methods import UI_methods
driver = webdriver.Chrome()

@allure.title("Поиск товара - валидное значение")
def test_search_val():
    browser = UI_methods(driver)
    search_phrase = "Python"
    browser.send_search_str(search_phrase)
    text = browser.get_founded_book()
    assert search_phrase in text
    driver.quit()

@allure.title("Поиск товара - числа")
def test_search_num():
    browser = UI_methods(driver)
    search_phrase = "123456789"
    browser.send_search_str(search_phrase)
    text = browser.not_founded()
    assert text == "Похоже, у нас такого нет"
    driver.quit()

@allure.title("Поиск товара - юникод в запросе")
def test_search_unicode():
    browser = UI_methods(driver)
    search_phrase = "🥇 ❤"
    browser.send_search_str(search_phrase)
    text = browser.not_founded()
    assert text == "Похоже, у нас такого нет"
    driver.quit()

@allure.title("Добавление товара в корзину")
def test_add_to_basket():
    browser = UI_methods(driver)
    search_phrase = "Python"
    browser.send_search_str(search_phrase)

    driver.implicitly_wait(10)