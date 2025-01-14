import os

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import PATH_CONFIG, PATH_QR


class DOWNLOAD_CONFIG_FILE(CallbackData, prefix='download_conf_file'):
    name:str


class DOWNLOAD_QR_FILE(CallbackData, prefix='download_qr_file'):
    name: str


class DELETE_CONFIG_FILE(CallbackData, prefix='delete_conf_file'):
    path: str
    name: str


class DELETE_QR_FILE(CallbackData, prefix='delete_qr_file'):
    path: str
    name: str


def builder_config_list_files_keyboard() -> InlineKeyboardMarkup:
    out_buttons = []
    config_files = os.listdir(PATH_CONFIG)
    config_files = sorted(config_files)
    qrcodes = os.listdir(PATH_QR)

    builder = InlineKeyboardBuilder()
    for config_file in config_files:
        # file = config_file.replace('.conf', '')
        # if f'{file}.png' in qrcodes:
        builder.button(text='',
                       callback_data=DOWNLOAD_CONFIG_FILE(name=config_file).pack())
    #         out_buttons.append(
    #             [
    #                 InlineKeyboardButton(text=f'{file}',
    #                                      callback_data=f'{CallBackData.file_download_config_}{config_file}'),
    #                 InlineKeyboardButton(text=f'⏬ config',
    #                                      callback_data=f'{CallBackData.file_download_config_}{config_file}'),
    #                 InlineKeyboardButton(text=f'🔳 qrcode', callback_data=f'{CallBackData.file_download_qr_}{file}.png'),
    #                 # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
    #             ]
    #         )
    #     else:
    #         out_buttons.append(
    #             [
    #                 InlineKeyboardButton(text=f'{file}',
    #                                      callback_data=f'{CallBackData.file_download_config_}{config_file}'),
    #                 InlineKeyboardButton(text=f'⏬ config',
    #                                      callback_data=f'{CallBackData.file_download_config_}{config_file}'),
    #                 # InlineKeyboardButton(text=f'🔳 qrcode', callback_data=f'{CallBackData.file_download_qr_}{file}.png'),
    #                 # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
    #             ]
    #         )
    # out_buttons.append([InlineKeyboardButton(text='🔙 Назад', callback_data=CallBackData.menu_admin)])
    builder.adjust(1)
    return builder.as_markup()
