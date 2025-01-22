from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.MyCallBackData import MyCallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

k_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=MyCallBackData.menu_create_user), ],
    [InlineKeyboardButton(text='🔖 Показать Configs', callback_data=MyCallBackData.show_config_files), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_main), ],

])

k_menu_user_config_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Cоздать', callback_data=MyCallBackData.create_user_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ],
])

k_menu_user_config_rename = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Все верно переименовать', callback_data=MyCallBackData.user_config_rename_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ],
])

k_back_to_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ]
])
