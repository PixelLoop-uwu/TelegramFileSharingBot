from aiogram import Router as _Router
from . import user

Router = _Router()
Router.include_router(user.Router)

