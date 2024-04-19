from aiogram import types
from aiogram.dispatcher import FSMContext

from WG import wg
from Telegram.config import ADMIN_ID
from loader import dp, bot
from Telegram.states.Menu import Menu


# @dp.callback_query_handler(lambda c: c.data == 'create_user', state=['*', None])
@dp.callback_query_handler(lambda c: c.data == 'create_user', user_id=[*ADMIN_ID, ], state=Menu.create_user_menu)
async def create_user(callback_query: types.callback_query, state: FSMContext):
    data = await state.get_data()
    user = data.get('contact')
    text, file = wg.create_user(user)
    await state.reset_state()
    with open(file, "rb") as f:
        await bot.send_document(chat_id=callback_query.from_user.id, document=f,
                                reply_markup=Telegram.keybords.users.users_menu)
