from aiogram.types import Message
from aiogram import Router as _Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from texts import greetings
from config import config
from keyboards import menu

Router = _Router()


@Router.message(Command("start"))
async def echo(message: Message, state: FSMContext) -> None:
  await state.update_data(current_page=1)

  await message.answer_photo(
    photo=config.banner, 
    caption=greetings, 
    reply_markup=menu
  )
