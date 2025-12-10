from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from po_shop.shop import Shop

# Укажите путь к GeckoDriver, если он не в PATH
gecko_driver_path: str = r'C:\Users\user\Downloads\gecko_driver\geckodriver.exe'
service: Service = Service(executable_path=gecko_driver_path)
driver = webdriver.Firefox()

def test_shop():
    shop = Shop(driver)
    shop.login(driver, "standard_user", "secret_sauce")
    shop.add_items("add-to-cart-sauce-labs-backpack")
    shop.add_items("add-to-cart-sauce-labs-bolt-t-shirt")
    shop.add_items("add-to-cart-sauce-labs-onesie")

    driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    shop.user_info("first-name", "Анастасия")
    shop.user_info("last-name", "Иванова")
    shop.user_info("postal-code", "450247")

    driver.find_element(By.ID, "continue").click()

    assert shop.assert_result == "$58.29"

    driver.quit()
