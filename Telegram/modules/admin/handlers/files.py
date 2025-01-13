import os
import os.path

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.loader import bot
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.keyboards.menu_files import get_config_list_files_keyboard
from config import PATH_QR, PATH_CONFIG

router = Router(name=__name__)


@router.callback_query(
    F.data.in_({CallBackData.show_config_files, })
    # & F.from_user.id.in_({*ADMIN_ID, })
)
async def show_config_list_files(callback_query: CallbackQuery):
    await bot.edit_message_text(
        text='Список Config files',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=get_config_list_files_keyboard()
    )


@router.callback_query(
    F.data.startswith(CallBackData.file_download_config_)
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_config_file(callback_query: CallbackQuery):
    query = callback_query.data
    file_name = str(query).replace(CallBackData.file_download_config_, '')
    path = os.path.join(PATH_CONFIG, file_name)
    if os.path.exists(path):
        file = FSInputFile(path, file_name)
        await bot.send_document(chat_id=callback_query.from_user.id, document=file)
        await bot.send_message(chat_id=callback_query.from_user.id, text='[ ADMIN ] ',
                               reply_markup=k_menu_admin)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Файла не существует',
                               reply_markup=k_menu_admin)
        print(path)


@router.callback_query(
    F.data.startswith(CallBackData.file_download_qr_)
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_qr_file(callback_query: CallbackQuery):
    query = callback_query.data
    file_name = str(query).replace(CallBackData.file_download_qr_, '')
    path = os.path.join(PATH_QR, file_name)
    if os.path.exists(path):
        file = FSInputFile(path, file_name)
        await bot.send_document(chat_id=callback_query.from_user.id, document=file)
        await bot.send_message(chat_id=callback_query.from_user.id, text='[ ADMIN ] ',
                               reply_markup=k_menu_admin)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Файла не существует',
                               reply_markup=k_menu_admin)
        print(path)
