import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from Telegram import config
from Telegram.handlers.echo import router as echo_router
from Telegram.handlers.start import router as start_router
from Telegram.modules.admin.handlers.admin import router as admin_router
from Telegram.modules.user.handlers.user import router as user_router

bot = Bot(token=config.BOT_TOKEN)
# router = Router(name=__name__)
loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(storage=storage, parse_mode=ParseMode.HTML)
dp.include_router(echo_router)
dp.include_router(start_router)
dp.include_router(admin_router)
dp.include_router(user_router)


async def start_bot():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
