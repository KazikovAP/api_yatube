# CRUD API для Yatube

Многофункциональный API для социальной сети Yatube.

---
## Описание возможностей проекта

- Аутентификация по токену
- Получение, cоздание, обновление и удаление публикаций и комментариев;
- Получение информации о сообществах;

---
## Технологии
* Python 3.9
* Django 3.2
* djangorestframework 3.12.4

---
## Установка и запуск

Для MacOs и Linux вместо python использовать python3

**1. Клонировать репозиторий:**
```
git clone https://github.com/KazikovAP/api_yatube.git
```

**2. Перейти в папку проекта:**
```
cd /api_yatube/
```

**3. Cоздать и активировать виртуальное окружение:**
```
python -m venv venv
```

Для Windows:
```
source venv/Scripts/activate
```

Для MacOs/Linux:
```
source venv/bin/activate
```

**4. Установить зависимости из файла requirements.txt:**
- Обновить пакетный менеджер pip
```
python -m pip install --upgrade pip
```

- Установить зависимости
```
pip install -r requirements.txt
```

**5. Создать и запустить миграции:**
- Перейти в папку yatube
```
cd /yatube_api/
```

- Создать миграции
```
python manage.py makemigrations
```

- Применить миграции
```
python manage.py migrate
```

**6. Запустить сервер:**
```
python manage.py runserver
```

> После выполнения вышеперечисленных инструкций проект доступен по адресу http://127.0.0.1:8000/

---
## Отправка, получение и обновление данных

---
### Примеры ответов на запросы для неаутентифицированных пользователей

> Для анонимных пользователей возможны только GET-запросы.

**1. GET-запрос на эндпоинт http://127.0.0.1:8000/api/v1/posts/**

    ```json
    [
    {
        "id": 1,
        "author": "test_user1",
        "image": "http://127.0.0.1:8000/media/posts/photo_2023-03-17_20.53.10.jpeg",
        "text": "Текст тестового поста",
        "pub_date": "2023-03-18T08:55:29.789186Z",
        "group": 1
    },
    {
        "id": 2,
        "author": "test_user2",
        "image": null,
        "text": "Текст тестового поста 2",
        "pub_date": "2023-03-18T09:05:39.315442Z",
        "group": null
    }
    ]
    ```

**2. GET-запрос на эндпоинт http://127.0.0.1:8000/api/v1/groups/**

     ```json
     [
    {
        "id": 1,
        "title": "Тестовая группа 1",
        "slug": "test_1",
        "description": "Описание тестовой группы 1"
    },
    {
        "id": 2,
        "title": "Тестовая группа 2",
        "slug": "test_2",
        "description": "Описание тестовой группы 2"
    }
    ]
     ```

---
### Примеры запросов для аутентифицированных пользователей

> Изменение чужого контента запрещено.

**1. POST-запрос на эндпоинт http://127.0.0.1:8000/api/v1/posts/ (создание публикации)**
   
    Тело запроса:
    ```json
    {
    "text": "Тестовый пост 3",
    "group": 1
    }
    ```
    Ответ эндпоинта:
    
    ```json
    {
    "id": 3,
    "author": "test_user1",
    "image": null,
    "text": "Тестовый пост 3",
    "pub_date": "2023-03-18T09:16:42.536210Z",
    "group": 1
    }
    ```

---
## Разработал:
[Aleksey Kazikov](https://github.com/KazikovAP)

---
## Лицензия:
[MIT](https://opensource.org/licenses/MIT)

