# from typing import AsyncGenerator

from fastapi import Depends
# from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import create_engine
# from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "mysql+mysqldb://root:password@localhost:3306/testdb"


class Base(DeclarativeBase):
    __allow_unmapped__ = True
    # pass

# sqlite
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine, expire_on_commit=True, autoflush=False, autocommit=False)
# engine = create_async_engine(DATABASE_URL)
# async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# def create_db_and_tables():
#     Base.metadata.create_all(bind=engine)

# async def create_db_and_tables():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session


# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)