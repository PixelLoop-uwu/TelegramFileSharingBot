from fastapi import APIRouter, Depends
from api.database.database import DatabaseManager
from api.permission import admin_check


router = APIRouter()

@router.get("/user")
async def get_user_data(user_id: int, admin = Depends(admin_check)) -> dict:
  async with DatabaseManager() as db:
    return {"user_id": user_id, "data": await db.get_user_data(user_id)}
