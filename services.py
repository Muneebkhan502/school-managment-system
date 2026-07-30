from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from models import Student_DB, SchoolClass, User, ChatHistory
from schemas import CreateStudent, Token,UpdateStudent, CreateClass, ClassResponse, CreateUser,UserResponse,UpdateUser,Login, PromtRequest,PromtResponse
from fastapi import HTTPException, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from exceptions import NotFoundException, ForbiddenException, UnauthorizedException
from utils.jwt import create_access_token, create_refresh_token, require_role, verify_token, get_current_user
import os
from dotenv import load_dotenv
from config import GEMINI_API_KEY
from google import genai
from google.genai import types
class StudentManager(): 

    def __init__(self, db: Session):
        self.db = db

    def add_student(self,  student_data: CreateStudent):
        student_obj = Student_DB(**student_data.model_dump())
        try:
            self.db.add(student_obj)
            self.db.commit()
            self.db.refresh(student_obj)
            return student_obj
        except IntegrityError:
            self.db.rollback()
            raise ForbiddenException("Student with this roll number or email already exists")

    def update_student(self, id:int, student: UpdateStudent):
        result = self.db.execute(select(Student_DB).where(Student_DB.id == id))
        existing = result.scalars().first()
        if not existing:
            raise NotFoundException("Student with this id not found to update")
        update_data = student.model_dump(exclude_unset=True,exclude_none=True)
        for field, value in update_data.items():
            setattr(existing,field,value)  #Setattr --> dyanamically set using loop
        self.db.add(existing)
        self.db.commit()
        self.db.refresh(existing)
        return existing
        
        

    def show_student(self, class_id: int | None = None, search: str | None = None, limit: int = 10):                                                                  
        query = select(Student_DB)
        #class filter
        if class_id:
            query = query.where(Student_DB.class_id == class_id)
        #search filter
        if search:
            query = query.where(Student_DB.first_name.like(f"%{search}%"))
        if limit:
            query = query.limit(limit)
        result = self.db.execute(query)                                  # self.db          →  hamara session (notepad)
        std = result.scalars().all()                                                    # .execute()       →  database ko query bhejo — "yeh kaam karo"
                                                                                         # select(Student_DB) →  SQL mein: SELECT * FROM students
                                                                                        # result           →  raw database response — abhi usable nahi
        return std                                                                      # .scalars()        →  raw response se actual student objects nikaalo
                                                                                        # .all()            →  saare student objects ko ek list mein daalo
                                                                                           
    def get_student(self, id: int):
        result = self.db.execute(select(Student_DB).where(Student_DB.id == id))
        student = result.scalars().first()
        if not student:
            raise NotFoundException("Student not found")
        return student
    
    def delete_student(self,id:int):

        result = self.db.execute(select(Student_DB).where(Student_DB.id == id))
        existing = result.scalars().first()
        if not existing:
            raise NotFoundException("Student with this id not found to delete")
        self.db.delete(existing)
        self.db.commit()

class ClassManager():
    def __init__(self, db:Session):
        self.db = db

    def add_class(self,class_student:CreateClass):
        try:
            std_obj = SchoolClass(**class_student.model_dump())
            self.db.add(std_obj)
            self.db.commit()
            self.db.refresh(std_obj)
        except IntegrityError:
            self.db.rollback()
            raise ForbiddenException("Class with this name already exists")
        return std_obj
    
    def show_class(self,id:int):
        result = self.db.execute(select(Student_DB).where(Student_DB.class_id == id))
        exiting = result.scalars().all()
        if not exiting:
            raise NotFoundException("No students found in this class")
        return exiting

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
class UserManager():
    def __init__(self,db:Session):
        self.db = db

    def add_user(self,user:CreateUser):
        hashed_pwd = pwd_context.hash(user.password)
        data = user.model_dump(exclude={"password"})
        user_obj = User(**data, hashed_password=hashed_pwd)
        try:
            self.db.add(user_obj)
            self.db.commit()
            self.db.refresh(user_obj)
            return user_obj
        except IntegrityError:
            self.db.rollback()
            raise ForbiddenException("User with this username or email already exists")
        
    def update_user(self, id:int, user:UpdateUser):
        result = self.db.execute(select(User).where(User.id == id))
        existing = result.scalars().first()
        if not existing:
            raise NotFoundException("User with this id not found")
        update_data = user.model_dump(exclude_unset= True, exclude_none=True)
        if "password" in update_data:
            hashed_pwd = pwd_context.hash(update_data["password"])
            update_data["hashed_password"] = hashed_pwd
            del update_data["password"]
        
        for key, value in update_data.items():
            setattr(existing,key,value)
        self.db.add(existing)
        self.db.commit()
        self.db.refresh(existing)
        return existing

    def show_all_users(self):
        result = self.db.execute(select(User))
        existing = result.scalars().all()
        if not existing:
            raise NotFoundException("User not found")
        return existing
     
    def get_user(self,id:int):
        result = self.db.execute(select(User).where(User.id == id))
        existing = result.scalars().first()
        if not existing:
            raise NotFoundException("Current User not found")
        return existing

    def delete_user(self,id:int):
        result = self.db.execute(select(User).where(User.id == id))
        existing = result.scalars().first()
        if not existing:
            raise NotFoundException("User not found")
        self.db.delete(existing)
        self.db.commit()
        return existing
    
    def user_login(self,form_data:OAuth2PasswordRequestForm):
        result = self.db.execute(select(User).where(User.username == form_data.username))
        user = result.scalars().first()
        if not user or not pwd_context.verify(form_data.password, user.hashed_password):
            raise UnauthorizedException("Incorrect username or password")
        access_token = create_access_token(user.id, user.role.value)
        refresh_token = create_refresh_token(user.id, user.role.value)
        return Token(access_token = access_token, refresh_token=refresh_token)
    
    def refresh_token(self, refresh_token: str):
        token_data = verify_token(refresh_token, expected_type="refresh")
        result = self.db.execute(select(User).where(User.id == token_data.user_id))
        user = result.scalars().first()
        if not user:
            raise NotFoundException("user not found")
        new_access = create_access_token(user.id, user.role.value)
        new_refresh = create_refresh_token(user.id, user.role.value)

        return Token(access_token=new_access, refresh_token=new_refresh)

class AiManager():
    def __init__(self,db:Session):
        self.db = db
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def ask_ai(self,prompt: PromtRequest, current_user):
        # fetch first 10 chats from history
        history = self.db.execute(select(ChatHistory).where(ChatHistory.user_id == current_user.id).order_by(ChatHistory.created_at.desc()).limit(10)).scalars().all()
        #Add chat history in a contents with expacted formate of google
        contents = []
        for chat in reversed(history):
            contents.append(types.Content(role = "user",
                                          parts = [types.Part(text = chat.prompt)]))
            contents.append(types.Content(role = "model",
                                          parts = [types.Part(text = chat.response)]))
        # add new prompt
        contents.append(types.Content(role = "user",
                                      parts = [types.Part(text = prompt.prompt)]))
        # print(contents)
        # print(type(contents))
        try:
            response = self.client.models.generate_content(model = "gemini-3.5-flash", contents = contents)
            # print(response.text)
            
            chat = ChatHistory(
                user_id = current_user.id,
                prompt = prompt.prompt,
                response = response.text
            )
            self.db.add(chat)
            self.db.commit()  
            self.db.refresh(chat) 
            return PromtResponse(
                prompt = prompt.prompt,
                response=response.text
                    )
        except Exception as e:
            print(e)
            print(type(e))
            #it is good practice to keep e out of httpexception bcz of security concern 
            #imagin if u keep inside it then let say error is about api key then client will leak apikey to user
            raise HTTPException(
                status_code = 500,
                detail = "Failed to generate Ai response"
            )

    def show_chat_history(self,current_user):
        history = self.db.execute(select(ChatHistory).where(ChatHistory.user_id == current_user.id).order_by(ChatHistory.created_at.desc()))
        existing = history.scalars().all()
       
        if not existing:
            raise NotFoundException("User or Chat not found")
        return existing

    def get_chat(self, search: str, current_user):
        query = select(ChatHistory).where(ChatHistory.user_id == current_user.id)
            #search filter
        if search:
            query = query.where(ChatHistory.prompt.ilike(f"%{search}%"))
            result = self.db.execute(query)
            chat = result.scalars().all()
            return chat
        raise NotFoundException("User Or Chat Not Found")