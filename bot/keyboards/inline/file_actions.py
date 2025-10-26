from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_actions_keyboard(file_id: str, file_name: str) -> InlineKeyboardMarkup:

  return InlineKeyboardMarkup(inline_keyboard=[
    [
      InlineKeyboardButton(text="<- Назад", callback_data="MYFILES:skip"),
      InlineKeyboardButton(text="Удалить", callback_data=f"DELETE:{file_id}:{file_name}")
    ]
  ])