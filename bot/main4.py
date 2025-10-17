from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config import config
from handlers import Router

bot = Bot(config.token)
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(Router)

if __name__ == "__main__":
  import asyncio
  asyncio.run( dp.start_polling(bot) )
