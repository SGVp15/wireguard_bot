from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from Telegram.Call_Back_Data import CALL_BACK_DATA

button_menu_admin = InlineKeyboardButton(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_admin)

k_menu_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🌟 Перезагрузить службу wireguard',
                          callback_data=CALL_BACK_DATA.menu_restart_service_wg), ],
    [InlineKeyboardButton(text='💀 Перезагрузить сервер', callback_data=CALL_BACK_DATA.menu_reboot_server), ],
    [InlineKeyboardButton(text='📒 Скачать логи', callback_data=CALL_BACK_DATA.download_logs), ],
    [InlineKeyboardButton(text='📒 Скачать WG_CONF', callback_data=CALL_BACK_DATA.download_wg_conf), ],
    [InlineKeyboardButton(text='📒 Скачать WG_DUMP', callback_data=CALL_BACK_DATA.download_wg_dump), ],
    [InlineKeyboardButton(text='♻️ Обновить Bot', callback_data=CALL_BACK_DATA.update_bot), ],
    [InlineKeyboardButton(text='❌ Удалить логи', callback_data=CALL_BACK_DATA.clear_log), ],
    [InlineKeyboardButton(text='? Показать версию', callback_data=CALL_BACK_DATA.show_version), ],
    [InlineKeyboardButton(text='🔙 Назад', callback_data=CALL_BACK_DATA.menu_main), ]
])

k_menu_restart_service = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить службу wireguard!',
                          callback_data=CALL_BACK_DATA.restart_service_wg_ok), ],
    [button_menu_admin, ],

])

k_menu_reboot_server = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛑 Все верно перезагрузить Server!',
                          callback_data=CALL_BACK_DATA.reboot_server_ok), ],
    [button_menu_admin, ],

])
