
import random
import shutil

from string import ascii_letters
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    File,
    UploadFile
)
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_post
from schemas import PostBase, PostCaptionUpdate, PostDisplay
from auth import oauth2


router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ["url", "uploaded"]


@router.post('/create_post', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid image_url_type. Must be 'url' or 'uploaded'."
        )

    return db_post.create_post(db, request)


@router.delete('/delete_post/{id}')
def delete_post(id: int, db: Session = Depends(get_db)):
    post = db.query(db_post.Post).filter(db_post.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id '{id}' not found"
        )

    db.delete(post)
    db.commit()

    return {"detail": "Post deleted successfully"}


@router.get('/', response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


# Static route BEFORE dynamic route
@router.get('/user_posts', response_model=List[PostDisplay])
def get_posts_by_user_id(user_id: int, db: Session = Depends(get_db)):
    posts = db.query(db_post.Post).filter(
        db_post.Post.user_id == user_id
    ).all()

    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No posts found for user with id '{user_id}'"
        )

    return posts


@router.get('/{id}', response_model=PostDisplay)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    post = db.query(db_post.Post).filter(db_post.Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id '{id}' not found"
        )

    return post


@router.post('/upload_file')
def upload_file(file: UploadFile = File(...)):
    rand_string = ''.join(random.choices(ascii_letters, k=6))
    new_name = f"_{rand_string}.".join(file.filename.split('.', 1))

    path_file = f"uploaded_file/{new_name}"

    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_path": path_file}

@router.patch('/update_caption/{id}', response_model=PostDisplay)
def update_post_caption(
    id: int,
    request: PostCaptionUpdate,
    db: Session = Depends(get_db)
):
    post = db.query(db_post.Post).filter(
        db_post.Post.id == id
    ).first()

    if post is None:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
        )

    post.caption = request.caption

    db.commit()
    db.refresh(post)

    print("UPDATED POST:", post)
    print("UPDATED CAPTION:", post.caption)

    return post