AI-Powered School Management System

A professional backend API built with FastAPI, PostgreSQL, and JWT Authentication — designed for managing students, teachers, classes, and subjects with role-based access control.

---

Features

- JWT Authentication (Access + Refresh Tokens)
- Role-Based Access Control (Admin, Teacher, Student)
- Full Students CRUD (Create, Read, Update, Delete)
- Classes & Subjects Management
- Users Management
- Professional Error Handling (consistent JSON responses)
- Pydantic V2 Schema Validation
- PostgreSQL Database with Alembic Migrations
- Dockerized Application
- Clean Architecture (routers/, utils/, services/)

---

Tech Stack

Technology         Purpose 

FastAPI            Web Framework 
PostgreSQL         Database 
SQLAlchemy 2.0       ORM 
Alembic            Database Migrations 
JWT (python-jose)  Authentication 
Passlib + bcrypt   Password Hashing 
Pydantic V2        Data Validation 
Docker             Containerization 
Uvicorn            ASGI Server 

---

Getting Started

### Prerequisites
- Python 3.9+
- PostgreSQL installed and running
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Muneebkhan502/school-managment-system.git
cd school-managment-system

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Install dependencies
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env
# Edit .env with your values

# 5. Run database migrations
alembic upgrade head

# 6. Start the server
fastapi dev main.py
```

### Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
DATABASE_URL=postgresql://username:password@localhost:5432/student_db
```

---

## 🐳 Run with Docker

```bash
# Build image
docker build -t sms-app .

# Run container
docker run -p 8000:8000 sms-app
```

---

##  API Endpoints

### Authentication
Method | Endpoint | Description

| POST | /auth/login | Login — get tokens |
| POST | /auth/refresh | Refresh access token |
| GET | /auth/me | Get current user |

### Students
| Method | Endpoint | Description |

| GET | /students/ | Get all students |
| POST | /students/ | Create student |
| GET | /students/{id} | Get student by ID |
| PATCH | /students/{id} | Update student |
| DELETE | /students/{id} | Delete student |

### Users
| Method | Endpoint | Description |

| GET | /users/ | Get all users |
| POST | /users/ | Create user |
| PATCH | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |

### Classes
| Method | Endpoint | Description |

| POST | /classes/ | Create class |
| GET | /classes/{id} | Get students by class |

---

## 📁 Project Structure

```
project_FastAPI/
├── routers/          # API route handlers
│   ├── auth.py
│   ├── student.py
│   ├── user.py
│   ├── classes.py
│   └── subjects.py
├── utils/            # Utility functions
│   └── jwt.py
├── statics/          # Static files
├── templates/        # HTML templates
├── main.py           # App entry point
├── models.py         # SQLAlchemy models
├── schemas.py        # Pydantic schemas
├── services.py       # Business logic
├── database.py       # DB connection
├── exceptions.py     # Custom exceptions
├── config.py         # Configuration
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## Author

Muneeb Afsar
- GitHub: [@Muneebkhan502](https://github.com/Muneebkhan502)
- Email: muneebafsar502@gmail.com

---

## License

This project is open source and available under the [MIT License](LICENSE).
