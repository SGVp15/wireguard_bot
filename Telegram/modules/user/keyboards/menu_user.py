from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CALL_BACK_DATA

k_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Создать пользователя >>', callback_data=CALL_BACK_DATA.menu_create_user), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_main), ],

])

k_menu_user_create = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='✅ Cоздать', callback_data=CALL_BACK_DATA.create_user_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_users), ],

])

k_back_to_menu_users = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_users), ]
])
