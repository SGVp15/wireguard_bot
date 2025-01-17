from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.loader import dp
from Telegram.modules.user.keyboards.menu_user import k_menu_user_create, k_back_to_menu_users, k_menu_users
from Telegram.modules.user.states.mashine_state import UserState
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')


@dp.callback_query(
    (F.data == MyCallBackData.menu_users)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def user_menu(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.edit_text(
        text='<b>[ Пользователи ]</b>',
        reply_markup=k_menu_users
    )
    await state.set_state(UserState.users_menu)


@dp.callback_query(
    (F.data == MyCallBackData.menu_create_user)
    & (F.from_user.id.in_({*ADMIN_ID, }))
)
async def create_user_menu(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.create_user_menu)
    await callback_query.message.edit_text(
        text=f'Введите имя пользователя\n'
             f'Пример: Иванов Иван',
        reply_markup=k_back_to_menu_users
    )


@dp.message(UserState.create_user_menu, F.from_user.id.in_({*ADMIN_ID, }))
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await state.update_data(name=message.text)
    await state.set_state(UserState.create_user)
    await message.answer(
        text=f'❔ Создать пользователя \n<b>{user}</b>',
        reply_markup=k_menu_user_create
    )
