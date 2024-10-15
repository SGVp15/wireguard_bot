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


@dp.callback_query(Form.create_user,
    F.data.in_({CallBackData.create_user_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def create_user(callback_query: types.callback_query, state: FSMContext):
    print('create_user')
    data = await state.get_data()
    user = data.get('name')
    print(f'{user}')
    text, file = wg.create_user(user)
    await state.clear()
    with open(file, "rb") as f:
        await bot.send_document(chat_id=callback_query.from_user.id, document=f,
                                reply_markup=keybords.inline.main_menu)
