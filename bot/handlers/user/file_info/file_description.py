from aiogram import Router as _Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards import get_actions_keyboard
from utils.message_generator import file_description_message

Router = _Router()
 

@Router.callback_query(F.data.startswith("OPENFILE:"))
async def handle_openfile(callback: CallbackQuery, state: FSMContext):

  file_id: str = callback.data.split(":")[1]
  data: dict = await state.get_data()

  file_info: dict = next((item for item in data.get("files_data") if item["id"] == file_id), None)

  await callback.message.edit_caption(
    caption=file_description_message(file_info),
    reply_markup=get_actions_keyboard(file_id, file_info.get("fullname")),
    parse_mode="Markdown"
  )

  await callback.answer()
