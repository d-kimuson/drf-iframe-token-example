# DRF + SPA iframe based authentication

## Env

``` bash
$ python -V
Python 3.8.7

$ poetry -V
Poetry version 1.1.4

$ node -v
v15.10.0

$ yarn -v
1.22.10
```

## Try

``` bash
# django
$ poetry install && cd frontend && yarn install
$ poetry shell
(.venv)$ python manage.py makemigrations && python manage.py migrate
(.venv)$ python manage.py runserver

# next
$ yarn dev
```

Go to http://127.0.0.1:8000/accounts/signup to create account and login, then http://127.0.0.1:3000 is automatically authenticated.
