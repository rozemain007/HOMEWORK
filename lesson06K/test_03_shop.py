from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
def test_shop():
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    user_name = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.ID, "password")

    user_name.send_keys("standard_user")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    items = ["add-to-cart-sauce-labs-backpack", "add-to-cart-sauce-labs-bolt-t-shirt", "add-to-cart-sauce-labs-onesie"]
    for item in items:
        driver.find_element(By.ID, item).click()

    #driver.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()
    
    
    driver.find_element(By.ID, "first-name").send_keys("Анастасия")
    driver.find_element(By.ID, "last-name").send_keys("Иванова")
    driver.find_element(By.ID, "postal-code").send_keys("450247")

    driver.find_element(By.ID, "continue").click()

    total = driver.find_element(By.CSS_SELECTOR, "summary_total_label")
    total_sum = f"{total}"
    assert total_sum == "58.29"

    driver.quit()



