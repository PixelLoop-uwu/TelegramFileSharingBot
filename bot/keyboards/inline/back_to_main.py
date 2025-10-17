from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_button: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text="<- Назад", callback_data="GOMAIN")
  ]
])