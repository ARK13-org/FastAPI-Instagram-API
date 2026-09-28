import random

from fastapi import APIRouter, Depends, HTTPException , status , File, UploadFile
from sqlalchemy.orm import Session
import shutil
from db.database import get_db
from db import db_post
from string import ascii_letters
from schemas import PostBase, PostDisplay , UserAuth
from auth import oauth2
from typing import List

router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ["url", "uploaded"]

@router.post('/create_post' , response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db),
                 current_user: UserAuth = Depends(oauth2.get_current_user)):
    if request.image_url_type not in image_url_types:
        return HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
                             detail="Invalid image_url_type. Must be 'url' or 'uploaded'.")
    return db_post.create_post(db, request)

@router.post('/delete/{id}')
def delete_post(id: int, db: Session = Depends(get_db),
                current_user: UserAuth = Depends(oauth2.get_current_user)):
    return db_post.delete_post(id=id, db=db, user_id=current_user.id)

@router.get('/', response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)

@router.post('/upload_file')
def upload_file(file: UploadFile = File(...)):
    rand_string = ''.join(random.choices(ascii_letters , k=6))
    new_name = f"_{rand_string}.".join(file.filename.split('.'  , 1))
    path_file = f"uploaded_file/{new_name}"
    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_path": path_file}