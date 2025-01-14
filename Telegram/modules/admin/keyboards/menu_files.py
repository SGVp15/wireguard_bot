import os

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import PATH_CONFIG


class DOWNLOAD_CONFIG_FILE(CallbackData, prefix='download_conf_file'):
    name: str


class DOWNLOAD_QR_FILE(CallbackData, prefix='download_qr_file'):
    name: str


class DELETE_CONFIG_FILE(CallbackData, prefix='delete_conf_file'):
    name: str


class DELETE_QR_FILE(CallbackData, prefix='delete_qr_file'):
    name: str


def builder_config_list_files_keyboard() -> InlineKeyboardMarkup:
    config_files = os.listdir(PATH_CONFIG)
    config_files = sorted(config_files)
    builder = InlineKeyboardBuilder()
    for config_file in config_files:
        builder.button(text=f'⏬{config_file}', callback_data=DOWNLOAD_CONFIG_FILE(name=config_file).pack())
    builder.adjust(1)
    return builder.as_markup()
