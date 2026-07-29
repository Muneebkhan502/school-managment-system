from dotenv import load_dotenv
import os
from google import genai
# Reading the .env file
load_dotenv()

# Configuration variables if not givin in env yahar par by default ly raha hai
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM","HS256")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

