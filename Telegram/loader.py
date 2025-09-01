import asyncio

from aiogram import Bot, Router, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from Telegram import config

bot = Bot(token=str(config.BOT_TOKEN), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
print('-' * 30, config.BOT_TOKEN)
router = Router(name=__name__)
loop = asyncio.get_event_loop()
dp = Dispatcher(storage=MemoryStorage(), parse_mode=ParseMode.HTML)
