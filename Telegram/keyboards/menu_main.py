from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')


# download_logs = InlineKeyboardButton('Скачать Логи', callback_data='download_logs')

k_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🙂 Пользователи >>', callback_data=CallBackData.menu_users), ],
    [InlineKeyboardButton(text='⚙️ ADMIN >>', callback_data=CallBackData.menu_admin), ],
])


