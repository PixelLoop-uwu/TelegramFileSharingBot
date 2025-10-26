from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import math


def actions_buttons_template(total_pages: int, current_page: int):
  buttons = []

  if current_page > 1:
    buttons.append(InlineKeyboardButton(text="‹‹", callback_data="GOBACK"))

  buttons.append(
    InlineKeyboardButton(text=f"{current_page} / {total_pages}", callback_data="null")
  )

  if current_page < total_pages:
    buttons.append(InlineKeyboardButton(text="››", callback_data="GONEXT"))

  return buttons


def get_files_keyboard(files_data: list, current_page: int) -> InlineKeyboardMarkup:
  total_pages = max(1, math.ceil(len(files_data) / 5))

  current_page = max(1, min(current_page, total_pages))

  inline_keyboard = []

  start_idx = (current_page - 1) * 5
  end_idx = min(current_page * 5, len(files_data))

  for i in range(start_idx, end_idx):
    file = files_data[i]
    inline_keyboard.append([
      InlineKeyboardButton(
        text=file.get("file_name", "Без имени"),
        callback_data=f"OPENFILE:{file.get('file_id')}"
      )
    ])

  if total_pages > 1:
    inline_keyboard.append(actions_buttons_template(total_pages, current_page))

  inline_keyboard.append([InlineKeyboardButton(text="<- Назад", callback_data="GOMAIN")])

  return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)