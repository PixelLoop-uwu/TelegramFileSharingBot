from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_to_main: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text="<- Назад", callback_data="GOMAIN")
  ]
])