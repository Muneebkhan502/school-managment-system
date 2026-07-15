from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from database import get_db
from models import User
from schemas import Token, TokenData, UserResponse
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, REFRESH_TOKEN_EXPIRE_DAYS
from passlib.context import CryptContext
from sqlalchemy import select
from typing import Annotated
router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# MUNEEB_LEARN: OAuth2PasswordBearer ye batata hai ke token kahan se aayega
# tokenUrl = ye woh endpoint hai jo token DETA hai (login)
# Django mein ye automatically handle hota tha TokenAuthentication se
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Create Token
def create_access_token(user_id: int, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub": str(user_id),   # MUNEEB_LEARN: "sub" = subject, JWT standard claim
        "role": role,           # custom claim — jo hum chahein daal sakte hain
        "exp": expire,          # MUNEEB_LEARN: "exp" = expiry — jose library automatically check karta hai ye
        "type": "access"        # ye hum ne add kiya taake refresh token se distinguish kar sakein
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def create_refresh_token(user_id: int, role: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    payload = {
        "sub": str(user_id),
        "role": role,
        "exp": expire,
        "type": "refresh"  
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# token verifiction after user logged in, har protected route pe ye function call hoga
def verify_token(token: str, expected_type: str = "access") -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or expired token",
        headers={"WWW-Authenticate": "Bearer"},  # OAuth2 standard header
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
        user_id = payload.get("sub")
        role = payload.get("role")
        token_type = payload.get("type")

        if not user_id or not role:
            raise credentials_exception
        
       
        # Refresh token ko access token ki jagah use hone se rokta hai
        if token_type != expected_type:
            raise HTTPException(status_code=403, detail=f"Expected {expected_type} token")
            
        return TokenData(user_id=int(user_id), role=role)
    
    except JWTError:
        raise credentials_exception
    
def get_current_user(
        token:str = Depends(oauth2_scheme),
        db: Session = Depends(get_db)) -> User:
    token_data = verify_token(token,expected_type="access")
    result = db.execute(select(User).where(User.id == token_data.user_id))
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code = 404, detail = "User not found")
    return user

def require_role(allowed_roles:list[str]):
    def role_checker(current_user: User = Depends(get_current_user)):
        if current_user.role.value not in allowed_roles:
            raise HTTPException(status_code=403)
        return current_user
    return role_checker
 

