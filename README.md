# Медиа Сервер

Сервис для хранения медиа файлов компании. Написан на Python и Django

1. Склонировать репо: 
```bash
$ git clone https://gitlab.npo-at.com/backoffice/media-server
```
2. Установить зависимости mysql
```bash
$ sudo apt install mysql-server
$ sudo apt-get install libmysqlclient-dev
```
3. Установить зависимости python
```bash
$ pip3 install mysqlclient
$ pip3 install django-bootstrap-icons
$ pip3 install django-crispy-forms
$ pip3 install crispy-bootstrap5
$ pip3 install django-bootstrap-v5
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
$ python3 manage.py runserver
```

6. Создать супер юзера для админки
```bash
$ python3 manage.py createsuperuser
```

7. Залогиниться в админке /admin

# Для развертки production сервера:
1. pip3 install uwsgi
3. sudo apt-get install nginx

# Сервер ffmpeg для компрессии по задачами из загрузки файлов:
1. sudo apt install ffmpeg
2. sudo apt install zeromq
3. pip3 install pyzmq
4. В корне репо запустить сервер python3 zmq_server.py