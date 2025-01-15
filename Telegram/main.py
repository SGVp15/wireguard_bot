from Telegram.modules.main.handlers.echo import router as echo_router
from Telegram.modules.main.handlers.start import router as start_router
from Telegram.loader import bot, dp
from Telegram.modules.admin.handlers.admin import router as admin_router
from Telegram.modules.user.handlers.files import router as file_router
from Telegram.modules.user.handlers.user import router as user_router

# dp.include_router(router)
dp.include_router(admin_router)
dp.include_router(file_router)
dp.include_router(user_router)
dp.include_router(start_router)
dp.include_router(echo_router)


async def start_bot():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
