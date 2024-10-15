from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.keybords.inline import main_menu
from Telegram.keybords.menu_user import k_menu_users, k_back_to_menu_users, k_menu_user_create
from Telegram.keybords.menu_admin import k_menu_admin, k_menu_restart_service
from Telegram.main import dp, bot
from Telegram.states.Form import Form


@dp.callback_query(
    (F.data == CallBackData.menu_main)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def back_to_main(callback_query: types.callback_query, state: FSMContext):
    await state.clear()
    await bot.edit_message_text(
        text='<b>[ MAIN ]</b>',
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=main_menu
    )

# ---  ADMIN   ---  ADMIN   ---  ADMIN   ---  ADMIN   ---  ADMIN   --- 
@dp.callback_query(
    (F.data == CallBackData.menu_admin)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def admin_menu(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.admin_menu)
    await bot.edit_message_text(
        text='<b>[ ADMIN ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_admin
    )

@dp.callback_query(
    (F.data == CallBackData.menu_admin)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def menu_restart_service_wg(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.menu_restart_service_wg)
    await bot.edit_message_text(
        text='<b>[ Перезагрузить службу WG ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_restart_service
    )





# ---  USER   ---  USER   ---  USER   ---  USER   ---  USER   --- 
@dp.callback_query(
    (F.data == CallBackData.menu_users)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def user_menu(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.users_menu)
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
    await state.set_state(Form.create_user_menu)
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text=f'Введите имя пользователя\n'
             f'Пример: Иванов Иван',
        parse_mode=ParseMode.HTML,
        reply_markup=k_back_to_menu_users
    )


@dp.message(Form.create_user_menu, F.from_user.id.in_({*ADMIN_ID, }))
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await state.update_data(name=message.text)
    await state.set_state(Form.create_user)
    await bot.send_message(
        chat_id=message.chat.id, text=f'❔ Создать пользователя \n<b>{user}</b>',
        parse_mode=ParseMode.HTML,
        reply_markup=k_menu_user_create
    )
