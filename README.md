# Django Homework - Module 16-1

## Задание 1
- Создан проект с приложением `users`.
- Модель `User` добавлена в админку.
- Подключение к MS SQL Server.

## Установка
1. Клонируйте: `git clone <your-repo-link>`
2. Создайте venv: `python -m venv venv`
3. Активируйте: `venv\Scripts\activate` (Windows)
4. Установите: `pip install -r requirements.txt`
5. Установите `ODBC Driver 18 for SQL Server`: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server
6. Скопируйте `.env_sample` в `.env` и настройте параметры базы.
7. Создайте базу в MS SQL Server: `CREATE DATABASE your_db_name;`
8. Миграции: `python manage.py migrate`
9. Суперпользователь: `python manage.py createsuperuser`
10. Запуск: `python manage.py runserver`