from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from time import sleep

edge_driver_path = r"C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))

locators = ["first_name", "last-name", "address", "e-mail", "phone", "zip-code", "city", "country", "job-position", "company"]
info = ["Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "", "Москва", "Россия", "QA", "SkyPro"]

# for i in range(len(locators)):
#     print(i, locators[i])
#     locator = locators[i]
#     element = driver.find_element(By.NAME, locator)
#     element.send_keys(info[i])
#     sleep(1)




driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
element_first_name = driver.find_element(By.NAME, "first-name")
element_second_name = driver.find_element(By.NAME, "last-name")
element_address = driver.find_element(By.NAME, "address")
element_email = driver.find_element(By.NAME, "e-mail")
element_phone = driver.find_element(By.NAME, "phone")
element_zipCode = driver.find_element(By.NAME, "zip-code")
element_city = driver.find_element(By.NAME, "city")
element_country = driver.find_element(By.NAME, "country")
element_jobPosition = driver.find_element(By.NAME, "job-position")
element_company = driver.find_element(By.NAME, "company")

element_first_name.send_keys("Иван")
element_second_name.send_keys("Петров")
element_address.send_keys("Ленина, 55-3")
element_email.send_keys("test@skypro.com")
element_phone.send_keys("+7985899998787")
element_zipCode.send_keys("")
element_city.send_keys("Москва")
element_country.send_keys("Россия")
element_jobPosition.send_keys("QA")
element_company.send_keys("SkyPro")

sleep(3)
button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
button.click()
sleep(5)

