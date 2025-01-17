from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.keyboards.menu_main import k_main_menu
from Telegram.loader import dp
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')


@dp.callback_query(
    (F.data == MyCallBackData.menu_main)
    & (F.from_user.id.in_({*ADMIN_ID, *USERS_ID}))
)
async def back_to_main(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.edit_text(
        text='<b>[ MAIN ]</b>',
        reply_markup=k_main_menu
    )
