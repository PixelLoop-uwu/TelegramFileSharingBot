from aiogram import types
from aiogram import Router as _Router
from aiogram.filters import Command

from config import config
from texts import policy
from keyboards import back_to_main

Router = _Router()


@Router.message(Command("policy"))
async def echo(message: types.Message) -> None:
  await message.answer_photo(
    photo=config.banner, 
    caption=policy, 
    reply_markup=back_to_main,
    parse_mode="HTML"
  )