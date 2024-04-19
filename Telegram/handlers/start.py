from aiogram import types
from aiogram.fsm.context import FSMContext

from Telegram import keybords
from Telegram.config import USERS_ID
from Telegram.main import dp


@dp.message_handler(commands=['start', 'help']
                    # , user_id=[*ADMIN_ID, ]
                    # , state=['*', None]
                    )
async def send_welcome_admin(message: types.Message, state: FSMContext):
    # await Menu.Menu.main_menu.set()
    text = f'Здравствуйте , {message.from_user.first_name}! \n'
    text += f'Этот бот работает с Wireguard.'
    text += f'\n ❓/id - узнать ваш id'
    await message.answer(text=text, reply_markup=keybords.inline.main_menu)


@dp.message_handler(commands=['start', 'help'], user_id=[*USERS_ID, ], state=['*', None])
async def send_welcome_new_user(message: types.Message):
    text = f'Здравствуйте, {message.from_user.first_name}.'
    text += f'\n ❓/id - узнать ваш id'
    await message.answer(text=text, reply_markup=keybords.inline.main_menu)


@dp.message_handler(commands=['start', 'help'], state=['*', None])
async def send_welcome(message: types.Message):
    text = f'Здравствуйте, {message.from_user.first_name}.'
    text += f'\n ❓/id - узнать ваш id'
    await message.answer(text=text, reply_markup=keybords.inline.main_menu)


@dp.message_handler(commands='id')
async def send_id(message: types.Message):
    await message.answer(message.chat.id)
