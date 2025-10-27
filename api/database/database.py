from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from datetime import datetime, timedelta

from api.models import FileData 
from .bases import Base, User, File


class UserNotFound(Exception):
  ...

class DatabaseManager:
  def __init__(self, db_url: str = "sqlite+aiosqlite:///api/database/storage.db"):
    self.engine = create_async_engine(db_url)
    self.Session = sessionmaker(
      bind=self.engine,
      expire_on_commit=False,
      class_=AsyncSession
    )


  async def _table_check(self):
    async with self.engine.begin() as conn:
      await conn.run_sync(Base.metadata.create_all)

  async def __aenter__(self):
    await self._table_check()
    return self

  async def __aexit__(self, exc_type, exc, tb):
    await self.engine.dispose()


  async def get_file_info(self, download_id: str) -> dict:
    async with self.Session() as session:
      stmt = select(File).where(File.download_id == download_id)
      result = await session.execute(stmt)
      file_obj = result.scalar_one_or_none()
      if file_obj:
        return {
          "file_id": file_obj.file_id,
          "file_name": file_obj.file_name,
          "size": file_obj.size,
          "upload_time": file_obj.upload_time,
          "downloads": file_obj.downloads,
          "download_id": file_obj.download_id,
          "user_id": file_obj.user_id
        }
      return {}
    
  async def get_user_data(self, user_id: int) -> list[dict]:
    async with self.Session() as session:
      stmt = select(File).where(File.user_id == user_id)
      result = await session.execute(stmt)
      files = result.scalars().all()

      return [
        {
          "file_id": f.file_id,
          "file_name": f.file_name,
          "size": f.size,
          "upload_time": f.upload_time.isoformat(),
          "downloads": f.downloads,
          "download_id": f.download_id
        }
        for f in files
      ]
    
  async def get_old_files(self, now: datetime, period: int) -> list:
    async with self.Session() as session:
      week_ago = now - timedelta(days=period)

      stmt = select(File).where(File.upload_time < week_ago)
      result = await session.execute(stmt)
      files = result.scalars().all()

      return files

  async def upload_file(self, user_id: int, file_data: FileData) -> dict:
    async with self.Session() as session:
      user = await session.get(User, user_id)
       
      if user is None:
        user = User(user_id=user_id)
        session.add(user)
        await session.commit()

      new_file = File(
        file_id=file_data.id,
        user_id=user_id,
        file_name=file_data.name,
        size=file_data.size,
        upload_time=file_data.upload_time,
        downloads=file_data.downloads,
        download_id=file_data.download_id
      )
      session.add(new_file)
      await session.commit()

  async def delete_file(self, user_id: int, file_id: str):
    async with self.Session() as session:
      stmt = select(File).where(File.file_id == file_id, File.user_id == user_id)
      result = await session.execute(stmt)
      file_obj = result.scalar_one_or_none()

      if file_obj is None:
        raise UserNotFound(f"Файл {file_id} для пользователя {user_id} не найден")

      await session.delete(file_obj)
      await session.commit()