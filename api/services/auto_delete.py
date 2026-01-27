from datetime import datetime, timezone
from api.database.database import DatabaseManager
from api.services import delete_file
from shared.config import config

async def delete_old_files():
  async with DatabaseManager() as db:
    old_files = await db.get_old_files(
      datetime.now(timezone.utc), 
      config.period
    )

    if not old_files:
      return
    
    for file in old_files:
      await db.delete_file(
        file.get("user_id"), file.get("file_id")
      )

      await delete_file(
        config.storage_path / file.get("user_id") / file.get("file_id")
      )
    
    