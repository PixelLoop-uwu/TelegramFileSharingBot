from aiogram import Router as _Router, F
from aiogram.types import CallbackQuery

from services import client
from keyboards import back_to_list

Router = _Router()


@Router.callback_query(F.data.startswith("DELETE:"))
async def handle_openfile(callback: CallbackQuery):

  async def sent_callback(message: str) -> None:
    await callback.message.edit_caption(  
      caption=message, 
      reply_markup=back_to_list(with_update=True),
      parse_mode="HTML"
    )

    await callback.answer()


  temp = callback.data.split(":")
  file_id, file_name = temp[1], temp[2]
  

  async with client as api:
    response = await api.delete_file(file_id, callback.from_user.id)

  if "error" in response:
    await sent_callback(f"☁️ <b>Произошла ошибка при удалении</b> {file_name}. {response.get("error")}")
    return


  await sent_callback(f"☁️ <b>Файл</b> {file_name} <b>успешно удален!</b>")


