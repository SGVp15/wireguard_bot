from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.MycallBackData import MycallBackData
from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

button_menu_admin = InlineKeyboardButton(text='🔙 Назад', callback_data=MycallBackData.menu_admin)

k_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Перезагрузить службу wireguard',
                          callback_data=MycallBackData.menu_restart_service_wg), ],
    [InlineKeyboardButton(text='💀 Перезагрузить сервер', callback_data=MycallBackData.menu_reboot_server), ],
    [InlineKeyboardButton(text='📒 Скачать логи', callback_data=MycallBackData.download_logs), ],
    [InlineKeyboardButton(text='📒 Скачать WG_CONF', callback_data=MycallBackData.download_wg_conf), ],
    [InlineKeyboardButton(text='📒 Скачать WG_DUMP', callback_data=MycallBackData.download_wg_dump), ],
    [InlineKeyboardButton(text='♻️ Обновить Bot', callback_data=MycallBackData.update_bot), ],
    [InlineKeyboardButton(text='❌ Удалить логи', callback_data=MycallBackData.clear_log), ],
    [InlineKeyboardButton(text='? Показать версию', callback_data=MycallBackData.show_version), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=MycallBackData.menu_main), ]
])

k_menu_restart_service = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить службу wireguard!',
                          callback_data=MycallBackData.restart_service_wg_ok), ],
    [button_menu_admin, ],

])

k_menu_reboot_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить Server!',
                          callback_data=MycallBackData.reboot_server_ok), ],
    [button_menu_admin, ],

])
