from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy import func
from sqlalchemy.orm.session import Session

from auth import oauth2
from db import models
from db.database import get_db
from db.hash import Hash

router = APIRouter(tags=["authentication"])


@router.post("/token")
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = (
        db.query(models.User)
        .filter(func.lower(models.User.username) == request.username.strip().lower())
        .first()
    )
    if not user or not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")

    access_token = oauth2.create_access_token(data={"sub": user.username})

    return {
        "access_token": access_token,
        "type_token": "bearer",
        "token_type": "bearer",
        "userID": user.id,
        "username": user.username,
    }
