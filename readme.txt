Today Learning
alembic migration ..jis trah hjum django ma python manage.py makemigration and make migrate use krty bilkul esi trah
hum fastapi ma alembic revision --autogenerate -m "..." use krty hai to compare models kih database ma kiya hai and models
ma kon sy field hai
phir hum alembic upgrade head kih jo models ye database k lye latest version defined krta hai jo models ma hai
lakin is sy pihly alembic install krna hoga through pip and phir directory banani hogi (alembic init alembic) is k throgh sab
required directory ban jty hai phir /env ma ini.py file hota hai jaha par hum jaha par hum apna database url set krty hai 
phir alembic/env.py ma sary models import krein aor Base bhi and target_metadata = Base.metadata likh dain (Base.metadata --> complete bilkul
blueprint collection of all tables)
--> path parameter 
--> query parameter(filtering and searching purpose)  
