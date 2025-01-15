import os
import os.path
import re

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.Call_Back_Data import CALL_BACK_DATA
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.loader import bot
from Telegram.modules.user.keyboards.menu_files import builder_config_list_files_keyboard, DOWNLOAD_CONFIG_FILE
from config import PATH_QR, PATH_CONFIG, DEBUG

if DEBUG:
    print(f'import {__name__}')

router = Router(name=__name__)


@router.callback_query(
    F.data.in_({CALL_BACK_DATA.show_config_files, })
    & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
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
                               callback_data: DOWNLOAD_CONFIG_FILE,
                               state: FSMContext):
    conf_name = callback_data.name
    qr_name = re.sub(r'\.conf$', '.png', conf_name)
    path_conf_file = os.path.join(PATH_CONFIG, conf_name)
    path_qr_file = os.path.join(PATH_QR, qr_name)

    await send_document(chat_id=callback_query.from_user.id, filename=conf_name, file=path_conf_file)
    await send_document(chat_id=callback_query.from_user.id, filename=qr_name, file=path_qr_file)


async def send_document(file, filename, chat_id):
    if os.path.exists(file):
        file = FSInputFile(file, filename=filename)
        await bot.send_document(
            chat_id=chat_id,
            document=file
        )
    else:
        await bot.send_message(
            text=f'File not found {file}',
            chat_id=chat_id,
        )
