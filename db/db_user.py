from typing import List, Optional

from fastapi import HTTPException, status
from sqlalchemy import func
from sqlalchemy.orm import Session

from db.hash import Hash
from db.models import User
from schemas import UserBase, UserUpdate

import datetime


def create_user(db: Session, request: UserBase):
    if db.query(User).filter(func.lower(User.username) == request.username.lower()).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="That username is already taken")
    if db.query(User).filter(func.lower(User.email) == request.email.lower()).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="That e-mail is already registered")

    user = User(
        username=request.username,
        email=request.email,
        password=Hash.bcrypt(request.password),
        created_at=datetime.datetime.now(),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def list_users(db: Session, q: Optional[str] = None, limit: int = 50) -> List[User]:
    query = db.query(User)
    if q and q.strip():
        query = query.filter(User.username.ilike(f"%{q.strip()}%"))
    return query.order_by(func.lower(User.username)).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with username '{username}' not found",
        )
    return user


def get_user_by_id(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{id}' not found",
        )
    return user


def update_user(db: Session, user: User, request: UserUpdate):
    if request.email is not None and request.email.lower() != (user.email or "").lower():
        taken = (
            db.query(User)
            .filter(func.lower(User.email) == request.email.lower(), User.id != user.id)
            .first()
        )
        if taken:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="That e-mail is already registered")
        user.email = request.email
    if request.bio is not None:
        user.bio = request.bio.strip()
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, id: int):
    user = get_user_by_id(db, id)
    db.delete(user)
    db.commit()
    return user
