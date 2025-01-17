from aiogram import F
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID
from Telegram.loader import bot, dp
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin, k_menu_restart_service, k_menu_reboot_server
from Telegram.states.Form import Form
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')


@dp.callback_query(
    (F.data == MyCallBackData.menu_admin)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def show_admin_menu(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.admin_menu)
    text = '<b>[ ADMIN ]</b>'
    kb = k_menu_admin
    try:
        await callback_query.message.edit_text(
            text=text,
            reply_markup=kb
        )
    except Exception as e:
        await bot.send_message(
            chat_id=callback_query.from_user.id,
            text=text,
            reply_markup=kb
        )


@dp.callback_query(
    (F.data == MyCallBackData.menu_restart_service_wg)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def menu_restart_service_wg(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.menu_restart_service_wg)
    await bot.edit_message_text(
        text='<b>[ Перезагрузить службу wireguard ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_restart_service
    )


@dp.callback_query(
    (F.data == MyCallBackData.menu_reboot_server)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def menu_reboot_server(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Form.menu_reboot_server)
    await bot.edit_message_text(
        text='<b>[ Перезагрузить сервер ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_reboot_server
    )
