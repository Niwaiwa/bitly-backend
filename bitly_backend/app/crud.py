import datetime
from sqlalchemy.orm import Session
from sqlalchemy import delete

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.hashed_password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_url_by_hash(db: Session, hash: str):
    return db.query(models.URL).filter(models.URL.hash == hash).first()


def get_urls_by_user(db: Session, user_id: int, limit: int = 10, page: int = 1):
    return db.query(models.URL).filter(models.URL.user_id == user_id).limit(limit).offset((page-1)*limit).all()


def short_url(db: Session, url: schemas.ShortURL, user_id: int):
    db_url = models.URL(hash=url.hash, origin_url=url.origin_url, expired_time=url.expired_time, user_id=user_id)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url


def delete_url(db: Session, url: models.URL):
    db.delete(url)
    db.commit()
    return
