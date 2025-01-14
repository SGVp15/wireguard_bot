import os
import os.path
import re

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.Call_Back_Data import CALL_BACK_DATA
from Telegram.loader import bot
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.keyboards.menu_files import builder_config_list_files_keyboard, DOWNLOAD_CONFIG_FILE
from config import PATH_QR, PATH_CONFIG

router = Router(name=__name__)


@router.callback_query(
    F.data.in_({CALL_BACK_DATA.show_config_files, })
    # & F.from_user.id.in_({*ADMIN_ID, })
)
async def show_config_list_files(callback_query: CallbackQuery):
    await bot.edit_message_text(
        text='Список Config files',
        parse_mode=ParseMode.HTML,
        chat_id=callback_query.from_user.id,
        message_id=callback_query.message.message_id,
        reply_markup=builder_config_list_files_keyboard()
    )


@router.callback_query(DOWNLOAD_CONFIG_FILE.filter())
async def download_config_file(callback_query: CallbackQuery,
                               callback_data: DOWNLOAD_CONFIG_FILE):
    await bot.send_message(chat_id=callback_query.from_user.id, text=f'{callback_data.name}',
                           reply_markup=k_menu_admin)
    conf_name = callback_data.name
    qr_name = re.sub(r'\.conf$', '.png', conf_name)
    path_conf_file = os.path.join(PATH_CONFIG, conf_name)
    path_qr_file = os.path.join(PATH_QR, qr_name)

    if os.path.exists(path_conf_file):
        file = FSInputFile(path_conf_file, conf_name)
        await bot.send_document(chat_id=callback_query.from_user.id, document=file)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text=f'[ {conf_name} ] Файла не существует')

    if os.path.exists(path_qr_file):
        file = FSInputFile(path_qr_file, qr_name)
        await bot.send_document(chat_id=callback_query.from_user.id, document=file)
    else:
        await bot.send_message(chat_id=callback_query.from_user.id, text=f'[ {qr_name} ] Файла не существует')
    await bot.send_message(chat_id=callback_query.from_user.id, text='[ ADMIN ] ',
                           reply_markup=k_menu_admin)
