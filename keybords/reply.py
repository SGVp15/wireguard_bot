from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


help = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False
                           ).add(KeyboardButton('/help'))
help.add(KeyboardButton('/id'))
