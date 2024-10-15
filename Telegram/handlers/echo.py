from aiogram import types, F
from aiogram.fsm.context import FSMContext

from Telegram.config import ADMIN_ID
from Telegram.main import bot, dp


@dp.callback_query()
async def echo(callback_query: types.callback_query, state: FSMContext):
    print(callback_query)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f'Не понимаю, что это значит.\n'
             f'callback_query\n'
             f'Воспользуйтесь командой /help',
    )


@dp.message(F.text.in_({'start','help', '/help'}))
async def echo(message: types.Message):
    print(f'[{message.from_user.id}]')
    print(f'{*ADMIN_ID,}')
    print(f'{message}')
    await message.reply(
        f'ADMIN_ID [{message.from_user.id}]\n Не понимаю, что это значит.'
        'Воспользуйтесь командой /help',
    )


@dp.message()
async def echo(message: types.Message):
    await message.reply(
        f'[{message.text}] --- Не понимаю, что это значит.'
        'Воспользуйтесь командой /help',
    )
