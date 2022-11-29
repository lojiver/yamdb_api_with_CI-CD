
### Проект api_yamdb:

Проект api_yamdb позволяет собирать отзывы на Книги, Фильмы и Музыка. Пользователи зарегистрированные на проекте, могут сами делать отзывы, оставлять комментарии и ставить оценки.

### Шаблон наполнения .env-файла:
DB_ENGINE=django.db.backends.postgresql
DB_NAME=name
POSTGRES_USER=user
POSTGRES_PASSWORD=password
DB_HOST=db
DB_PORT=5432

### Как запустить проект:
![workflow](https://github.com/lojiver/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)


Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/lojiver/api_yamdb
```

```
cd infra
```

Собрать и запустить контейнер

```
docker-compose up -d --build 
```


### Примеры запросов:

Вывод произведений:
```
http://localhost/api/v1/titles/
```

Вывод отзывов:
```
http://localhost/api/v1/titles/{title_id}/reviews/
```

Вывод комментариев:
```
http://localhost/api/v1/titles/{title_id}/reviews/{review_id}/
```