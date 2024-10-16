from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData

k_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Перезагрузить службу wireguard',
                          callback_data=CallBackData.menu_restart_service_wg), ],
    [InlineKeyboardButton(text='💀 Перезагрузить сервер', callback_data=CallBackData.menu_reboot_server), ],
    [InlineKeyboardButton(text='📒 Скачать логи', callback_data=CallBackData.download_logs), ],
    [InlineKeyboardButton(text='📒 Скачать WG_CONF', callback_data=CallBackData.download_wg_conf), ],
    [InlineKeyboardButton(text='📒 Скачать WG_DUMP', callback_data=CallBackData.download_wg_dump), ],
    [InlineKeyboardButton(text='🛠 Обновить Bot', callback_data=CallBackData.update_bot), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CallBackData.menu_main), ]
])

k_menu_restart_service = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить службу wireguard!',
                          callback_data=CallBackData.restart_service_wg_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CallBackData.menu_admin), ],

])

k_menu_reboot_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить Server!',
                          callback_data=CallBackData.reboot_server_ok), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CallBackData.menu_admin), ],

])

