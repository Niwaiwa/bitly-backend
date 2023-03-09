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
    is_verifiied: bool
    is_admin: bool
    created_time: datetime.datetime

    class Config:
        orm_mode = True

class UserUpdate():
    pass