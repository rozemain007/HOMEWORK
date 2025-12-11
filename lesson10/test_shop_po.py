from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from po_shop.shop import Shop
import allure

# Укажите путь к GeckoDriver, если он не в PATH
gecko_driver_path: str = r'C:\Users\user\Downloads\gecko_driver\geckodriver.exe'
service: Service = Service(executable_path=gecko_driver_path)
driver = webdriver.Firefox()

@allure.title("Тестирование магазина")
@allure.description("Тестирование соответсвия итоговой суммы покупок ожидаемой суммы")
@allure.feature("READ")
@allure.severity("Medium")
def test_shop():
    with allure.step("Открываем магазин"):
        shop = Shop(driver)

    with allure.step("Авторизуемся в магазине"):
        shop.login(driver, "standard_user", "secret_sauce")

    with allure.step("Добавляем товары в корзину"):
        shop.add_items("add-to-cart-sauce-labs-backpack")
        shop.add_items("add-to-cart-sauce-labs-bolt-t-shirt")
        shop.add_items("add-to-cart-sauce-labs-onesie")

    with allure.step("Переходим в корзину"):
        driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
        driver.find_element(By.ID, "checkout").click()

    with allure.step("Вводим личные данные пользователя для доставки"):
        shop.user_info("first-name", "Анастасия")
        shop.user_info("last-name", "Иванова")
        shop.user_info("postal-code", "450247")

    with allure.step("Отправляем данные о пользователе"):
        driver.find_element(By.ID, "continue").click()

    with allure.step("Получаем итоговую сумму покупки, сравниваем её с ожидаемой"):
        assert shop.assert_result == "$58.29"

    driver.quit()
