from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field, field_validator

EMAIL_PATTERN = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


# ---------------------------------------------------------------- users
class UserBase(BaseModel):
    username: str = Field(min_length=3, max_length=30, pattern=r"^[A-Za-z0-9_.]+$")
    email: str = Field(pattern=EMAIL_PATTERN, max_length=120)
    password: str = Field(min_length=6, max_length=128)


class UserUpdate(BaseModel):
    bio: Optional[str] = Field(default=None, max_length=150)
    email: Optional[str] = Field(default=None, pattern=EMAIL_PATTERN, max_length=120)


class UserMini(BaseModel):
    """Small user object embedded in posts and comments."""
    id: int
    username: str

    class Config:
        from_attributes = True


User = UserMini  # backwards-compatible name


class UserDisplay(BaseModel):
    """Public profile. Never exposes the e-mail address."""
    id: int
    username: str
    bio: Optional[str] = None
    created_at: Optional[datetime] = None
    posts_count: int = 0
    comments_count: int = 0

    class Config:
        from_attributes = True


class UserPrivate(UserDisplay):
    """What the owner sees about themselves (/user/me, registration)."""
    email: str


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


# ------------------------------------------------------------- comments
class CommentCreate(BaseModel):
    text: str = Field(min_length=1, max_length=500)
    post_id: int

    @field_validator("text")
    @classmethod
    def _strip(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Comment cannot be empty")
        return v


class CommentUpdate(BaseModel):
    text: str = Field(min_length=1, max_length=500)

    @field_validator("text")
    @classmethod
    def _strip(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Comment cannot be empty")
        return v


class CommentDisplay(BaseModel):
    id: int
    text: str
    timestamp: datetime
    user: UserMini
    post_id: int

    class Config:
        from_attributes = True


# ---------------------------------------------------------------- posts
class PostBase(BaseModel):
    image_url: str = Field(min_length=1)
    image_url_type: str
    caption: str = ""
    creator_id: Optional[int] = None  # ignored: the logged-in user is the creator


class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: Optional[str] = ""
    timestamp: datetime
    user: UserMini
    comments: List[CommentDisplay] = []

    class Config:
        from_attributes = True


class PostCaptionUpdate(BaseModel):
    caption: str = Field(max_length=2200)
