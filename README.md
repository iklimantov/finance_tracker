# Finance Tracker

Простое веб-приложение для учёта личных финансов на Python с использованием Flask и SQLite.  
Позволяет добавлять, просматривать и удалять расходы, а также фильтровать их по категориям и диапазону дат.

## 🚀 Функционал
- Добавление расходов (сумма, категория, дата, описание)
- Просмотр списка расходов в виде таблицы
- Подсчёт общей суммы
- Фильтрация по категориям
- Фильтрация по диапазону дат
- Удаление записей

## 🛠️ Технологии
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/)
- SQLite (встроенная база данных)

## ⚙️ Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/username/finance-tracker.git
   cd finance-tracker

2. Создайте и активируйте виртуальное окружение (рекомендуется):
   python -m venv venv
source venv/bin/activate   # для Linux / MacOS
venv\Scripts\activate      # для Windows

3. Установите зависимости
pip install -r requirements.txt

4. Запустите приложение
python app.py

5. Откройте в браузере
http://127.0.0.1:5000/


Структура проекта:
finance-tracker/
│
├── app.py                # Flask-приложение (роуты, логика)
├── models.py             # Модель данных (SQLAlchemy)
├── requirements.txt      # Зависимости проекта
├── templates/            # HTML-шаблоны
│   ├── base.html
│   ├── index.html
│   └── add_expense.html
└── .gitignore

