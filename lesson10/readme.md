## Запуск тестов и генерация отчёта Allure

1. Установить зависимости: `pip install -r requirements.txt`
2. Запустить тесты с генерацией результатов Allure: `pytest --alluredir=allure-results`
3. Сгенерировать и открыть отчёт: `allure serve allure-results`