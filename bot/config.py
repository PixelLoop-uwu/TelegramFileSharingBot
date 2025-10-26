from aiogram.types import FSInputFile

from dotenv import load_dotenv
import os

load_dotenv() 

class Config:
  token = os.getenv("BOT_TOKEN", "")
  admin_id = int(os.getenv("ADMIN_ID", "0"))

  api_host = "127.0.0.1"
  api_port = 8000

  files_limit = 20
  download_host = "https://share.pixelloop.ru"

  banner = FSInputFile("bot/background.jpg")

config = Config()