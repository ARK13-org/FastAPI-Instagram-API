from typing import List

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from auth import oauth2
from db import db_comment
from db.database import get_db
from db.models import User
from schemas import CommentCreate, CommentDisplay, CommentUpdate

router = APIRouter(prefix="/comment", tags=["comment"])


@router.post("/create_comment", response_model=CommentDisplay)
def create_comment(
    request: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    return db_comment.create_comment(db, request, current_user.id)


@router.delete("/delete_comment", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    db_comment.delete_comment(id=id, db=db, user_id=current_user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch("/update_comment/{id}", response_model=CommentDisplay)
def update_comment(
    id: int,
    request: CommentUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    return db_comment.update_comment(db, id, request.text, current_user.id)


@router.get("/{id}", response_model=List[CommentDisplay])
def get_comments_by_post_id(id: int, db: Session = Depends(get_db)):
    return db_comment.get_comments_by_post_id(id=id, db=db)
