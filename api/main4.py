from fastapi import FastAPI
from .routes import users, files


api = FastAPI()

api.include_router(users.router)
api.include_router(files.router)

