import random

from fastapi import APIRouter, Depends, HTTPException , status , File, UploadFile
from sqlalchemy.orm import Session
import shutil
from db.database import get_db
from db import db_comment
from schemas import CommentBase, CommentDisplay , UserAuth
from auth import oauth2
from typing import List

router = APIRouter(prefix="/comment", tags=["comment"])

@router.post('/create_comment' , response_model=CommentDisplay)
def create_post(request: CommentBase, db: Session = Depends(get_db),
                 current_user: UserAuth = Depends(oauth2.get_current_user)):
    return db_comment.create_comment(db, request)

@router.post('/delete/{id}')
def delete_comment(id: int, db: Session = Depends(get_db),
                current_user: UserAuth = Depends(oauth2.get_current_user)):
    return db_comment.delete_comment(id=id, db=db, user_id=current_user.id)

@router.get('/{id}', response_model=List[CommentDisplay])
def get_all_posts(id:int ,db: Session = Depends(get_db)):
    return db_comment.get_comments_by_post_id(id=id , db=db)