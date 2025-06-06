from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.MyCallBackData import MyCallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

k_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=MyCallBackData.menu_config_user_create), ],
    [InlineKeyboardButton(text='🔖 Показать Configs', callback_data=MyCallBackData.show_config_files), ],
    [InlineKeyboardButton(text='🗑 Показать Удаленные Configs', callback_data=MyCallBackData.show_config_delete_files), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_main), ],

])

k_menu_user_config_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 OK - создать', callback_data=MyCallBackData.config_user_create_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ],
])

k_menu_user_config_rename = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='⌨️ OK - переименовать', callback_data=MyCallBackData.config_user_rename_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ],
])

k_menu_user_config_delete = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🗑 OK - Удалить', callback_data=MyCallBackData.config_user_delete_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ],
])

k_back_to_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_users), ]
])
