import os
import random
import shutil
from string import ascii_letters
from typing import List

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from auth import oauth2
from db import db_post
from db.database import get_db
from db.models import User
from schemas import PostBase, PostCaptionUpdate, PostDisplay

router = APIRouter(prefix="/post", tags=["post"])

image_url_types = ["url", "uploaded"]
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
UPLOAD_DIR = "uploaded_file"


@router.post("/create_post", response_model=PostDisplay)
def create_post(
    request: PostBase,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    if request.image_url_type not in image_url_types:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Invalid image_url_type. Must be 'url' or 'uploaded'.",
        )
    return db_post.create_post(db, request, current_user.id)


@router.delete("/delete_post/{id}")
def delete_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    return db_post.delete_post(id, db, current_user.id)


@router.get("/", response_model=List[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


# Static routes BEFORE the dynamic /{id} route
@router.get("/user_posts", response_model=List[PostDisplay])
def get_posts_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return db_post.get_posts_by_user(db, user_id)  # empty list when the user has no posts


@router.post("/upload_file")
def upload_file(
    file: UploadFile = File(...),
    current_user: User = Depends(oauth2.get_current_user),
):
    name, ext = os.path.splitext(os.path.basename(file.filename or "image"))
    ext = ext.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Only image files are allowed")

    os.makedirs(UPLOAD_DIR, exist_ok=True)
    rand_string = "".join(random.choices(ascii_letters, k=6))
    new_name = f"{name}_{rand_string}{ext}"
    path_file = f"{UPLOAD_DIR}/{new_name}"

    with open(path_file, "w+b") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"file_path": path_file, "url": f"/files/{new_name}"}


@router.get("/{id}", response_model=PostDisplay)
def get_post_by_id(id: int, db: Session = Depends(get_db)):
    return db_post.get_post(db, id)


@router.patch("/update_caption/{id}", response_model=PostDisplay)
def update_post_caption(
    id: int,
    request: PostCaptionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(oauth2.get_current_user),
):
    post = db_post.get_owned_post(db, id, current_user.id)
    post.caption = request.caption.strip()
    db.commit()
    db.refresh(post)
    return post
