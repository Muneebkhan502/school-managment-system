from typing import Annotated
from fastapi import APIRouter,status,Depends
from schemas import CreateClass, ClassResponse, StudentResponse
from services import StudentManager, ClassManager
from sqlalchemy.orm import Session
from database import get_db
router = APIRouter()

@router.post("/", response_model=ClassResponse, status_code=status.HTTP_201_CREATED)
def create_class(student_class: CreateClass, db: Annotated[Session, Depends(get_db)]):
    manager = ClassManager (db)
    return manager.add_class(student_class)

@router.get("/{id}", response_model=list[StudentResponse], status_code=status.HTTP_200_OK)
def get_students_by_class(id:int,db: Annotated[Session, Depends(get_db)]):
    manager = ClassManager(db)
    return manager.show_class(id)