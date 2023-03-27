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
GET /city/city_id/street/ - получение улиц по city_id;
POST /shop/ - Создание магазина
GET  /shop/?street=&city= — получение списка магазинов ;
```
