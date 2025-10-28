from aiogram.types import FSInputFile
from pathlib import Path

from dotenv import load_dotenv
import os

load_dotenv() 


class Config:
  token = os.getenv("BOT_TOKEN", "")
  admins_id = [6058443893] 

  api_host = "127.0.0.1"
  api_port = 8000

  files_limit = 20
  days_before_detele = 7
  storage_path: Path = Path('./data')
  
  download_host = "https://share.pixelloop.ru"
  banner = FSInputFile("bot/background.jpg")




  