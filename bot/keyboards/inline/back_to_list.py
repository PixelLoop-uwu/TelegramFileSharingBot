from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

back_to_list: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text="<- Назад", callback_data="MYFILES:N"),
  ]
])