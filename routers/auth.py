from typing import Annotated
from fastapi import APIRouter,Depends
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from schemas import Token, UserResponse
from services import UserManager
from sqlalchemy.orm import Session
from database import get_db
from utils.jwt import get_current_user
from models import User

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# login routes
@router.post("/login",response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    manager = UserManager(db)
    return manager.user_login(form_data)

@router.post("/refresh", response_model=Token)
def refresh_token_endpoint(refresh_token: str, db:Annotated[Session, Depends(get_db)]):
    manager = UserManager(db)
    return manager.refresh_token(refresh_token)

@router.get("/me", response_model=UserResponse)
def get_me(current_user:User = Depends(get_current_user)):
    return current_user