from aiogram import Router as _Router


Router = _Router()

from . import start
from . import policy 

Router.include_router(start.Router)
Router.include_router(policy.Router)

from .files_list import handlers, menu

Router.include_router(menu.Router)
Router.include_router(handlers.Router)

from .file_menu import menu, handlers

Router.include_router(menu.Router)
Router.include_router(handlers.Router)

from .upload import handler

Router.include_router(handler.Router)