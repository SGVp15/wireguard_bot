from aiogram.fsm.state import State, StatesGroup

from config import DEBUG

if DEBUG:
    print(f'import {__name__}')


class AdminState(StatesGroup):
    admin_menu = State()
    menu_restart_service_wg = State()
    menu_reboot_server = State()
