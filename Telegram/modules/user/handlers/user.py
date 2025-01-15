import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery

import Telegram.modules.user.handlers.files
from Telegram.Call_Back_Data import CALL_BACK_DATA
from Telegram.config import ADMIN_ID
from Telegram.loader import bot
from Telegram.keyboards.menu_main import k_main_menu
from Telegram.modules.user.states.mashine_state import UserState
from config import DEBUG
from utils.log import log
from wireguard.wireguard_class import WIREGUARD as wg

if DEBUG:
    print(f'import {__name__}')

router = Router()


@router.callback_query(UserState.create_user,
                       F.data.in_({CALL_BACK_DATA.create_user_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, })
                       )
async def create_user(callback_query: CallbackQuery, state: FSMContext):
    print('create_user')
    data = await state.get_data()
    user = data.get('name')
    print(f'{user}')
    text, config_file, qr_code_file = wg.create_user(user)
    log.info('create_user {user}')
    await state.clear()

    file = FSInputFile(config_file, filename=os.path.basename(config_file))
    await bot.send_message(
        text=f'Config file code {user}',
        chat_id=callback_query.from_user.id,
    )
    await Telegram.modules.user.handlers.files.send_document(
        chat_id=callback_query.from_user.id,
        document=file, reply_markup=k_main_menu
    )

    file = FSInputFile(qr_code_file, filename=os.path.basename(qr_code_file))
    await bot.send_message(
        text=f'QR code {user}',
        chat_id=callback_query.from_user.id,
    )
    await Telegram.modules.user.handlers.files.send_document(
        chat_id=callback_query.from_user.id,
        document=file, reply_markup=k_main_menu
    )
