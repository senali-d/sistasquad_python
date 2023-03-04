# Sistasquad game players collaboration app

## Dependencies versions used
- django=4.1.4
- djangorestframework=3.14.0
- psycopg2-binary
- django-cors-headers=3.13.0
- unicorn==20.1.0

## Project setup

- Install Python3

- Clone the Repo

- Create a `.env` file in the project root directory. And fill it in the following config format.

  ```
  export DB_NAME=<db_name>
  export DB_USER=<db_user>
  export DB_USER_PASSWORD=<db_password>
  export DB_HOST=<hostname>
  export DB_PORT=<port>
  ```

- Install Dependencies

  ```pip install -r requirements.txt```


- Run the following commands for migrations

  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

- Run the following command for create superuser

  ```
  DJANGO_SUPERUSER_PASSWORD=admin python manage.py createsuperuser --username admin --email admin@email.com --noinput
  ```

- Run the following command for runserver

  ```
  python manage.py runserver
  ```


> Note: Please make sure create database in postgres server before run the above command.
