# TODOs Auth API

In this project you're in charge of integrating an API to your service, and deploying it to Heroku.

Most of the project's functionality is already done: both models and frontend are built. We've also included an admin user and a few model instances to have data to get started

##### Setup Instruction

```bash
$ mkvirtualenv todos-api -p /usr/bin/python3
$ pip install -r dev-requirements.txt
$ make migrate
```

You can now run the development server:

```bash
$ make runserver
```

And point your browser to the correct URL and should see already the todos working. There's a superuser created with username `admin` and password `admin`.

##### How to regenerate the DB?

The Database is already provided, but if you need to regenerate it, just run:

```bash
$ rm -f django_todos/django_todos/db.sqlite3  # WARNING: deleting previous DB.
$ make migrate
$ make load_data
```
