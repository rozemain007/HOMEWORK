import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
base_url = "https://web-agr.chitai-gorod.ru/web/api/v2/search"

class Api_methods():
    def __init__(self, base_url):
        self.base_url = base_url

    def search(self, bearer_token: str, phrase: str) -> int:
        """
        Поиск по ключевым словам
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {bearer_token}"
        }

        params = {
            "customerCityId": 213,
            "phrase": phrase,
            "abTestGroup": 1
        }

        req = requests.get(self.base_url + "/search-phrase-suggests?suggests%5Bpage%5D=1&suggests%5Bper-page%5D=5&phrase=Уна Харт&abTestGroup=1&include=authors%2CbookCycles%2Ccategories%2Cpublishers%2CpublisherSeries%2Cproducts",
            headers=headers, params=params)

        return req.status_code

class UI_methods():

    def __init__(self, driver):
        self.driver = driver

    def send_search_str(self, search_str: str) -> str:
        """
        Поиск по ключевым словам
        """
        self.driver.maximize_window()
        self.driver.get("https://www.chitai-gorod.ru/")
        button = self.driver.find_element(By.NAME, "search")
        button.send_keys(search_str)
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.text_to_be_present_in_element_attribute((By.NAME, "search"), "value", search_str))
        button.send_keys(Keys.RETURN)

    def get_founded_book(self):
        """
        Находим первый элемент поиска
        """
        wait = WebDriverWait(self.driver, 20)
        search_page_loc = (By.CSS_SELECTOR, "h1.search-title__head")
        wait.until(EC.presence_of_element_located(search_page_loc))

        title = self.driver.find_element(By.CSS_SELECTOR, 'a.product-card__title')
        text_title = title.text
        return text_title

    def not_founded(self) -> str:
        wait = WebDriverWait(self.driver, 20)
        not_found_locator = (By.CSS_SELECTOR, 'h4.catalog-stub__title')
        wait.until(EC.presence_of_element_located(not_found_locator))

        not_found = self.driver.find_element(By.CSS_SELECTOR, 'h4.catalog-stub__title')
        text = not_found.text
        return text

    def add_book(self):
        """
        Добавление в корзину
        """
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.search-title__head")))

        self.driver.implicitly_wait(10)
        self.driver.execute_script("window.scrollBy(0, 800);")

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-buttons.product-card__actions")))
        self.driver.find_element(By.CSS_SELECTOR, 'div.product-buttons.product-card__actions').click()





