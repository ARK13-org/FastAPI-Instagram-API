import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from db.models import Comment, Post
from schemas import CommentCreate


def create_comment(db: Session, request: CommentCreate, user_id: int):
    if not db.query(Post).filter(Post.id == request.post_id).first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id '{request.post_id}' not found")
    new_comment = Comment(
        text=request.text,
        user_id=user_id,
        post_id=request.post_id,
        timestamp=datetime.datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_comments_by_post_id(db: Session, id: int):
    return db.query(Comment).filter(Comment.post_id == id).order_by(Comment.timestamp, Comment.id).all()


def _get(db: Session, id: int) -> Comment:
    comment = db.query(Comment).filter(Comment.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Comment with id '{id}' not found")
    return comment


def update_comment(db: Session, id: int, text: str, user_id: int):
    comment = _get(db, id)
    if comment.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You can only edit your own comments")
    comment.text = text
    db.commit()
    db.refresh(comment)
    return comment


def delete_comment(id: int, db: Session, user_id: int):
    """The comment's author OR the owner of the post can delete a comment."""
    comment = _get(db, id)
    if comment.user_id == user_id or comment.post.user_id == user_id:
        db.delete(comment)
        db.commit()
        return
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to delete this comment")
