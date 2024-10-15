from aiogram import types, F
from aiogram.filters import Command

from Telegram import keybords
from Telegram.config import ADMIN_ID
from Telegram.main import dp


@dp.message(F.text.in_({'/start', '/help'}) & F.from_user.id.in_({*ADMIN_ID, }))
async def send_welcome_new_user(message: types.Message):
    text = f'Здравствуйте, {message.from_user.first_name}.'
    text += f'\n ❓/id - узнать ваш id'
    # message.text
    await message.answer(text=text, reply_markup=keybords.inline.main_menu)


@dp.message(F.command.in_({'start', 'help'}))
async def send_welcome_new_user(message: types.Message):
    text = f'Здравствуйте, {message.from_user.first_name}.'
    text += f'\n ❓/id - узнать ваш id'
    await message.answer(text=text)


@dp.message(Command('id'))
async def send_id(message: types.Message):
    await message.answer(str(message.chat.id))
