# api_final

api final

### Описание

Проект «API для Yatube»

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/leonid-lovsky/api_final_yatube.git
```

```
cd api_final_yatube
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

### Примеры

- Получение публикаций
```
GET /api/v1/posts/
```
```
Array [
    id: integer (id публикации)
    author: string (username пользователя)
    text: string (текст публикации)
    pub_date: string <date-time>
    image: string or null <binary>
    group: integer or null (id сообщества)
]
```
- Получить список всех комментариев для выбранной публикации
```http://localhost:8000/api/v1/posts/1/comments/```
```
GET /api/v1/posts/1/comments/
```
```
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "id": 1,
        "author": "yadmin",
        "text": "первый тестовый коммент для первого поста",
        "created": "2020-04-23T12:59:14.096584Z",
        "post": 1
    },
    ...
]
```

[Полная докуменация](http://localhost:8000/redoc/)