from aiogram.fsm.state import State, StatesGroup

from config import DEBUG

if DEBUG:
    print(f'import {__name__}')

class UserState(StatesGroup):
    users_menu = State()

    create_user_menu = State()
    name = State()
    create_user = State()
    rename_user = State()
