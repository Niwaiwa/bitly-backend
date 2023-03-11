
from sqlalchemy import Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import mapped_column
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = mapped_column(Integer, primary_key=True, index=True)
    email = mapped_column(String(320), nullable=False, unique=True, index=True)
    hashed_password = mapped_column('password', String(64), nullable=False)
    nickname = mapped_column(String(30))
    api_key = mapped_column(String(64))
    is_active = mapped_column(Boolean, nullable=False, default=True)
    is_verifiied = mapped_column(Boolean, nullable=False, default=False)
    is_admin = mapped_column(Boolean, nullable=False, default=False)
    created_time = mapped_column(DateTime, nullable=False, default=func.current_timestamp())
