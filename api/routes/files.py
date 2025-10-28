from fastapi import APIRouter, Body
from fastapi.responses import FileResponse
from pathlib import Path
import uuid


from api.models import UploadFileRequest, DeleteFileRequest, FileData
from api.services import download_file, get_file_data, delete_file
from api.database.database import DatabaseManager
from api.config import config


router = APIRouter()


@router.post("/upload")
async def upload_file(request: UploadFileRequest) -> dict:
  file_id = str(uuid.uuid4())
  file_path = config.storage_path / str(request.user_id) / file_id

  try:
    await download_file(request.file_url, file_path)
  except Exception as e: 
    return {"error": str(e)}
  
  file_data: FileData = get_file_data(file_id, request.file_name, file_path)
  download_url = f"{config.download_host}/{file_data.download_id}"

  async with DatabaseManager() as db:
    await db.upload_file(request.user_id, file_data)

  return {"status": "ok", "download_url": download_url, "file_name": request.file_name}


@router.delete("/delete")
async def upload_file(request: DeleteFileRequest = Body(...)) -> dict:
  async with DatabaseManager() as db:
    try:  
      await db.delete_file(request.user_id, request.file_id)
    except Exception as e:
      return {"error": str(e)}
    
    file_path = config.storage_path / str(request.user_id) / request.file_id

    try:
      await delete_file(file_path)

    except FileNotFoundError as e:
      return {"error": e}

    return {"status": "ok"}


@router.get("/{download_id}")
async def download(download_id: str):
  async with DatabaseManager() as db:
    file_data = await db.get_file_info(download_id)

    if not file_data:
      return {"error": "Файл не найден"}

    await db.increment_downloads(file_data.get("user_id"), file_data.get("file_id"))

    file_path = config.storage_path / str(file_data.get("user_id")) / file_data.get("file_id")
    return FileResponse(file_path, media_type="application/octet-stream", filename=file_data.get("file_name"))
