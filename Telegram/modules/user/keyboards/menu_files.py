import os

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Telegram.Call_Back_Data import CALL_BACK_DATA
from config import PATH_CONFIG, DEBUG

if DEBUG:
    print(f'import {__name__}')

class DOWNLOAD_CONFIG_FILE(CallbackData, prefix='download_conf_file'):
    name: str


class DOWNLOAD_QR_FILE(CallbackData, prefix='download_qr_file'):
    name: str


class DELETE_CONFIG_FILE(CallbackData, prefix='delete_conf_file'):
    name: str


class DELETE_QR_FILE(CallbackData, prefix='delete_qr_file'):
    name: str


def builder_config_list_files_keyboard() -> InlineKeyboardMarkup:
    config_files = sorted(os.listdir(PATH_CONFIG))
    builder = InlineKeyboardBuilder()
    builder.button(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_users)
    for config_file in config_files:
        builder.button(text=f'⏬{config_file}', callback_data=DOWNLOAD_CONFIG_FILE(name=config_file).pack())
    builder.button(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_users)
    builder.adjust(1)
    return builder.as_markup()
