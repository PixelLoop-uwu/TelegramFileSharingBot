from pathlib import Path
from datetime import datetime, timezone
from random import choices
import string

from api.models import FileData


def get_file_data(id: str, name: str, path: Path) -> FileData:
  return FileData(
    id=id,
    name=name,
    size=path.stat().st_size,
    upload_time=datetime.now(timezone.utc).replace(second=0, microsecond=0),
    download_id=''.join(choices(string.ascii_letters + string.digits, k=8))
  )