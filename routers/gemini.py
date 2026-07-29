from schemas import PromtRequest , PromtResponse
from fastapi import APIRouter,status,Depends
from services import AiManager
from sqlalchemy.orm import Session
from models import User
from utils.jwt import get_current_user
router = APIRouter()
from database import get_db
from typing import Annotated

@router.post("/", response_model=PromtResponse, status_code=status.HTTP_200_OK)
def ask_ai(prompt: PromtRequest,
           current_user:User = Depends(get_current_user),
           db: Session = Depends(get_db)):
    manager = AiManager(db)
    return manager.ask_ai(prompt, current_user)