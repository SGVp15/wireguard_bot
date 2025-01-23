from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.loader import dp
from Telegram.modules.user.keyboards.menu_files import RENAME_CONFIG_FILE
from Telegram.modules.user.keyboards.menu_userConfig import k_menu_user_config_create, k_back_to_menu_users, \
    k_menu_users, \
    k_menu_user_config_rename
from Telegram.modules.user.states.mashine_state import UserState
from config import DEBUG
from wireguard.user_config import UserConfig

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
    (F.data == MyCallBackData.menu_config_user_create)
    & (F.from_user.id.in_({*ADMIN_ID, }))
)
async def create_user_menu(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(UserState.create_user_menu)
    await callback_query.message.edit_text(
        text=f'Введите имя пользователя\n'
             f'Пример: Иванов Иван',
        reply_markup=k_back_to_menu_users
    )


@dp.callback_query(RENAME_CONFIG_FILE.filter())
async def rename_user_menu(callback_query: CallbackQuery, callback_data: RENAME_CONFIG_FILE, state: FSMContext):
    user_config = UserConfig(callback_data.name)
    await state.set_state(UserState.rename_user)
    await state.update_data(user_config=user_config)
    await callback_query.message.edit_text(
        text=f'[ Переименовать ]\n'
             f'{user_config.name}\n'
             f'Введите новое название',
        reply_markup=k_back_to_menu_users
    )


@dp.message(UserState.create_user_menu, F.from_user.id.in_({*ADMIN_ID, }))
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await state.update_data(name=user)
    await state.set_state(UserState.create_user)
    await message.answer(
        text=f'❔ Создать пользователя \n'
             f'<b>{user}</b>',
        reply_markup=k_menu_user_config_create
    )


@dp.message(UserState.rename_user, F.from_user.id.in_({*ADMIN_ID, }))
async def q_rename_user(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_config: UserConfig = data.get('user_config')
    await state.set_state(UserState.rename_user)
    user_config.new_name = message.text
    await state.update_data(new_name=message.text)
    await message.answer(
        text=f'❔ Перименовать\n'
             f'<b>{user_config.name}</b> -> <b>{user_config.new_name}</b>',
        reply_markup=k_menu_user_config_rename
    )
