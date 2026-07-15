from typing import Annotated
from fastapi import APIRouter,status,Depends
from schemas import StudentResponse, CreateStudent,UpdateStudent
from services import StudentManager
from utils.jwt import require_role, get_current_user
from sqlalchemy.orm import Session
from database import get_db
from models import User
router = APIRouter()

#@router ye path operation decorator
@router.get("/",response_model=list[StudentResponse], status_code=status.HTTP_200_OK)
def get_all_students(db: Annotated[Session, Depends(get_db)],
                     class_id: int | None = None, search: str | None = None ,
                      limit: int | None = None,
                      current_user: User = Depends(require_role(["admin","teacher"]))   ):
    manager = StudentManager(db)
    return manager.show_student(class_id, search, limit)
 
@router.get("/{id}",response_model=StudentResponse, status_code = status.HTTP_200_OK)
def get_student_by_id(id: int, 
                       db: Annotated[Session, Depends (get_db)],current_user: User = Depends(require_role(["admin","teacher","student"]))):
    manager = StudentManager(db)
    return manager.get_student(id)


@router.post("/",response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(student_data: CreateStudent, db: Annotated[Session, Depends(get_db)],current_user: User = Depends(require_role(["admin","teacher"]))):
    manager = StudentManager(db)
    return manager.add_student(student_data)

@router.patch("/{id}",response_model=StudentResponse, status_code=status.HTTP_200_OK)
def update_student(id:int, student:UpdateStudent, db: Annotated[Session, Depends(get_db)], current_user: User=Depends(require_role(["admin","teacher"]))):
    manager = StudentManager(db)
    return manager.update_student(id, student)

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_student(id:int, db: Annotated[Session, Depends(get_db)], current_user: User = Depends(require_role(["admin"]))):
    manager = StudentManager(db)
    return manager.delete_student(id)
