from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

users_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data='main_menu'), ],
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data='create_user_menu'), ],
])

user_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data='users_menu'), ],
    [InlineKeyboardButton(text='Все верно :) создать', callback_data='create_user'), ],
])

back_to_users_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data='users_menu'), ]
])

