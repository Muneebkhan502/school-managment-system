from typing import Annotated
from fastapi import APIRouter,status,Depends
from schemas import StudentResponse, CreateStudent,UpdateStudent
from services import StudentManager
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter()

@router.get("/")
def show_subject():
    pass