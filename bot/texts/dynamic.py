from humanize import naturalsize
from datetime import datetime, timedelta
from config import config


def file_description_message(file_data: dict) -> str:
  upload_date_str = file_data.get("upload_time")
    
  upload_date = datetime.fromisoformat(upload_date_str)
  delete_date = upload_date + timedelta(days=7)
    
  return (
    "🌨️ <b>Информация о файле:</b>\n\n"
    f"☁️ <b>Название:</b> {file_data.get('file_name')}\n"
    f"☁️ <b>Размер:</b> {naturalsize(file_data.get('size'))}\n\n"
    f"☁️ <b>Дата загрузки:</b> {upload_date.strftime('%d.%m.%Y')}\n"
    f"☁️ <b>Будет удален:</b> {delete_date.strftime('%d.%m.%Y')}\n\n"
    f"☁️ <b>Ссылка:</b> {config.download_host}/{file_data.get('download_id')}\n"
    f"☁️ <b>Скачали:</b> {file_data.get('downloads')}"
  )

