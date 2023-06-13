# Базовый образ, который содержит Python
FROM python:3.8-slim-buster

# Установка переменной окружения для запуска в режиме production
ENV DJANGO_ENV=production

# Установка переменной окружения для отключения вывода сообщений Python в буферизированном режиме
ENV PYTHONUNBUFFERED=1

# Install MySQL client
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev build-essential ldap-utils libldap2-dev libsasl2-dev\
    && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории внутри контейнера
WORKDIR /code

# Копирование зависимостей проекта
COPY requirements.txt /code/

# Установка зависимостей проекта
RUN pip3 install -r requirements.txt

# Копирование остальных файлов проекта
COPY . /code/

# Запуск команды для сборки статических файлов (если необходимо)
RUN python3 manage.py collectstatic --noinput

# Открытие порта, который будет использоваться для доступа к приложению
EXPOSE 8001

# Команда для запуска приложения в контейнере
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]