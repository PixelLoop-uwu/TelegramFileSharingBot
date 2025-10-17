from aiogram import Router as _Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.client import client
from keyboards import back_to_list

Router = _Router()


@Router.callback_query(F.data.startswith("DELETE:"))
async def handle_openfile(callback: CallbackQuery, state: FSMContext):

  temp = callback.data.split(":")
  file_id, file_name = temp[1], temp[2]
  
  try:
    client().delete_file(file_id, callback.from_user.id)

  except Exception as e:
    await callback.message.edit_caption(
      caption=f"☁️ *Произошла ошибка при удалении* {file_name}. {e}", 
      reply_markup=back_to_list,
      parse_mode="Markdown"
    )

    await callback.answer()
    return
  
  

  await callback.message.edit_caption(
    caption=f"☁️ *Файл* {file_name} *успешно удален!*", 
    reply_markup=back_to_list,
    parse_mode="Markdown"
  )

  await callback.answer()
