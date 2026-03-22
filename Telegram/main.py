from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import root_config
from Utils.log import log

bot = Bot(token=root_config.BOT_TOKEN)

# loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(storage=storage, parse_mode=ParseMode.HTML)


async def start_bot():
    try:
        log.info("Запуск бота...")
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
