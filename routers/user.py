from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth import oauth2
from db import db_user
from db.database import get_db
from db.models import User
from schemas import UserBase, UserDisplay, UserPrivate, UserUpdate

router = APIRouter(prefix="/user", tags=["user"])


@router.post("", response_model=UserPrivate)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get("", response_model=List[UserDisplay])
def list_users(q: Optional[str] = None, limit: int = 50, db: Session = Depends(get_db)):
    """All users, optionally filtered by ?q=part-of-username."""
    return db_user.list_users(db, q, min(max(limit, 1), 200))


# Static routes BEFORE the dynamic /{id} route
@router.get("/me", response_model=UserPrivate)
def get_me(current_user: User = Depends(oauth2.get_current_user)):
    return current_user


@router.patch("/me", response_model=UserPrivate)
def update_me(
    request: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    return db_user.update_user(db, current_user, request)


@router.get("/by_username/{username}", response_model=UserDisplay)
def get_user_by_username(username: str, db: Session = Depends(get_db)):
    return db_user.get_user_by_username(db, username)


@router.get("/{id}", response_model=UserDisplay)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    return db_user.get_user_by_id(db, id)


@router.delete("/delete/{id}", response_model=UserDisplay)
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    if current_user.id != id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only delete your own account")
    return db_user.delete_user(db, id)
