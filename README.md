```
pipenv shell
```

```
# flask env
FLASK_APP=run
FLASK_ENV=development

# app env
DATABASE_URL=mysql+pymysql://root:1234@localhost:3306/app

# docker-compose env
MYSQL_ROOT_PASSWORD=1234
MYSQL_DATABASE=app
```

```
docker-compose up
flask run
```

```
flask db init
flask db migrate
flask db upgrade
```