from aiogram.types import CallbackQuery
from aiogram import Router as _Router, F

from aiogram.fsm.context import FSMContext

from bot.services import client
from bot.keyboards import get_files_keyboard, back_to_main

Router = _Router()


@Router.callback_query(F.data.startswith("MYFILES:"))
async def process_callback(callback: CallbackQuery, state: FSMContext):

  data_state = await state.get_data()
  current_page = data_state.get("current_page", 1)


  if not callback.data.split(":")[1]:
    
    async with client as api:
      response = await api.get_user_data(callback.from_user.id)

    if "error" in response:
      await callback.message.edit_caption(
        f'Ошибка api: {response.get("error")}',
        reply_markup=back_to_main
      )
      return

    files_data = response.get("data", {})
    await state.update_data(files_data=files_data, current_page=current_page)

  else:
    files_data = data_state.get("files_data", {})
    

  if not files_data:
    await callback.message.edit_caption(
      caption=(
        "💭 Вы еще не загрузили ни одного файла.\n\n"
        "_Чтобы загрузить файл, просто отправьте его в чат_"
      ), 
      reply_markup=back_to_main
    )
    return


  keyboard = get_files_keyboard(files_data, current_page)

  await callback.message.edit_caption(
    caption="💭 Выберите нужный файл:", 
    reply_markup=keyboard
  )
  
  await callback.answer()