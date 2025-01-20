import os

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from Telegram.MyCallBackData import MyCallBackData
from config import PATH_CONFIG, DEBUG

if DEBUG:
    print(f'import {__name__}')


class DOWNLOAD_CONFIG_FILE(CallbackData, prefix='getConf'):
    name: str


class RENAME_CONFIG_FILE(CallbackData, prefix='ranameConf'):
    name: str


class MENU_CONF_LIST(CallbackData, prefix='Conf'):
    name: str


class DISABLE_CONFIG_FILE(CallbackData, prefix='disConf'):
    name: str


class DELETE_CONFIG_FILE(CallbackData, prefix='delConf'):
    name: str


def builder_config_list_files_keyboard() -> InlineKeyboardMarkup:
    config_files = sorted(os.listdir(PATH_CONFIG))
    builder = InlineKeyboardBuilder()
    builder.button(text='🔙 Назад', callback_data=MyCallBackData.menu_users)
    for config_file in config_files:
        builder.button(text=f'{config_file}', callback_data=MENU_CONF_LIST(name=config_file).pack())
    builder.button(text='🔙 Назад', callback_data=MyCallBackData.menu_users)
    builder.adjust(1)
    return builder.as_markup()


def builder_config_file_keyboard(config_file) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text='🔙 Назад', callback_data=MyCallBackData.menu_users)
    builder.button(text=f'⏬ Скачать', callback_data=DOWNLOAD_CONFIG_FILE(name=config_file).pack())
    builder.button(text=f'Переименовать', callback_data=RENAME_CONFIG_FILE(name=config_file).pack())
    builder.button(text=f'Удалить', callback_data=DELETE_CONFIG_FILE(name=config_file).pack())
    builder.button(text='🔙 Назад', callback_data=MyCallBackData.menu_users)
    builder.adjust(1)
    return builder.as_markup()
