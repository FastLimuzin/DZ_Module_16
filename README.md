# Домашняя работа - Модуль 16 (Django)

## Задание 1
- Создано приложение `users` с моделью `User`.
- Подключена база MS SQL Server.

## Задание 2
- Установлена библиотека `Pillow` для работы с изображениями.
- Создано приложение `posts` с моделями `Post` и `Comment`.
- Настроены `STATIC` и `MEDIA`.
- Добавлены функции `post_list` и `post_detail` с шаблонами на русском языке.

## Установка
1. Склонируйте репозиторий: `git clone <your-repo-link>`
2. Создайте виртуальное окружение: `python -m venv venv`
3. Активируйте: `venv\Scripts\activate` (Windows)
4. Установите зависимости: `pip install -r requirements.txt`
5. Установите драйвер: [ODBC Driver 18 for SQL Server](https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)
6. Скопируйте `.env_sample` в `.env` и настройте параметры базы.
7. Создайте базу в MS SQL Server: `CREATE DATABASE your_db_name;`
8. Примените миграции: `python manage.py migrate`
9. Создайте суперпользователя: `python manage.py createsuperuser`
10. Запустите сервер: `python manage.py runserver`

## Использование
- Главная страница: `http://127.0.0.1:8000/` — список постов.
- Админка: `http://127.0.0.1:8000/admin/` — управление пользователями и постами.n manage.py runserver`py runserver`