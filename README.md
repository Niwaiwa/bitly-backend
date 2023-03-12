# bitly-backend

a practice project for bitly short url

## start

```
cd bitly_backend
python main.py
```

## features

fastapi
sqlachemy
alembic
mariadb


## alembic

```
alembic init alembic

alembic -c alembic.ini --raiseerr revision -m "create users table"
PYTHONPATH=./ alembic.exe upgrade head
PYTHONPATH=./ alembic.exe upgrade +2
PYTHONPATH=./ alembic.exe downgrade base
PYTHONPATH=./ alembic.exe downgrade -1
```

## mariadb

```
docker-compose -f docker-mariadb.yml up -d
docker-compose -f docker-mariadb.yml down
```