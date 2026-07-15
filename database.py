from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:admin1234@localhost:5433/student_db" # this is the URL for the PostgreSQL database, it specifies that we want to use PostgreSQL and the database name is student_db.

engine = create_engine(SQLALCHEMY_DATABASE_URL) # this line creates a SQLAlchemy engine that will manage the connection to database.
Base = declarative_base() # this line creates a base class for our database models. We will use this base class to define our Student model, which will represent the structure of the student table in the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    with SessionLocal() as db:
        yield db 