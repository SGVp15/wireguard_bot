from aiogram import types

import Telegram.loader


async def set_default_commands(dp):
    await Telegram.loader.bot.set_my_commands(
        [
            types.BotCommand('start', 'Запуcтить бота'),
            types.BotCommand('help', 'Вывести справку'),
            types.BotCommand('create_user', 'Создать пользователя'),
        ]
    )
