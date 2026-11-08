from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from schemas import UserBase, UserDisplay

router = APIRouter(prefix="/user", tags=["user"])

@router.post("", response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

@router.get("{username}", response_model=UserDisplay)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_username(db, username)

@router.get("/{id}", response_model=UserDisplay)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, id)

@router.delete('/delete/{id}', response_model=UserDisplay)
def delete_user(id: int, db: Session = Depends(get_db)):
    return db_user.delete_user(db, id)