from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CALL_BACK_DATA

# download_logs = InlineKeyboardButton('Скачать Логи', callback_data='download_logs')

k_main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🙂 Пользователи >>', callback_data=CALL_BACK_DATA.menu_users), ],
    [InlineKeyboardButton(text='⚙️ ADMIN >>', callback_data=CALL_BACK_DATA.menu_admin), ],
])


