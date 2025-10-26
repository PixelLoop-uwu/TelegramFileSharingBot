from aiogram import Router as _Router, F
from aiogram.types import Message
from aiogram.enums import ContentType

from config import config
from services import client
from keyboards import back_to_list

Router = _Router()

@Router.message(F.content_type == ContentType.DOCUMENT)
async def go_back(message: Message):
  async def sent_callback(text: str) -> None:

    await message.answer_photo(
      photo=config.banner,
      caption=text, 
      reply_markup=back_to_list(with_update=True)
    )

  file = await message.bot.get_file(message.document.file_id)

  file_url = f"https://api.telegram.org/file/bot{config.token}/{file.file_path}"
  file_name = message.document.file_name 
  user_id = message.from_user.id


  responce = await client.upload_file(file_url=file_url, file_name=file_name, user_id=user_id)

  if "error" in responce:
    await sent_callback(f"Ошибка загрузки файла: {responce.get("error")}")
    return


  await sent_callback(
    (
      f"Файл {responce.get('file_name')} был успешно загружен!\n\n" 
      f"Ссылка: {responce.get('file_url')}"
    )
  )
