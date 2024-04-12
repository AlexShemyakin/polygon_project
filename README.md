# Веб-сервис, позволяющий вносить и сохранять координаты в виде PolygonField.

## Запуск проекта
### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:AlexShemyakin/polygon_project.git
```

### Cоздать и активировать виртуальное окружение:

```
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
```

### Выполнить миграции и сбор статики:

```
cd ../poligon_proj
python manage.py migrate
python manage.py collectstatic
```

### Создать суперпользователя для администрирования сайта:

```
python manage.py createsuperuser
```
Теперь локальный сервер доступен по адресу http://127.0.0.1:8000/
И страница администрирования http://127.0.0.1:8000/admin/

## Запуск проекта через контейнеры
### Записать переменные окружения в .env. Пример приведен в .env_example.

### Для локального запуска следует запустить docker-compose.yml:

```
cd infra
sudo docker compose -f docker-compose.yml up -d
```
Создание контейнеров выполняется, но контейнер backend сразу падает из-за ошибки нахождения библиотеки gdal.
На ПК она установлена, но при попытках указать проекту на данную либу, ничего не находится.
А как оказалось, инструмент pip не может ее установить.

### Выполнить миграции и сбор статических файлов (При успешном создании контейнеров):

```
sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
```

### Создать суперпользователя для доступа к администрированию сайта (При успешном создании контейнеров):

```
cd ../poligon_proj
python manage.py createsuperuser
```
Теперь локальный сервер доступен по адресу http://127.0.0.1:8000/

## Работа с API (в моем случае применялся Postman)
### GET выполнятся по следующему запросу

```
  http://127.0.0.1:8000/api/polygon/
```

### POST выполняется по следующему запросу

```
http://127.0.0.1:8000/api/polygon/
```

### PATCH выполняется по следующему запросу

```
http://127.0.0.1:8000/api/polygon/{id}/
```

#### При POST и PATCH запросах, необходимо вводить координаты с первым пробелом 

```
{
    "name": "testing_polygon",
    "area": " 69 174 69 204 62 205 62 173"
}
```

### DELETE выполняется по следующему запросу

```
http://127.0.0.1:8000/api/polygon/{id}/
```

## Автор проекта
[Шемякин Александр](https://github.com/AlexShemyakin)

## Стек технологий
Разработка:

[Django]
[Python]
[DRF]
[PostgreSQL]

[Docker]
[Gunicorn]
