Тестовое задание

Хасанов Рахмидин

```
Сервис для создания и просмотра магазинов в разных городах
```

Запуск

```
 1. git clone https://github.com/rahmiddin/TestCase.git
 2. cd TestCase
 3. pip install -r requirements.txt
 4. cd Shop
 5. python manage.py runserver
```

Доступ

```
 Адмиика: http://127.0.0.1:8000/admin
 
 user: superuser
 
 password: qwerty
```
Запросы
```
GET /city/ — получение всех городов из базы;
GET /city/id/ - получение города по id;
GET /city/create/ - создание города;
GET /city/<city_id>/street/ — получение всех улиц города; (city_id — идентификатор города)
GET /street/create/ - создание улицы;
POST /shop/create — создание магазина; Данный метод получает json c объектом магазина, в ответ возвращает id созданной записи.
GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
```
