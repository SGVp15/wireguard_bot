from aiogram import types, F
from aiogram.fsm.context import FSMContext

from aiogram.filters import Command

from Telegram.Call_Back_Data import CallBackData
from Telegram.keybords.inline import inline_kb_main
from root_config import ADMIN_ID, USERS_ID, VERSION
from Telegram.keybords import inline
from Telegram.main import dp, bot


@dp.message(F.command.in_({'start', 'help'}) & F.from_user.id.in_({*ADMIN_ID}))
async def send_welcome_admin(message: types.Message, state: FSMContext):
    text = f'Здравствуйте , {message.from_user.first_name}! \n'
    text += f'Этот бот работает с ProctorEDU.'
    text += f'\n ❓/id - узнать ваш id'
    text += f'\n Version = {VERSION}'
    await message.answer(text=text, reply_markup=inline.inline_kb_main)


@dp.message(F.command.in_({'start', 'help'}) & F.from_user.id.in_({*USERS_ID}))
async def send_welcome_new_user(message: types.Message):
    text = f'Здравствуйте, {message.from_user.first_name}.'
    text += f'\n ❓/id - узнать ваш id'
    text += f'\n Version = {VERSION}'
    await message.answer(text=text, reply_markup=inline.inline_kb_main)


@dp.message(Command('start', 'help'))
async def send_welcome(message: types.Message):
    text = f'Здравствуйте, {message.from_user.first_name}.'
    text += f'\n ❓/id - узнать ваш id'
    text += f'\n Version = {VERSION}'

    await message.answer(text=text, reply_markup=inline.inline_kb_main)


@dp.callback_query(F.data.in_({CallBackData.SHOW_VERSION}))
async def btn_sent_report_and_cert_lk(callback_query: types.callback_query):
    await bot.send_message(text=f'{VERSION}', chat_id=callback_query.from_user.id,
                           reply_markup=inline_kb_main)


@dp.message(Command('id'))
async def send_id(message: types.Message):
    await message.answer(str(message.chat.id))
