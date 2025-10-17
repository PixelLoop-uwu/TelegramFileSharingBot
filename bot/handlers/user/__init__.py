from aiogram import Router as _Router

from . import start
from . import policy 

from .my_files import files_list
from .my_files import page_hadlers

from .file_info import file_description
from .file_info import file_handlers

Router = _Router()

Router.include_router(start.Router)
Router.include_router(policy.Router)

Router.include_router(files_list.Router)
Router.include_router(page_hadlers.Router)

Router.include_router(file_description.Router)
Router.include_router(file_handlers.Router)