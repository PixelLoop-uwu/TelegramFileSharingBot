from aiogram import Router as _Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.enums import ContentType
from aiogram.exceptions import TelegramBadRequest

from config import config
from services import client

Router = _Router()

@Router.message(F.content_type.in_({
  ContentType.DOCUMENT
}))
async def go_back(message: Message):

  user_id = message.from_user.id
  file_name = message.document.file_name


  async with client as api:
    data_state = await api.get_user_data(user_id)

    if len(data_state.get("data", {})) >= config.files_limit:
      await message.answer(text=(
        "☁️ *Вы привысили* лимит в *15 файлов!*\n\n"
        "_Удалите один из своих файлов чтобы загрузить новый_"
      ))
      return


  try:
    file = await message.bot.get_file(message.document.file_id)

    file_url = f"https://api.telegram.org/file/bot{config.token}/{file.file_path}"
 
    if len(file_name) > 20:
      await message.answer(text="☁️ *Длинна имени файла* не может превышать *20 символов!*")
      return

    async with client as api:
      responce = await api.upload_file(file_url=file_url, file_name=file_name, user_id=user_id)

    if "error" in responce:
      await message.answer(text=f"Ошибка загрузки файла: {responce.get("error")}")
      return

    await message.answer(
      text=(
        f"☁️ Файл <b>{responce.get('file_name')}</b> был успешно загружен!\n\n"
        f"☁️ Ссылка: <a href='{responce.get('download_url')}'>{responce.get('download_url')}</a>"
      ),
      parse_mode="HTML"
    )


  except TelegramBadRequest as e:
    if "file is too big" in str(e):
      await message.answer(
        "☁️ *Размер файл*а не может привышать *50Mb!*\n\n"
        "_Это ограничение телеграма_"
      )
