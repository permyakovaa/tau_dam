# Медиа Сервер

Сервис для хранения медиа файлов компании. Написан на Python и Django

1. Склонировать репо: 
```bash
$ git clone https://gitlab.npo-at.com/backoffice/media-server
```
2. Установить зависимости python mysql
```bash
$ pip install mysqlclient
```
3. Указать настройки mysl
```bash
$ nano /usr/local/etc/my.cnf
```
```bash
[mysqld]
# Only allow connections from localhost
bind-address = 127.0.0.1
mysqlx-bind-address = 127.0.0.1

# my.cnf
[client]
database = atms
user = username
password = password
default-character-set = utf8
```
4. Накатить миграции на БД
```bash
$ python3 manage.py migrate
```
5. Запуск сервера
```bash
$ python3 manage.pu runserver
```

6. Создать супер юзера для админки
```bash
$ python3 manage.py createsuperuser
```

7. Залогиниться в админке /admin