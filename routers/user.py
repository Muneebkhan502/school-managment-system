from typing import Annotated
from fastapi import APIRouter,status,Depends
from schemas import CreateClass, ClassResponse, StudentResponse, CreateUser,UserResponse,UpdateUser,Login
from services import UserManager
from sqlalchemy.orm import Session
from database import get_db
from utils.jwt import require_role
from models import User
router = APIRouter()

@router.post("/",response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    manager = UserManager(db)
    return manager.add_user(user_data)

@router.patch("/{id}", response_model=UserResponse ,status_code=status.HTTP_200_OK)
def update_user(id: int, user_data: UpdateUser, db: Annotated[Session, Depends(get_db)], current_user: User = Depends(require_role(["admin"]))):
    manager = UserManager(db)
    return manager.update_user(id, user_data)


@router.get("/",response_model=list[UserResponse],status_code=status.HTTP_200_OK)
def show_all_user(db: Annotated[Session, Depends(get_db)], current_user: User = Depends(require_role(["admin"]))):
    manager = UserManager(db)
    return manager.show_all_users()

@router.get("/{id}",response_model=UserResponse,status_code=status.HTTP_200_OK)
def show_user_by_id(id:int, db: Annotated[Session, Depends(get_db)], current_user: User = Depends(require_role(["admin","teacher","student"]))):
    manager = UserManager(db)
    return manager.get_user(id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id:int, db:Annotated[Session, Depends(get_db)], _ = Depends(require_role(["admin"]))):
    manager = UserManager(db)
    return manager.delete_user(id)

