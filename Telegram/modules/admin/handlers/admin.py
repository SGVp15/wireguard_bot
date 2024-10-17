import os.path

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.keyboards.menu_main import k_main_menu
from Telegram.loader import bot
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from config import WG_CONF, WG_DUMP, SYSTEM_LOG, VERSION
from wireguard.wireguard_class import WIREGUARD as wg

router = Router()


@router.callback_query(
    F.data.in_({CallBackData.update_bot, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def update_bot(callback_query: CallbackQuery, state: FSMContext):
    wg.update_bot()


@router.callback_query(
    F.data.in_({CallBackData.show_version, })
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
    F.data.in_({CallBackData.restart_service_wg_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def restart_service(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    wg.restart_service()
    await bot.send_message(
        text='restart service - ok',
        chat_id=callback_query.from_user.id,
        reply_markup=k_main_menu
    )


@router.callback_query(
    F.data.in_({CallBackData.reboot_server_ok, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def restart_service(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    wg.reboot_server()
    await bot.send_message(
        text='restart service - ok',
        chat_id=callback_query.from_user.id,
        reply_markup=k_main_menu
    )


@router.callback_query(
    F.data.in_({CallBackData.download_wg_conf, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_wg_conf(callback_query: CallbackQuery, state: FSMContext):
    file = WG_CONF
    filename = f'wg0.conf'
    await send_document(file, filename, callback_query.from_user.id)


@router.callback_query(
    # AdminState.admin_menu,
    F.data.in_({CallBackData.download_logs, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_logs(callback_query: CallbackQuery, state: FSMContext):
    file = SYSTEM_LOG
    filename = f'log.log'
    print(state)
    await send_document(file, filename, callback_query.from_user.id)


@router.callback_query(
    # AdminState.admin_menu,
    F.data.in_({CallBackData.clear_log, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def clear_log(callback_query: CallbackQuery, state: FSMContext):
    with open(SYSTEM_LOG, 'w') as f:
        f.write('')


@router.callback_query(
    F.data.in_({CallBackData.download_wg_dump, })
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_wg_dump(callback_query: CallbackQuery, state: FSMContext):
    wg.get_dump()
    file = WG_DUMP
    filename = f'wg_dump.txt'
    await send_document(file, filename, callback_query.from_user.id)


async def send_document(file, filename, chat_id):
    if os.path.exists(file):
        file = FSInputFile(file, filename=filename)
        await bot.send_document(
            chat_id=chat_id,
            document=file, reply_markup=k_menu_admin
        )
    else:
        await bot.send_message(
            text=f'File not found {file}',
            chat_id=chat_id,
        )
