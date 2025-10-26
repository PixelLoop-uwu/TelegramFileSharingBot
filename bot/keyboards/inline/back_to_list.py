from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_to_list(with_update: bool) -> InlineKeyboardMarkup:
  suffix = "skip" if not with_update else ""
  return InlineKeyboardMarkup(inline_keyboard=[
    [
      InlineKeyboardButton(
        text="<- Назад",
        callback_data=f"MYFILES:{suffix}",
      ),
    ]
  ])