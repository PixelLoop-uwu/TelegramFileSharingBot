from aiogram import types
from aiogram import Router as _Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import config
from keyboards import menu

Router = _Router()


@Router.message(Command("start"))
async def echo(message: types.Message, state: FSMContext) -> None:
  await state.update_data(current_page=1)

  await message.answer_photo(
    photo=config.banner,
    caption=config.messages.greetings,
    reply_markup=menu,
    parse_mode="Markdown"
  )