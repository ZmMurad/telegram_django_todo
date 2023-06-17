# Сервис для списка своих дел с поддержкой API и телеграм ботов
Каждое дело привязанно к конкретному пользователю, разные пользователи не могут менять чужие записи или видеть их.
## Установка и запуск

1. Склонировать репозиторий с Github
2. Перейти в директорию проекта
3. Запустить команду 
```
pip install -r requirements.txt
```
4. Создать файл .env заполнить в нем поля 
```
EMAIL_HOST_USER =
EMAIL_HOST_PASSWORD = 
URL_SERVER="127.0.0.1" по умолчанию
PORT="8000" по умолчанию
TOKEN= токет для бота
```

5. Запустить команду
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
6. Запустить в папке telegrambot main.py в другом терминале
```
cd telegrambot
python main.py
```

***
## Маршруты основной страницы

```http://127.0.0.1:8000/ ```

## Маршруты API

# ```http://127.0.0.1:8000/api/v1/does/ ```- GET запрос без параметров для списка своих дел, вы должны быть авторизованы по токену. Токен можно получить на главной странице после регистрации. Авторизация в headers.
Пример:


## request
```
headers={
    "Authorization": f"Token {token}"
}
```

## response
```
{
    "status": "success",
    "data": [
        {
            "id": int:id,
            "title": "new",
            "text": "new",
            "active": true
        },
    ]
}
```

# ```http://127.0.0.1:8000/api/v1/does/ ```- POST запрос с данными title, text для внесения нового дела. Авторизация в headers.
Пример:

## request
```
headers={
    "Authorization": f"Token {token}"
}
data={
    "title":"title_test",
    "text":"text_test"
}
```

## response
```
{
    "title": "postman",
    "text": "postman",
    "active": true
}
```



# ```http://127.0.0.1:8000/api/v1/does/<int:pk>/ ```- GET запрос с токеном для получения текущей записи
Пример:

## request
```
headers={
    "Authorization": f"Token {token}"
}
```

## response
```
{
    "status": "success",
    "data": {
        "id": int:id,
        "title": "new",
        "text": "new",
        "active": true
    }
}
```



# ```http://127.0.0.1:8000/api/v1/does/<int:pk>/ ```- DELETE запрос с токеном для удаления записи
Пример:

## request
```
headers={
    "Authorization": f"Token {token}"
}
```
## response
```

{
    "status": "success"
}
```

# ```http://127.0.0.1:8000/api/v1/does/<int:pk>/ ```- PUT запрос с токеном и новыми данными для изменения записи
Пример:
## request
```
headers={
    "Authorization": f"Token {token}"
}
data={
    "title":"title_test",
    "text":"text_test"
}
```
## response
```
{
    "status": "success",
    "data": {
        "id": int:id,
        "title": "new",
        "text": "new",
        "active": true
    }
}
```
