## Стек технологий

* Python 3
* FastAPI
* SQLAlchemy
* PostgreSQL
* Uvicorn

---

## Структура проекта

```
app/
 ├── api/
 │    ├── books.py
 │    └── categories.py
 ├── db/
 │    ├── crud.py
 │    ├── db.py
 │    └── models.py
 ├── schemas.py
 └── main.py

examples/ (скриншоты работы API)
requirements.txt
README.md
```

## Запуск проекта

### 1. Клонирование репозитория

```bash
git clone https://github.com/grandis0n/octagon-example.git
cd octagon-example
```

### 2. Создание виртуального окружения

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Настройка подключения к PostgreSQL

В файле `app/db/db.py` необходимо указать строку подключения к базе данных:

```
postgresql://username:password@localhost:5432/dbname
```

Перед запуском убедитесь, что PostgreSQL запущен и база данных создана.

### 5. Запуск API

```bash
uvicorn app.main:app --reload
```

После запуска API будет доступно по адресу:

```
http://127.0.0.1:8000
```

Swagger-документация:

```
http://127.0.0.1:8000/docs
```

---

## Основные эндпоинты

### Categories

* GET `/categories` — получить список категорий
* GET `/categories/{id}` — получить категорию по id
* POST `/categories` — создать категорию
* PUT `/categories/{id}` — обновить категорию
* DELETE `/categories/{id}` — удалить категорию

### Books

* GET `/books` — получить список книг
* GET `/books/{id}` — получить книгу по id
* GET `/books?category_id=1` — фильтрация книг по категории
* POST `/books` — создать книгу
* PUT `/books/{id}` — обновить книгу
* DELETE `/books/{id}` — удалить книгу

---

## Проверка работы API

После запуска сервера тестирование API выполнялось через:

* Swagger UI
* Postman
* psql (проверка данных в базе)

Скриншоты выполнения запросов и состояния базы данных находятся в папке:

```
examples/
```
