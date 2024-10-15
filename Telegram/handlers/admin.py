from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from config import SYSTEM_LOG
from wireguard.wg import WIREGUARD as wg
from ..Call_Back_Data import CallBackData
from ..config import ADMIN_ID
from ..keybords.inline import main_menu
from ..keybords.menu_admin import k_menu_admin
from ..main import dp, bot
from ..menus.admin import admin_menu
from ..states.Form import Form


@dp.callback_query(Form.menu_restart_service_wg,
                   F.data.in_({CallBackData.restart_service_wg_ok, })
                   & F.from_user.id.in_({*ADMIN_ID, })
                   )
async def restart_service(callback_query: types.callback_query, state: FSMContext):
    await state.clear()
    wg.restart_service()
    await bot.send_message(
        text='restart service - ok',
        chat_id=callback_query.from_user.id,
        reply_markup=main_menu
    )


@dp.callback_query(Form.menu_restart_service_wg,
                   F.data.in_({CallBackData.reboot_server_ok, })
                   & F.from_user.id.in_({*ADMIN_ID, })
                   )
async def restart_service(callback_query: types.callback_query, state: FSMContext):
    await state.clear()
    wg.reboot_server()
    await bot.send_message(
        text='restart service - ok',
        chat_id=callback_query.from_user.id,
        reply_markup=main_menu
    )


@dp.callback_query(Form.admin_menu,
                   F.data.in_({CallBackData.download_logs, })
                   & F.from_user.id.in_({*ADMIN_ID, })
                   )
async def download_logs(callback_query: types.callback_query, state: FSMContext):
    file = FSInputFile(SYSTEM_LOG, filename=f'log.txt')
    await bot.send_document(
        chat_id=callback_query.from_user.id,
        document=file, reply_markup=k_menu_admin
    )
