import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData
from config import PATH_CONFIG, PATH_QR


def get_config_list_files_keyboard(path=PATH_CONFIG) -> [InlineKeyboardButton]:
    out_buttons = []
    configs = os.listdir(PATH_CONFIG)
    qrcodes = os.listdir(PATH_QR)
    for config_file in configs:
        file = config_file.replace('.conf', '')
        # if config_file.endswith('.conf')
        out_buttons.append(
            [
                InlineKeyboardButton(text=f'⏬ {config_file}',
                                     callback_data=f'{CallBackData.file_download_config_}{file}.conf'),
                InlineKeyboardButton(text=f'🔳 qr', callback_data=f'{CallBackData.file_download_qr_}{file}.png'),
                # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
            ]
        )
    return InlineKeyboardMarkup(inline_keyboard=[*out_buttons])


def get_qr_list_files_keyboard(path=PATH_QR) -> [InlineKeyboardButton]:
    out_buttons = []

    for qrcode_file in qrcodes:
        out_buttons.append(
            [
                InlineKeyboardButton(text=f'⏬ 🔳 {qrcode_file}',
                                     callback_data=f'{CallBackData.file_download_qr_}{qrcode_file}'),
                # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
            ]
        )
    return InlineKeyboardMarkup(inline_keyboard=[*out_buttons])
