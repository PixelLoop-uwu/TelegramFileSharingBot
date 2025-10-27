from pathlib import Path

class Config:
  storage_path: Path = Path('./data')
  server_domain: str = "https://share.pixelloop.ru"
  period: int = 7

config = Config()
  