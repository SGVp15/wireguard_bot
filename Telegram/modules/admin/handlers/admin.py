from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID
from Telegram.loader import bot
from Telegram.modules.user.handlers.files import send_document
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.menus.admin import show_admin_menu
from config import WG_CONF, WG_DUMP, SYSTEM_LOG, VERSION, DEBUG
from wireguard.wireguard_class import WIREGUARD as wg

if DEBUG:
    print(f'import {__name__}')

router = Router(name=__name__)


@router.callback_query(
    F.data.in_({MyCallBackData.update_bot, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def update_bot(callback_query: CallbackQuery, state: FSMContext):
    wg.update_bot()


@router.callback_query(
    F.data.in_({MyCallBackData.show_version, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def show_version(callback_query: CallbackQuery, state: FSMContext):
    await bot.edit_message_text(
        text=f'<b>{VERSION}</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_admin
    )


@router.callback_query(
    F.data.in_({MyCallBackData.restart_service_wg_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def restart_service(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    wg.restart_service()
    await bot.send_message(text='restart service - ok', chat_id=callback_query.from_user.id, )
    await show_admin_menu(callback_query, state)


@router.callback_query(
    F.data.in_({MyCallBackData.reboot_server_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def restart_service(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    wg.reboot_server()
    await bot.send_message(
        text='restart service - ok',
        chat_id=callback_query.from_user.id
    )
    await show_admin_menu(callback_query, state)


@router.callback_query(
    F.data.in_({MyCallBackData.download_wg_conf, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_wg_conf(callback_query: CallbackQuery, state: FSMContext):
    file = WG_CONF
    filename = f'wg0.conf'
    await send_document(file, filename, callback_query.from_user.id)
    await show_admin_menu(callback_query, state)


@router.callback_query(
    # AdminState.admin_menu,
    F.data.in_({MyCallBackData.download_logs, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_logs(callback_query: CallbackQuery, state: FSMContext):
    file = SYSTEM_LOG
    filename = f'log.log'
    await send_document(file, filename, callback_query.from_user.id)
    await show_admin_menu(callback_query, state)


@router.callback_query(
    # AdminState.admin_menu,
    F.data.in_({MyCallBackData.clear_log, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def clear_log(callback_query: CallbackQuery, state: FSMContext):
    with open(SYSTEM_LOG, 'w') as f:
        f.write('')
    await bot.send_message(text='clear log - ok', chat_id=callback_query.from_user.id)
    await show_admin_menu(callback_query, state)


@router.callback_query(
    F.data.in_({MyCallBackData.download_wg_dump, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_wg_dump(callback_query: CallbackQuery, state: FSMContext):
    wg.get_dump()
    file = WG_DUMP
    filename = f'wg_dump.txt'
    await send_document(file, filename, callback_query.from_user.id)
    await show_admin_menu(callback_query, state)
