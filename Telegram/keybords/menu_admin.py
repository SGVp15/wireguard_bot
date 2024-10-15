from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

k_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_main), ],
    [InlineKeyboardButton(text='🌟 Перезагрузить службу WG >>', callback_data=CallBackData.menu_restart_service_wg), ],
    [InlineKeyboardButton(text='💀 Перезагрузить сервер WG >>', callback_data=CallBackData.menu_reboot_server), ],
])

k_menu_restart_service = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_admin), ],
    [InlineKeyboardButton(text='Все верно перезагрузить службу WG', callback_data=CallBackData.restart_service_wg_ok), ],
])

k_menu_restart_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='<< Назад', callback_data=CallBackData.menu_admin), ],
    [InlineKeyboardButton(text='Все верно перезагрузить Server', callback_data=CallBackData.restart_server_ok), ],
])
