from aiogram.utils import executor

from loader import dp
from utils.set_bot_commands import set_default_commands


async def on_start(dispatcher):
    await set_default_commands(dispatcher)


if __name__ == '__main__':
    print('bot run')
    executor.start_polling(dp)
