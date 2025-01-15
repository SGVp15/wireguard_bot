from aiogram.fsm.state import State, StatesGroup

from config import DEBUG

if DEBUG:
    print(f'import {__name__}')



class Form(StatesGroup):
    main_menu = State()
    users_menu = State()

    create_user_menu = State()
    name = State()

    create_user = State()

    admin_menu = State()
    menu_restart_service_wg = State()
    menu_reboot_server = State()
