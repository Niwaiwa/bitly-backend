from fastapi import Depends, FastAPI, HTTPException, Request, Response, Form
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserRead)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.UserRead])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.UserRead)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/login", response_model=schemas.UserRead)
def login(email: str = Form(), password: str = Form(), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if db_user.hashed_password != password:
        raise HTTPException(status_code=400, detail="Login failed")
    return db_user


@app.get("/{hash}")
def redirect_url(hash: str, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_hash(db, hash=hash)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.origin_url)


@app.post("/short_url", response_model=schemas.URLRead)
def short_url(url: schemas.ShortURL, db: Session = Depends(get_db)):
    # user_id = get_current_user
    db_url = crud.get_url_by_hash(db, hash=url.hash)
    if db_url:
        raise HTTPException(status_code=404, detail="URL already used")
    db_url = crud.short_url(db, url=url, user_id=url.user_id)
    return db_url


@app.delete("/delete_url", response_model=None)
def delete_url(url: schemas.DeleteURL, db: Session = Depends(get_db)):
    db_url = crud.get_url_by_hash(db, hash=url.hash)
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    crud.delete_url(db, db_url)
    return {"message": "success."}
