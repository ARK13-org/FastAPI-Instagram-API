from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime , timedelta
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm import Session
from db.database import get_db
from fastapi.exceptions import HTTPException
from fastapi import Depends , status
from db.db_user import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = '...'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict , expires_delta:Optional[timedelta] = None) :
    to_encode = data.copy()
    if expires_delta :
        expire = datetime.utcnow() + expires_delta
    else :
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp' : expire})
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token:str = Depends(oauth2_scheme) , db:Session = Depends(get_db)) :
    error_credentials = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,
                                       detail='could not validate credintials' ,
                                       headers={'WWW-authenticate' : 'bearer'})

    try :
        _dict = jwt.decode(token , SECRET_KEY , algorithms=ALGORITHM)
        username:str = _dict.get('sub')
        if not username :
            raise error_credentials
    except JWTError :
        raise error_credentials

    user = get_user_by_username(username , db)

    return user
