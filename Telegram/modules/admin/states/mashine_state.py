from aiogram.fsm.state import State, StatesGroup


class AdminState(StatesGroup):
    admin_menu = State()
    menu_restart_service_wg = State()
    menu_reboot_server = State()
