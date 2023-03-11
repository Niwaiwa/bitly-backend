import uuid
import datetime
from pydantic import BaseModel
from typing import Union


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    hashed_password: str

class UserRead(UserBase):
    id: int
    nickname: Union[str, None]
    api_key: Union[str, None]
    is_active: bool
    is_verified: bool
    is_admin: bool
    created_time: datetime.datetime

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    pass

class Login(UserBase):
    password: str

class RedirectURL(BaseModel):
    hash: str

class ShortURL(BaseModel):
    hash: str
    origin_url: str
    expired_time: datetime.datetime | None = datetime.datetime.now() + datetime.timedelta(days=7)
    user_id: int

class URLRead(BaseModel):
    id: int
    hash: str
    origin_url: str
    created_time: datetime.datetime
    expired_time: datetime.datetime

    class Config:
        orm_mode = True

class DeleteURL(RedirectURL):
    pass