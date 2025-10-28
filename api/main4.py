from fastapi import FastAPI
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from contextlib import asynccontextmanager

from .routes import users, files
from .services import delete_old_files


api = FastAPI()
scheduler = AsyncIOScheduler()

api.include_router(users.router)
api.include_router(files.router)


@asynccontextmanager
async def lifespan(app: FastAPI):
  scheduler.add_job(delete_old_files, "interval", hour=1)
  scheduler.start()

  yield  

  scheduler.shutdown()

