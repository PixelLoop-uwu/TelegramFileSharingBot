from pathlib import Path

class Config:
  storage_path: Path = Path('./data')
  server_domain: str = "https://share.pixelloop.ru"

config = Config()
  