from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID
from Telegram.loader import bot
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.menus.admin import show_admin_menu
from Telegram.modules.user.handlers.files import my_send_document
from config import WG_CONF, WG_DUMP, SYSTEM_LOG, VERSION, DEBUG
from wireguard.wireguard_class import WIREGUARD as wg, WIREGUARD

if DEBUG:
    print(f'import {__name__}')

router = Router(name=__name__)


@router.callback_query(
    F.data.in_({MyCallBackData.update_bot, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def update_bot(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    wg.update_bot()


@router.callback_query(
    F.data.in_({MyCallBackData.show_version, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def show_version(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer()
    await bot.edit_message_text(
        text=f'<b>{VERSION}</b>',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=k_menu_admin,
    )


@router.callback_query(
    F.data.in_({MyCallBackData.service_wg_restart_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def restart_service(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.answer()
    await bot.send_message(text='restart service - ok', chat_id=callback_query.from_user.id, )
    await show_admin_menu(callback_query, state)
    wg.restart_service()


@router.callback_query(
    F.data.in_({MyCallBackData.server_reboot_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def restart_service(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.answer()
    await bot.send_message(
        text='restart service - ok',
        chat_id=callback_query.from_user.id,
        parse_mode=ParseMode.HTML,
    )
    await show_admin_menu(callback_query, state)
    wg.reboot_server()


@router.callback_query(
    F.data.in_({MyCallBackData.wg_create_main_config, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def wg_create_main_config(callback_query: CallbackQuery, state: FSMContext):
    WIREGUARD.create_wg_conf()
    await callback_query.message.edit_text(
        text='Create wg0.conf - ok',
        reply_markup=k_menu_admin,
        parse_mode=ParseMode.HTML,
    )
    await show_admin_menu(callback_query, state)


@router.callback_query(
    F.data.in_({MyCallBackData.download_wg_conf, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_wg_conf(callback_query: CallbackQuery, state: FSMContext):
    file = WG_CONF
    await callback_query.answer()
    await my_send_document(chat_id=callback_query.from_user.id, full_path=file)
    await show_admin_menu(callback_query, state)


@router.callback_query(
    # AdminState.admin_menu,
    F.data.in_({MyCallBackData.download_logs, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_logs(callback_query: CallbackQuery, state: FSMContext):
    file = SYSTEM_LOG
    await callback_query.answer()
    await my_send_document(chat_id=callback_query.from_user.id, full_path=file)
    await show_admin_menu(callback_query, state)


@router.callback_query(
    F.data.in_({MyCallBackData.clear_log, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def clear_log(callback_query: CallbackQuery, state: FSMContext):
    with open(SYSTEM_LOG, 'w') as f:
        f.write('')
    await callback_query.message.edit_text(text='clear log - ok')
    await show_admin_menu(callback_query, state)


@router.callback_query(
    F.data.in_({MyCallBackData.download_wg_dump, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_wg_dump(callback_query: CallbackQuery, state: FSMContext):
    wg.get_dump()
    file = WG_DUMP
    await my_send_document(chat_id=callback_query.from_user.id, full_path=file)
    await show_admin_menu(callback_query, state)
