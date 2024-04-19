from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from Telegram.states.Menu import Menu


@dp.callback_query_handler(lambda c: c.data == 'users_menu', state=['*', None])
async def users_menu(callback_query: types.callback_query):
    await Menu.users_menu.set()
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=Telegram.keybords.users.users_menu)


@dp.callback_query_handler(lambda c: c.data == 'create_user_menu', state=['*', None])
async def create_user_menu(callback_query: types.callback_query, state: FSMContext):
    await Menu.create_user_menu.set()
    await bot.send_message(chat_id=callback_query.from_user.id,
                           text=f'<b>Введите имя пользователя</b>\n'
                                f'Пример: Иванов Иван',
                           reply_markup=Telegram.keybords.users.back_to_users_menu
                           )


@dp.message_handler(state=Menu.create_user_menu)
async def user_create(message: types.Message, state: FSMContext):
    user = message.text
    await state.update_data(contact=user)
    await bot.send_message(chat_id=message.chat.id, text=f'❔ Создать пользователя <b>{user}</b>',
                           reply_markup=Telegram.keybords.users.user_create)


@dp.callback_query_handler(lambda c: c.data == 'main_menu', state=['*', None])
async def main_menu(callback_query: types.callback_query, state: FSMContext):
    text = f'Этот бот работает с WG.'
    await bot.edit_message_reply_markup(chat_id=callback_query.from_user.id,
                                        message_id=callback_query.message.message_id,
                                        reply_markup=Telegram.keybords.inline.main_menu)
    await Menu.main_menu.set()
