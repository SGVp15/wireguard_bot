from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    users_menu = State()

    create_user_menu = State()
    name = State()

    create_user = State()
