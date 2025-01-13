import os
import os.path

from aiogram import F, Router, types
from aiogram.types import FSInputFile

from Telegram.Call_Back_Data import CallBackData
from Telegram.loader import bot, router
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.keyboards.menu_files import get_qr_list_files_keyboard, get_config_list_files_keyboard
from config import PATH_QR


@router.callback_query(
    F.data.startswith(CallBackData.FILE_DOWNLOAD_)
)
async def download_qr_file(callback_query: types.callback_query):
    query = callback_query.data
    file_name = str(query).replace(CallBackData.FILE_DOWNLOAD_, '')
    path = os.path.join(PATH_QR, file_name)
    if os.path.exists(path):
        file = FSInputFile(path, file_name)
        await bot.send_document(chat_id=callback_query.from_user.id, document=file, reply_markup=k_menu_admin)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Файла не существует',
                               reply_markup=k_menu_admin())


@router.callback_query(F.data.in_({CallBackData.show_qr_files}))
async def show_qr_list_files(callback_query: types.callback_query):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text='Список QR code',
        reply_markup=get_qr_list_files_keyboard()
    )



@router.callback_query(F.data.in_({CallBackData.show_qr_files}))
async def show_config_list_files(callback_query: types.callback_query):
    await bot.send_message(
        chat_id=callback_query.from_user.id,
        text='Список Configs',
        reply_markup=get_config_list_files_keyboard()
    )
