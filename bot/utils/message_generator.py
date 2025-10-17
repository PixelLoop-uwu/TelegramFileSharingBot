from humanize import naturalsize
from datetime import datetime, timedelta

def file_description_message(file_data: dict) -> str:
    upload_date = file_data.get("upload_date")
    
    upload_datetime = datetime(
        year=upload_date[2],
        month=upload_date[1],
        day=upload_date[0],
        hour=upload_date[3],
        minute=upload_date[4]
    )
    delete_date = upload_datetime + timedelta(days=7)
    
    return (
        f"☁️ *Название:* {file_data.get('fullname')}\n"
        f"☁️ *Размер:* {naturalsize(file_data.get('size'))}\n\n"
        f"☁️ *Дата загрузки:* {upload_date[0]}.{upload_date[1]}.{upload_date[2]} {upload_date[3]}:{upload_date[4]}\n"
        f"☁️ *Будет удален:* {delete_date.strftime('%d.%m.%Y %H:%M')}\n\n"
        f"☁️ *Ссылка на файл*: {file_data.get('download_link')}\n"
        f"☁️ *Скачали*: {file_data.get('downloads')}"
    )