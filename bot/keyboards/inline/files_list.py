from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import math

def actions_buttons_template(total_pages: int, current_page: int):
  actions_buttons_templates: dict = {
    1: [ 
      InlineKeyboardButton(text=f"{current_page} / {total_pages}", callback_data="null"),
      InlineKeyboardButton(text="››", callback_data="GONEXT")
    ],

    2: [ 
      InlineKeyboardButton(text="‹‹", callback_data="GOBACK"),
      InlineKeyboardButton(text=f"{current_page} / {total_pages}", callback_data="null"),
      InlineKeyboardButton(text="››", callback_data="GONEXT")
    ],

    3: [
      InlineKeyboardButton(text="‹‹", callback_data="GOBACK"),
      InlineKeyboardButton(text=f"{current_page} / {total_pages}", callback_data="null")
    ]
  }

  return actions_buttons_templates[current_page]


def get_files_keyboard(files_data: list, current_page: int) -> InlineKeyboardMarkup:

  total_pages: int = math.ceil(len(files_data) / 5)

  button_template = lambda i: InlineKeyboardButton(
    text=files_data[i].get("fullname"), 
    callback_data=f"OPENFILE:{files_data[i].get("id")}"
  )

  inline_keyboard = [
    [button_template(i)] for i in range(
      (current_page - 1) * 5, min(current_page * 5, len(files_data))
    )
  ]

  inline_keyboard.append(actions_buttons_template(total_pages, current_page))
  inline_keyboard.append([InlineKeyboardButton(text="<- Назад", callback_data="GOMAIN")])

  return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

