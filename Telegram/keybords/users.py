from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

users_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.main_menu), ],
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=CallBackData.create_user_menu), ],
])

user_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.users_menu), ],
    [InlineKeyboardButton(text='Все верно :) создать', callback_data=CallBackData.create_user), ],
])

back_to_users_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.users_menu), ]
])
