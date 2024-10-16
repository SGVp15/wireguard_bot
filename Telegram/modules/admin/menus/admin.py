from aiogram import F, types
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin, k_menu_restart_service, k_menu_reboot_server
from Telegram.main import dp, bot
from Telegram.states.Form import Form


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
    (F.data == CallBackData.menu_restart_service_wg)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def menu_restart_service_wg(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.menu_restart_service_wg)
    await bot.edit_message_text(
        text='<b>[ Перезагрузить службу wireguard ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_restart_service
    )


@dp.callback_query(
    (F.data == CallBackData.menu_reboot_server)
    & (F.from_user.id.in_({*ADMIN_ID}))
)
async def menu_reboot_server(callback_query: types.callback_query, state: FSMContext):
    await state.set_state(Form.menu_reboot_server)
    await bot.edit_message_text(
        text='<b>[ Перезагрузить сервер ]</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_reboot_server
    )
