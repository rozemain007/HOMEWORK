import allure
from page_object.methods import Api_methods
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjIzNjM4MzEwLCJpYXQiOjE3NjU1MjgxODYsImV4cCI6MTc2NTUzMTc4NiwidHlwZSI6MjAsImp0aSI6IjAxOWIxMWFlLTJmZGItN2MzMS1iOTMzLTcxYjZmYjEzOWYyMCIsInJvbGVzIjoxMH0.1YUC6c4AwitLQBeuM2PQg7ih7DeoyGp8N7etimlt9DI"
base_url = "https://web-agr.chitai-gorod.ru/web/api/v2/search"


@allure.title("Поиск введен кириллицей")
def test_search_kir():
    url = Api_methods(base_url)
    with allure.step("Отправляем запрос кириллицей и получаем status_code"):
        search = Api_methods.search(url, token, "Читай" )
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search == 200


@allure.title('Поиск введен латиницей')
def test_search_lat():
    url = Api_methods(base_url)
    with allure.step("Отправляем запрос латиницей и получаем status_code"):
        search = Api_methods.search(url, token, "Read")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search == 200


@allure.title("Поиск введен цифрами")
def test_search_int():
    url = Api_methods(base_url)
    with allure.step("Отправляем запрос цифрами и получаем status_code"):
        search = Api_methods.search(url, token, "12122025")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search == 200


@allure.title("Поиск без авторизации")
def test_no_auth():
    url = Api_methods(base_url)
    with allure.step("Отправляем запрос без токена авторизации"):
        search = Api_methods.search(url, "", "Search")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search == 401


@allure.title("Поиск с пустым запросом")
def test_none_str():
    url = Api_methods(base_url)
    with allure.step("Отправляем пустой запрос"):
        search = Api_methods.search(url, token, "")
    with allure.step("Сравниваем статус-код с ожидаемым"):
        assert search == 422