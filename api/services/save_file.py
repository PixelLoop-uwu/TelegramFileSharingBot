import aiohttp
from pathlib import Path
import aiofiles


class DownloadError(Exception):
  ...


async def download_file(url: str, file_path: Path) -> None:
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      file_path.parent.mkdir(parents=True, exist_ok=True)

      if response.status != 200:
        raise DownloadError(f"Не удалось скачать файл: {response.status}")

      async with aiofiles.open(file_path, 'wb') as f:
        while True:
          chunk = await response.content.read(1024*1024)
          if not chunk:
            break
          await f.write(chunk)
