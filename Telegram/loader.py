import asyncio

from aiogram import Bot, Router, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from Telegram import config

bot = Bot(token=config.BOT_TOKEN)
router = Router(name=__name__)
loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(storage=storage, parse_mode=ParseMode.HTML)
