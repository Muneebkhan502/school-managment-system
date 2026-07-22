from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(SQLALCHEMY_DATABASE_URL) # this line creates a SQLAlchemy engine that will manage the connection to database.
Base = declarative_base() # this line creates a base class for our database models. We will use this base class to define our Student model, which will represent the structure of the student table in the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    with SessionLocal() as db:
        yield db 