import allure
from selenium import webdriver
from page_hw.calculator import Calculator
edge_driver_path = r"C:\Users\user\Downloads\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Chrome()


@allure.title("Тестирование калькулятора")
@allure.description("Тестирование соответсвия итогового значения ожидаемому")
@allure.feature("READ")
@allure.severity("Medium")
def test_02_calc():
    with allure.step("Открытие калькулятора"):
        calculator = Calculator(driver)

    with allure.step("Вводим значение ожидания"):
        calculator.delay("45")

    with allure.step("Нажимаем на кнопки для совершения матем. операции"):
        calculator.click_button("7")
        calculator.click_button("+")
        calculator.click_button("8")
        calculator.click_button("=")

    with allure.step("Получаем результат математической операции"):
        result = calculator.return_result("15")

    with allure.step("Сравниваем ожидаемый результат с фактическим"):
        assert result == "15"

    driver.quit()
