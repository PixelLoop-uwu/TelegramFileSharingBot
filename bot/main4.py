from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import config
from handlers import Router

bot = Bot(config.token, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(Router)

if __name__ == "__main__":
  import asyncio
  asyncio.run( dp.start_polling(bot) )
