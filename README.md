# API Yatube
API для проекта Yatube

## Зависимости
- Django==2.2.16
- pytest==6.2.4
- pytest-pythonpath==0.7.3
- pytest-django==4.4.0
- djangorestframework==3.12.4
- djangorestframework-simplejwt==4.7.2
- Pillow==8.3.1
- PyJWT==2.1.0
- requests==2.26.0
- djoser==2.1.0

## Установка
Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/leonid-lovsky/api_yatube.git
```

```
cd api_yatube
```

Создать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры

- Получение публикаций

```
GET /api/v1/posts/
```

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "author": "TestUser",
        "image": null,
        "text": "Тестовый пост 1",
        "pub_date": "2022-09-04T16:38:01.699357Z",
        "group": null
    },
    ...
]
```

- Получение публикации

```
GET /api/v1/posts/<post_id>/
```

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "author": "TestUser",
    "image": null,
    "text": "Тестовый пост 1",
    "pub_date": "2022-09-04T16:38:01.699357Z",
    "group": null
}
```

- Получение комментариев

```
GET /api/v1/posts/<post_id>/comments/
```

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "author": "TestUser",
        "text": "Комментарий 1",
        "created": "2022-09-04T16:46:51.990803Z",
        "post": 1
    },
    ...
]
```

- Получение комментария

```
GET /api/v1/posts/<post_id>/comments/<comment_id>/
```

```
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "author": "TestUser",
    "text": "Коммент 1",
    "created": "2022-09-04T16:46:51.990803Z",
    "post": 1
}
```

- Список сообществ

```
GET /api/v1/groups/
```

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "description": "",
        "title": "Группа 1",
        "slug": "group_1"
    },
    ...
]
```

- Информация о сообществе

```
GET /api/v1/groups/
```

```
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "description": "",
    "title": "Группа 1",
    "slug": "group_1"
}
```

- Подписки

```
GET /api/v1/follow/
```

```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "user": "TestUser",
        "following": "TestUser2"
    },
    ...
]
```
