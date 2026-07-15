from pydantic import BaseModel ,Field, EmailStr, ConfigDict
class CreateStudent(BaseModel):
    first_name: str = Field(..., description="First name of the person", min_length=3, max_length=50)
    last_name: str = Field(..., description="Last name of the person", min_length=2, max_length=50)
    class_id: int   = Field(..., description="Department of the person", gt=0) 
    email: EmailStr | None = None
    rollno: int = Field(..., description="Roll number of the student", gt=0)
    marks: float = Field(..., description="Marks of the student", ge=0, le=100)
    contact_number: str | None = None
    ## ye line isliye likhi hai taki hum apne Person class ke attributes ko directly use kar sakein, bina kisi extra code ke, jab hum PersonModel ka instance banayenge

class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    email: EmailStr | None = None
    school_class: ClassResponse | None = None
    rollno: int
    marks: float
    contact_number: str | None = None
    image_url: str | None = None
class UpdateStudent(BaseModel):
    first_name: str | None = None
    class_id: int | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    rollno: int | None = None
    marks: float | None = None
    contact_number: str | None = None

class CreateClass(BaseModel):
    class_name: str = Field(..., description="Name of the class", min_length=2, max_length=100)
    section: str = Field(..., description="Section of the class", min_length=1, max_length=50)

class ClassResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    class_name: str | None = None
    section: str | None = None

class CreateUser(BaseModel):
    username:str = Field(..., description="Username for the user", min_length=3, max_length=100)
    email: EmailStr = Field(..., description="Email address of the user",min_length=5, max_length=255)
    role: str = Field(..., description = "Are you student,teacher, or admin", min_length=4, max_length=20)
    password: str = Field(..., description="Password for the user", min_length=6)
    
class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    role: str

class UpdateUser(BaseModel):
    username: str | None = None
    email: EmailStr | None = None
    role: str | None = None
    password: str | None = None

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer" # ye line isliye likhi hai taki jab hum Token model ka instance banayenge, to by default token_type ki value "bearer" ho jaye, jab tak hum explicitly usse kuch aur na de.

class TokenData(BaseModel):
    user_id: int 
    role: str 