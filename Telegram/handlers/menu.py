from random import setstate

from aiogram import types, F
from aiogram.fsm.context import FSMContext

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.keybords.inline import main_menu
from Telegram.keybords.users import users_menu, back_to_users_menu, user_create_menu
from Telegram.main import dp, bot
from Telegram.states.Form import Form


@dp.callback_query((F.data == CallBackData.menu_users)
                   & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID})))
async def user_menu(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.users_menu)
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=users_menu)


@dp.callback_query(
    (F.data == CallBackData.admin_menu)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def admin_menu(callback_query: types.callback_query):
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=main_menu)


@dp.callback_query(
    F.data == CallBackData.menu_create_user
    and F.from_user.id.in_({*ADMIN_ID, })
)
async def create_user_menu(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.create_user_menu)
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f'<b>Введите имя пользователя</b>\n'
                                f'Пример: Иванов Иван',
                           reply_markup=back_to_users_menu
                           )


@dp.message(Form.create_user_menu)
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await bot.send_message(chat_id=message.chat.id, text=f'❔ Создать пользователя \n<b>{user}</b>',
                           reply_markup=user_create_menu
                           )

    await state.update_data(name=message.text)
    await state.set_state(Form.create_user)


@dp.callback_query(
    (F.data == CallBackData.menu_main)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def back_to_main(callback_query: types.callback_query, state: FSMContext):
    await state.clear()
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=main_menu)
