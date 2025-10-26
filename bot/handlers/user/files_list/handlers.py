from aiogram import Router as _Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from keyboards import menu, get_files_keyboard
from texts import greetings

Router = _Router()


@Router.callback_query(F.data == "GOBACK")
async def go_back(callback: CallbackQuery, state: FSMContext):
  data = await state.get_data()
  current_page = data.get("current_page", 1)

  current_page = current_page - 1

  files_data = data.get("files_data", [])

  await state.update_data(current_page=current_page)

  keyboard = get_files_keyboard(files_data, current_page)

  await callback.message.edit_reply_markup(reply_markup=keyboard)
  await callback.answer()


@Router.callback_query(F.data  == "GONEXT")
async def go_next(callback: CallbackQuery, state: FSMContext):
  data = await state.get_data()
  current_page = data.get("current_page", 1)

  files_data = data.get("files_data", [])

  current_page = current_page + 1

  await state.update_data(current_page=current_page)

  keyboard = get_files_keyboard(files_data, current_page)

  await callback.message.edit_reply_markup(reply_markup=keyboard)
  await callback.answer()


@Router.callback_query(F.data == "null")
async def go_back(callback: CallbackQuery):
  await callback.answer()
  

@Router.callback_query(F.data == "GOMAIN")
async def go_main(callback: CallbackQuery):
  await callback.message.edit_caption(
    caption=greetings, reply_markup=menu
  )


