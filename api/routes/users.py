from fastapi import APIRouter
from ..database.database import DatabaseManager


router = APIRouter()

@router.get("/user")
async def get_user_data(user_id: int) -> dict:
  async with DatabaseManager() as db:
    return {"user_id": user_id, "data": await db.get_user_data(user_id)}
