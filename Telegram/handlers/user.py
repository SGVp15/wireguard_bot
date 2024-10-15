from typing import Dict, Any

from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext

from Telegram import keybords
from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.main import dp, bot
from Telegram.states.Form import Form
from WG import wg


# @dp.callback_query_handler(lambda c: c.data == 'create_user', user_id=[*ADMIN_ID, ], state=Menu.create_user_menu)
@dp.callback_query(
    F.data.in_({CallBackData.create_user_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
    , Form.create_user
)
async def create_user(callback_query: types.callback_query, state: FSMContext):
    data = await state.get_data()
    user = data.get('name')
    text, file = wg.create_user(user)
    await state.clear()
    with open(file, "rb") as f:
        await bot.send_document(chat_id=callback_query.from_user.id, document=f,
                                reply_markup=keybords.inline.main_menu)
