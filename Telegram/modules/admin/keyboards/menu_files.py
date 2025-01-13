import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData
from config import PATH_CONFIG, PATH_QR


def get_config_list_files_keyboard(path=PATH_CONFIG) -> [InlineKeyboardButton]:
    out_buttons = []
    files = os.listdir(path)
    for file in files:
        out_buttons.append(
            [
                InlineKeyboardButton(text=f'⏬ {file}', callback_data=f'{CallBackData.file_download_}{file}'),
                # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
            ]
        )
    return InlineKeyboardMarkup(inline_keyboard=[*out_buttons])


def get_qr_list_files_keyboard(path=PATH_QR) -> [InlineKeyboardButton]:
    out_buttons = []
    files = os.listdir(path)
    for file in files:
        out_buttons.append(
            [
                InlineKeyboardButton(text=f'⏬ {file}', callback_data=f'{CallBackData.file_download_}{file}'),
                # InlineKeyboardButton(text=f'🗑 {file}', callback_data=f'{CallBackData.FILE_DELETE_}{file}'),
            ]
        )
    return InlineKeyboardMarkup(inline_keyboard=[*out_buttons])
