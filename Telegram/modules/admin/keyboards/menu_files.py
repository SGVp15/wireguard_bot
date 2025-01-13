import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData
from config import PATH_CONFIG, PATH_QR


def get_config_list_files_keyboard() -> [InlineKeyboardButton]:
    out_buttons = []
    config_files = os.listdir(PATH_CONFIG)
    qrcodes = os.listdir(PATH_QR)
    for config_file in config_files:
        file = config_file.replace('.conf', '')
        if f'{file}.png' in qrcodes:
            out_buttons.append(
                [
                    InlineKeyboardButton(text=f'{file}', callback_data=f'{file}'),
                    InlineKeyboardButton(text=f'⏬ config',
                                         callback_data=f'{CallBackData.file_download_config_}{config_file}'),
                    InlineKeyboardButton(text=f'🔳 qrcode', callback_data=f'{CallBackData.file_download_qr_}{file}.png'),
                    # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
                ]
            )
        else:
            out_buttons.append(
                [
                    InlineKeyboardButton(text=f'{file}', callback_data=f'{file}'),
                    InlineKeyboardButton(text=f'⏬ config',
                                         callback_data=f'{CallBackData.file_download_config_}{config_file}'),
                    # InlineKeyboardButton(text=f'🔳 qrcode', callback_data=f'{CallBackData.file_download_qr_}{file}.png'),
                    # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
                ]
            )
    return InlineKeyboardMarkup(inline_keyboard=[*out_buttons])
