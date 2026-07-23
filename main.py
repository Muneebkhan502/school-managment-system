from fastapi import FastAPI
# from fastapi.responses import JSONResponse
# # from database import engine,Base
# from routers import student,classes, user, auth
# from exceptions import AppException, NotFoundException, UnauthorizedException, ForbiddenException
# import traceback
# import sys

# try:
#     from routers import student, classes, user, auth
# except Exception as e:
#     print("IMPORT ERROR:", e)
#     traceback.print_exc()
#     sys.exit(1)
app = FastAPI() # the engine has been started with name of app
@app.get("/")
def home():
    return {"message": "Hello Debugger!"}
# #Global Exception
# @app.exception_handler(AppException) 
# async def exception_handler(request: Request, exc: AppException):
#     return JSONResponse(
#         status_code = exc.status_code,
#         content = {
#             "status" : "error",
#             "code" : exc.status_code,
#             "message" : exc.message,
#             "field" : exc.field
#         }
#     )

    
# app.include_router(student.router, prefix="/students", tags=["Students"]) # tags helps us in grouping in swagger UI
# app.include_router(classes.router, prefix="/classes", tags=["Classes"])
# app.include_router(user.router, prefix="/users", tags=["Users"]) 
# app.include_router(auth.router, prefix="/auth", tags=["Authentication"]) 