from pathlib import Path
from asyncio import get_running_loop

async def delete_file(file_path: Path):
  loop = get_running_loop()
  await loop.run_in_executor(None, file_path.unlink)