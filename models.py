from sqlalchemy import Integer, String,Float, ForeignKey
from sqlalchemy import Enum as SQLEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
import enum
from database import Base

class Student_DB(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    rollno: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email:Mapped[str] = mapped_column(String(50), unique=True, nullable=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("Classes.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    marks: Mapped[float] = mapped_column(Float, default=0)
    date_of_birth: Mapped[str] = mapped_column(String(20), nullable=True, default=None)
    image_file: Mapped[str | None] = mapped_column(String(255), nullable=True, default=None)
    contact_number: Mapped[str | None ] = mapped_column(String(11), nullable=True, default=None)
    school_class: Mapped["SchoolClass"] = relationship(back_populates="students")
    user: Mapped[User] = relationship(back_populates= "students")
    @property
    def image_url(self):
        if self.image_file:
            return f"/images/{self.image_file}"
        return "/static/profile_pics/default.jpg"
    @property 
    def full_name(self): 
        return "{} {}".format(self.first_name,self.last_name)
    def __str__(self):
        return f"Name: {self.full_name} | Class: {self.class_id}"

class SchoolClass(Base):
    __tablename__ = "Classes"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    class_name: Mapped[str] = mapped_column(String(100), nullable=False)
    section: Mapped[str] = mapped_column(String(50), nullable=False)
    students: Mapped[list["Student_DB"]] = relationship(back_populates="school_class")

class UserRole(enum.Enum):
    admin = "admin"
    teacher = "teacher"
    student = "student"
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] =  mapped_column(String(100), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable= False) 
    hashed_password: Mapped[str] = mapped_column(String(250), nullable=False)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole ,native_enum = False,
                                                    name="userrole_type"), default=UserRole.student,
                                                      nullable=False)
    students: Mapped["Student_DB"] = relationship(back_populates="user")