from aiogram import F, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.main import dp, bot
from Telegram.modules.user.keyboards.menu_user import k_menu_user_create, k_back_to_menu_users, k_menu_users
from Telegram.modules.user.states.mashine_state import UserState


@dp.callback_query(
    (F.data == CallBackData.menu_users)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def user_menu(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(UserState.users_menu)
    await bot.edit_message_text(
        text='<b>[ Пользователи ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_users
    )


@dp.callback_query(
    (F.data == CallBackData.menu_create_user)
    & (F.from_user.id.in_({*ADMIN_ID, }))
)
async def create_user_menu(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(UserState.create_user_menu)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f'Введите имя пользователя\n'
             f'Пример: Иванов Иван',
        parse_mode=ParseMode.HTML,
        reply_markup=k_back_to_menu_users
    )


@dp.message(UserState.create_user_menu, F.from_user.id.in_({*ADMIN_ID, }))
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await state.update_data(name=message.text)
    await state.set_state(UserState.create_user)
    await bot.send_message(
        chat_id=message.chat.id, text=f'❔ Создать пользователя \n<b>{user}</b>',
        parse_mode=ParseMode.HTML,
        reply_markup=k_menu_user_create
    )
