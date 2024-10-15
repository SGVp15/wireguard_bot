from aiogram import types, F
from aiogram.fsm.context import FSMContext

from Telegram import keybords
from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.main import dp, bot
from Telegram.states.Form import Form


@dp.callback_query(F.data == CallBackData.menu_users and F.from_user.id.in_({*ADMIN_ID, }))
async def users_menu(callback_query: types.callback_query):
    await Form.users_menu.set()
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=keybords.users.users_menu)


@dp.callback_query(F.data == CallBackData.menu_create_user and F.from_user.id.in_({*ADMIN_ID, }))
async def create_user_menu(callback_query: types.callback_query, state: FSMContext):
    await Form.create_user_menu.set()
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f'<b>Введите имя пользователя</b>\n'
                                f'Пример: Иванов Иван',
                           reply_markup=keybords.users.back_to_users_menu
                           )


@dp.message(state=Form.create_user_menu)
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await state.update_data(contact=user)
    await bot.send_message(chat_id=message.chat.id, text=f'❔ Создать пользователя <b>{user}</b>',
                           reply_markup=keybords.users.user_create_menu)


@dp.callback_query(F.data == 'main_menu', state=['*', None])
async def main_menu(callback_query: types.callback_query, state: FSMContext):
    text = f'Этот бот работает с WG.'
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=keybords.inline.main_menu)
    await Form.main_menu.set()
