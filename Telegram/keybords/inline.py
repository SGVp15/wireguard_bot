from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# download_logs = InlineKeyboardButton('Скачать Логи', callback_data='download_logs')

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🙂 Пользователи >>', callback_data='users_menu'), ],
    [InlineKeyboardButton(text=' ADMIN >>', callback_data='admin_menu'), ],
])


