import asyncio

from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from Telegram import config

bot = Bot(token=config.BOT_TOKEN)
router  = Router(name=__name__)
loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(storage=storage, parse_mode=ParseMode.HTML)


async def start_bot():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
