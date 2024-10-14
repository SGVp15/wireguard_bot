from aiogram import types, F
from aiogram.fsm.context import FSMContext

from Telegram.main import bot, dp


@dp.callback_query(F.state.in_({'*', None}))
async def echo(callback_query: types.callback_query, state: FSMContext):
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f'Не понимаю, что это значит.\n'
                                f'callback_query\n'
                                f'Воспользуйтесь командой /help',
                           )


@dp.message()
async def echo(message: types.Message):
    await message.reply(
        'Не понимаю, что это значит.'
        'Воспользуйтесь командой /help',
    )
