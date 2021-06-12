Django. JWT Аутентификация

Требования перечислены в requirements.txt
+ PostgreSQL

установка всех пакетов из списка:
pip install -r requirements.txt

Для работы проекта необходимо создать файл .env в папке django_auth
Файл .env должен содержать следующую информацию:
---------------------------
DEBUG=True
SECRET_KEY='ваш секретный ключ'
POSTGRES_DB='название БД'
POSTGRES_USER='имя пользователя БД'
POSTGRES_PASSWORD='пароль пользователя БД'
---------------------------

Необходимо создать таблицы в базе данных путем миграции из моделей проекта:
---------------------------
python manage.py makemigrations
python manage.py migrate
---------------------------

создание суперпользователя:
python3 manage.py createsuperuser


---------------------------
  Запросы
---------------------------

Создание нового пользователя:
POST на http://<...>/user/create/
содержание запроса:
{
    "email": "www@www.com",
    "first_name": "john",
    "last_name": "doe",
    "password": "123qwe"
}
ответ:
{
    "id": <...>,
    "email": "www@www.com",
    "first_name": "john",
    "last_name": "doe",
    "date_joined": "<...>"
}

Получение токена пользователя:
POST на http://<...>/user/obtain_token/
содержание запроса:
{
    "email": "www@www.com",
    "password": "123qwe"
}
ответ:
{
    "name": "john1y doe",
    "token": "<новый токен>"
}

