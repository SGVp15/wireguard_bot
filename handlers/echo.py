from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot


@dp.callback_query_handler(state=['*', None])
async def echo(callback_query: types.callback_query, state: FSMContext):
    await bot.send_message(chat_id=callback_query.from_user.id, text=f'Не понимаю, что это значит.\n'
                                                                     f'callback_query\n'
                                                                     f'Воспользуйтесь командой /help',
                           )


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply('Не понимаю, что это значит.'
                        'Воспользуйтесь командой /help',
                        )
