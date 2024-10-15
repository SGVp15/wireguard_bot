from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

# download_logs = InlineKeyboardButton('Скачать Логи', callback_data='download_logs')

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🙂 Пользователи >>', callback_data=CallBackData.menu_users), ],
    [InlineKeyboardButton(text=' ADMIN >>', callback_data=CallBackData.menu_admin), ],
])


