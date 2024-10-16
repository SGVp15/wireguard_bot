from aiogram import types, F, Router
from aiogram.fsm.context import FSMContext

from Telegram.main import bot, dp

router = Router()


@router.callback_query()
async def echo(callback_query: types.callback_query, state: FSMContext):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f'Не понимаю, что это значит.\n'
             f'callback_query\n'
             f'Воспользуйтесь командой /help',
    )


@router.message(F.text.in_({'start', 'help', '/help'}))
async def echo(message: types.Message):
    await message.reply(
        f'ADMIN_ID\n Не понимаю, что это значит.'
        'Воспользуйтесь командой /help',
    )


@router.message()
async def echo(message: types.Message):
    await message.reply(
        f'[{message.text}] --- Не понимаю, что это значит.'
        'Воспользуйтесь командой /help',
    )
