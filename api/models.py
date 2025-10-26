from pydantic import BaseModel
from datetime import datetime


class UserRequest(BaseModel):
  user_id: int

class UploadFileRequest(BaseModel):
  file_url: str
  file_name: str
  user_id: int

class DeleteFileRequest(BaseModel):
  file_id: str
  user_id: int

class FileData(BaseModel):
  
  """
  :id: str
  :name: str
  :size: int
  :upload_time: list
  :downloads: int = 0
  """

  id: str
  name: str
  size: int
  download_id: str
  downloads: int = 0
  upload_time: datetime