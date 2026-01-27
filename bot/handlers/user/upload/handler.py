from aiogram import Router as _Router, F
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from pathlib import Path

from shared.config import config
from bot.services import client

Router = _Router()

@Router.message(
  (F.document | F.photo | F.video | F.audio),
  ~F.voice,
  ~F.video_note
)
async def handle_upload(message: Message):
  user_id = message.from_user.id
    
  if message.document:
    media = message.document
    file_name = media.file_name or media.file_unique_id
  elif message.video:
    media = message.video
    file_name = media.file_name or f"{media.file_unique_id}.mp4"
  elif message.audio:
    media = message.audio
    file_name = media.file_name or f"{media.file_unique_id}.mp3"
  elif message.photo:
    media = message.photo[-1]
    file_name = f"{media.file_unique_id}.jpg"
  else:
    return

  async with client as api:
    data_state = await api.get_user_data(user_id)
    if len(data_state.get("data", [])) >= config.files_limit:
      return await message.answer("☁️ Превышен лимит в 15 файлов!")

    if len(file_name) > 20:
      fp = Path(file_name)
      file_name = fp.stem[:14] + fp.suffix

    try:
      file = await message.bot.get_file(media.file_id)
      file_url = f"https://api.telegram.org/file/bot{config.token}/{file.file_path}"

      async with client as api:
        response = await api.upload_file(
          file_url=file_url, 
          file_name=file_name, 
          user_id=user_id
        )

      if "error" in response:
        return await message.answer(f"Ошибка: {response.get('error')}")

      await message.answer(
        f"☁️ Файл <b>{response.get('file_name')}</b> был успешно загружен!\n\n"
        f"☁️ Ссылка: <a href='{response.get('download_url')}'>{response.get('download_url')}</a>",
        parse_mode="HTML"
      ) 

    except TelegramBadRequest as e:
      if "file is too big" in str(e):
        await message.answer("☁️ Файл слишком тяжелый для обычного бота (max 20MB на скачивание)")
      else:
        await message.answer(f"Произошла ошибка API: {e}")