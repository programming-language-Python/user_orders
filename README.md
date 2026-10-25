# Стек технологий
- FastAPI
- SQLAlchemy
- Pydantic
- alembic
- PostgreSQL
- faker

# Демонстрация работы
![Демонстрация работы.mp4](%D0%94%D0%B5%D0%BC%D0%BE%D0%BD%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B.mp4)

# Запуск
Ввести команды в консоли
1. 
```cmd
cd user_orders
```
2. 
```cmd
pip install -r requirements.txt
```
3.
```cmd
python -m venv venv
```

```cmd
.\venv\Scripts\activate
```
4. Переименовать .env.example в .env и заполнить файл данными для подключения к PostgreSQL
5. Ввести в консоли
```cmd
alembic upgrade head
```
6. Запустить файл для заполнения тестовыми данными БД
```cmd
python src/db/fill_db.py
```
7.
```cmd
python main.py
```
8. Перейти по адресу http://127.0.0.1:8000/docs#/

# Условие задания
Есть две SQL таблицы (users и orders) со следующими полями:

users
---------
user_id      INT (PK)
user_name    VARCHAR
city         VARCHAR
reg_date     DATE


orders
---------
order_id     INT (PK)
user_id      INT (FK -> users)
order_date   DATE
amount       DECIMAL
status       VARCHAR  -- возможные значения - 'completed', 'cancelled', 'pending'
is_test      BOOLEAN


НУЖНО:
Для каждого пользователя из города Москва, который зарегистрировался не раньше 2024-01-01, нужно получить его последний по дате заказ со статусом completed и вывести:
user_id
user_name
order_id последнего заказа
order_date последнего заказа
amount последнего заказа
порядковый номер этого заказа в истории пользователя (по возрастанию даты, среди completed заказов)
сумму всех completed заказов пользователя (общая выручка от него)

Тестовые заказы не учитываем. Необходимо отсортировать результат по amount последнего заказа по убыванию. Пользователей без completed заказов в результат не включать.
