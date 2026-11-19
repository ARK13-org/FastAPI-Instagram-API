import datetime
from typing import List

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models import Post
from schemas import PostBase


def create_post(db: Session, request: PostBase, user_id: int):
    new_post = Post(
        image_url=request.image_url.strip(),
        image_url_type=request.image_url_type,
        caption=request.caption.strip(),
        timestamp=datetime.datetime.now(),
        user_id=user_id,
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all_posts(db: Session) -> List[Post]:
    return db.query(Post).order_by(Post.timestamp.desc(), Post.id.desc()).all()


def get_posts_by_user(db: Session, user_id: int) -> List[Post]:
    return (
        db.query(Post)
        .filter(Post.user_id == user_id)
        .order_by(Post.timestamp.desc(), Post.id.desc())
        .all()
    )


def get_post(db: Session, id: int) -> Post:
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{id}' not found")
    return post


def get_owned_post(db: Session, id: int, user_id: int) -> Post:
    post = get_post(db, id)
    if post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="This is not your post")
    return post


def delete_post(id: int, db: Session, user_id: int):
    post = get_owned_post(db, id, user_id)
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted successfully"}
