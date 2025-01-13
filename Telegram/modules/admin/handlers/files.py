import os
import os.path

from aiogram import F, types, Router
from aiogram.types import FSInputFile

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.loader import bot
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.keyboards.menu_files import get_qr_list_files_keyboard, get_config_list_files_keyboard
from config import PATH_QR

router = Router(name=__name__)


@router.callback_query(
    F.data.startswith(CallBackData.file_download_)
    & F.from_user.id.in_({*ADMIN_ID, })
)
async def download_qr_file(callback_query: types.callback_query):
    query = callback_query.data
    file_name = str(query).replace(CallBackData.file_download_, '')
    path = os.path.join(PATH_QR, file_name)
    if os.path.exists(path):
        file = FSInputFile(path, file_name)
        await bot.send_document(chat_id=callback_query.from_user.id, document=file, reply_markup=k_menu_admin)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text='Файла не существует',
                               reply_markup=k_menu_admin())

