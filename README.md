# bitly-backend

a practice project

##


## alembic

```
alembic init alembic

alembic -c alembic.ini --raiseerr revision --autogenerate -m "create users table"
PYTHONPATH=./ alembic.exe upgrade head
PYTHONPATH=./ alembic.exe upgrade +2
PYTHONPATH=./ alembic.exe downgrade base
PYTHONPATH=./ alembic.exe downgrade -1
```