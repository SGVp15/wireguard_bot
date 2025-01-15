from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.MycallBackData import MycallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

k_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=MycallBackData.menu_create_user), ],
    [InlineKeyboardButton(text='🔖 Показать Configs', callback_data=MycallBackData.show_config_files), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MycallBackData.menu_main), ],

])

k_menu_user_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Cоздать', callback_data=MycallBackData.create_user_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MycallBackData.menu_users), ],

])

k_back_to_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MycallBackData.menu_users), ]
])
