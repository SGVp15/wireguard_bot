from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

users_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_main), ],
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=CallBackData.menu_create_user), ],
])

user_create_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_users), ],
    [InlineKeyboardButton(text='Все верно :) создать', callback_data=CallBackData.create_user_ok), ],
])

back_to_users_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_users), ]
])
