from fastapi import HTTPException , status
from db.models import Comment
from schemas import CommentBase
from sqlalchemy.orm import Session
import datetime

def create_comment(db: Session, request: CommentBase):
    new_comment = Comment(
        text=request.text,
        user_id=request.user_id,
        post_id=request.post_id,
        timestamp=datetime.datetime.now(),
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_comments_by_post_id(db: Session , id :int):
    return db.query(Comment).filter(Comment.post_id == id).all()

def delete_comment(id: int, db: Session, user_id: int):
    comment = db.query(Comment).filter(Comment.id == id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Comment with id '{id}' not found")
    if comment.user_id == user_id or comment.post.id == user_id:   
        db.delete(comment)
        db.commit()
        return {"OK"}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You are not authorized to delete this Comment")