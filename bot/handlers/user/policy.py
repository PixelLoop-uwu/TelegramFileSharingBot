from aiogram import types
from aiogram import Router as _Router
from aiogram.filters import Command

from config import config
from keyboards import back_button

Router = _Router()


@Router.message(Command("policy"))
async def echo(message: types.Message) -> None:
  
  await message.answer_photo(
    photo = config.banner,
    caption = config.messages.policy,
    reply_markup = back_button,
    parse_mode="Markdown"
  )