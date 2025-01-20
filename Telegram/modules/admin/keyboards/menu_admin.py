from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.MyCallBackData import MyCallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

button_menu_admin = InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_admin)

k_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Перезагрузить службу wireguard',
                          callback_data=MyCallBackData.menu_restart_service_wg), ],
    [InlineKeyboardButton(text='💀 Перезагрузить сервер', callback_data=MyCallBackData.menu_reboot_server), ],
    [InlineKeyboardButton(text='📒 Скачать логи', callback_data=MyCallBackData.download_logs), ],
    [InlineKeyboardButton(text='📒 Скачать WG_CONF', callback_data=MyCallBackData.download_wg_conf), ],
    [InlineKeyboardButton(text='📒 Скачать WG_DUMP', callback_data=MyCallBackData.download_wg_dump), ],
    [InlineKeyboardButton(text='Пересоздать WG_CONF', callback_data=MyCallBackData.wg_create_main_config), ],
    [InlineKeyboardButton(text='♻️ Обновить Bot', callback_data=MyCallBackData.update_bot), ],
    [InlineKeyboardButton(text='❌ Удалить логи', callback_data=MyCallBackData.clear_log), ],
    [InlineKeyboardButton(text='? Показать версию', callback_data=MyCallBackData.show_version), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MyCallBackData.menu_main), ]
])

k_menu_restart_service = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить службу wireguard!',
                          callback_data=MyCallBackData.restart_service_wg_ok), ],
    [button_menu_admin, ],

])

k_menu_reboot_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить Server!',
                          callback_data=MyCallBackData.reboot_server_ok), ],
    [button_menu_admin, ],

])
