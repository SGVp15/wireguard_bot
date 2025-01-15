from aiogram import types, F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from Telegram.Call_Back_Data import CALL_BACK_DATA
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.modules.main.keyboards.menu_main import k_main_menu
from Telegram.loader import bot, dp
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')



@dp.callback_query(
    (F.data == CALL_BACK_DATA.menu_main)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def back_to_main(callback_query: types.callback_query, state: FSMContext):
    await state.clear()
    await bot.edit_message_text(
        text='<b>[ MAIN ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_main_menu
    )
