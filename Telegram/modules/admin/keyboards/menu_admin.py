from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

button_menu_admin = InlineKeyboardButton(text='🔙 Назад', callback_data=CallBackData.menu_admin)

k_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Перезагрузить службу VPN',
                          callback_data=CallBackData.menu_service_vpn_restart), ],
    [InlineKeyboardButton(text='💀 Перезагрузить сервер', callback_data=CallBackData.menu_server_reboot), ],
    [InlineKeyboardButton(text='📒 Скачать логи', callback_data=CallBackData.download_logs), ],
    # [InlineKeyboardButton(text='📒 Скачать WG_CONF', callback_data=MyCallBackData.download_wg_conf), ],
    # [InlineKeyboardButton(text='📒 Скачать WG_DUMP', callback_data=MyCallBackData.download_wg_dump), ],
    # [InlineKeyboardButton(text='🌟 Пересоздать WG_CONF', callback_data=MyCallBackData.wg_create_main_config), ],
    [InlineKeyboardButton(text='♻️ Обновить Bot', callback_data=CallBackData.update_bot), ],
    [InlineKeyboardButton(text='❌ Удалить логи', callback_data=CallBackData.clear_log), ],
    [InlineKeyboardButton(text='? Показать версию', callback_data=CallBackData.show_version), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CallBackData.menu_main), ]
])

k_menu_restart_service = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить службу!',
                          callback_data=CallBackData.service_vpn_restart_ok), ],
    [button_menu_admin, ],

])

k_menu_reboot_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить Server!',
                          callback_data=CallBackData.server_reboot_ok), ],
    [button_menu_admin, ],
])

