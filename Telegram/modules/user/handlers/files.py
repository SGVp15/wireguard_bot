import os
import os.path

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.loader import bot
from Telegram.modules.user.keyboards.menu_files import builder_config_list_files_keyboard, DOWNLOAD_CONFIG_FILE, \
    MENU_CONF_LIST, builder_config_file_keyboard
from config import DEBUG
from wireguard.user_config import UserConfig

if DEBUG:
    print(f'import {__name__}')

router = Router(name=__name__)


@router.callback_query(
    F.data.in_({MyCallBackData.show_config_files, })
    & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
)
async def show_config_list_files(callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text='Список Config files',
        reply_markup=builder_config_list_files_keyboard()
    )


@router.callback_query(MENU_CONF_LIST.filter())
async def show_config_menu(callback_query: CallbackQuery,
                           callback_data: MENU_CONF_LIST, ):
    name = callback_data.name
    await callback_query.message.edit_text(
        text=f'Conf: <b>{name}</b>',
        reply_markup=builder_config_file_keyboard(name)
    )


@router.callback_query(DOWNLOAD_CONFIG_FILE.filter())
async def download_config_file(callback_query: CallbackQuery,
                               callback_data: DOWNLOAD_CONFIG_FILE,
                               state: FSMContext):
    user_config = UserConfig(callback_data.name)

    await my_send_document(chat_id=callback_query.from_user.id,
                           full_path=user_config.path_config_file)

    await my_send_document(chat_id=callback_query.from_user.id,
                           full_path=user_config.path_qr_file)


async def my_send_document(chat_id: str | int, full_path: str, filename: str = None) -> None:
    if filename is None:
        filename = os.path.basename(full_path)
    if os.path.exists(full_path):
        full_path = FSInputFile(full_path, filename=filename)
        await bot.send_document(
            chat_id=chat_id,
            document=full_path
        )
    else:
        await bot.send_message(
            text=f'File not found {full_path}',
            chat_id=chat_id,
        )
