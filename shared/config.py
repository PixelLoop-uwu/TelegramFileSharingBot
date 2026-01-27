import tomllib
from pathlib import Path
from pydantic import BaseModel, ConfigDict
from dotenv import load_dotenv
from aiogram.types import FSInputFile
import os

load_dotenv()

class Config(BaseModel):
  model_config = ConfigDict(arbitrary_types_allowed=True)

  tg_token: str
  app_token: str

  banner: FSInputFile
  admins_id: list[int]

  host: str
  port: int

  files_limit: int
  days_before_delete: int

  storage_path: Path
  download_url: str


def load_config(config_path: Path = Path("config.toml")) -> Config:
  f = config_path.read_text("utf-8")
  toml = tomllib.loads(f) 

  flat_config = {}
  for category_dict in toml.values():
    if isinstance(category_dict, dict):
      flat_config.update(category_dict)
      
    if category_dict.get("banner", None):
      flat_config["banner"] = FSInputFile(flat_config["banner"])

    if category_dict.get("storage_path", None):
      flat_config["storage_path"] = Path(flat_config["storage_path"])

    flat_config["tg_token"] = os.getenv("bot_token")
    flat_config["app_token"] = os.getenv("app_token")

  return Config(**flat_config)


config = load_config()