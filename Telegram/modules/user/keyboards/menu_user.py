from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

k_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_main), ],
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=CallBackData.menu_create_user), ],
])

k_menu_user_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_users), ],
    [InlineKeyboardButton(text='Все верно :) создать', callback_data=CallBackData.create_user_ok), ],
])

k_back_to_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_users), ]
])
