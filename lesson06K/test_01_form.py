from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

edge_driver_path = r"C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

locators = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
info = ["Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro"]

def test_01_form():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    for loc, value in zip(locators, info):
        driver.find_element(By.NAME, loc).send_keys(value)

    button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()

    for field_id in locators:
        field = driver.find_element(By.ID, field_id)
        assert "success" in field.get_attribute("class")

    zip_code = driver.find_element(By.ID, "zip-code")
    assert "danger" in zip_code.get_attribute('class')

    driver.quit()


