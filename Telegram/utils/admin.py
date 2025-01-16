from aiogram.enums import ParseMode

from Telegram.config import ADMIN_ID
from Telegram.loader import bot


async def send_message_to_admins(text: str):
    for chat_id in ADMIN_ID:
        await bot.send_message(chat_id=chat_id, text=text, parse_mode=ParseMode.HTML)
