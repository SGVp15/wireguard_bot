import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID
from Telegram.modules.user.handlers.files import my_send_document
from Telegram.keyboards.menu_main import k_main_menu
from Telegram.loader import bot
from Telegram.modules.user.states.mashine_state import UserState
from config import DEBUG
from utils.log import log
from wireguard.wireguard_class import WIREGUARD as wg

if DEBUG:
    print(f'import {__name__}')

router = Router()


@router.callback_query(UserState.create_user,
                       F.data.in_({MyCallBackData.create_user_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, })
                       )
async def create_user(callback_query: CallbackQuery, state: FSMContext):
    print('create_user')
    data = await state.get_data()
    user = data.get('name')
    print(f'{user}')
    config_string, full_path_conf_file, full_path_qr_file = wg.create_user(user)
    log.info('create_user {user}')
    await state.clear()

    await my_send_document(chat_id=callback_query.from_user.id, filename=os.path.basename(full_path_conf_file),
                           full_path=full_path_conf_file)
    await my_send_document(chat_id=callback_query.from_user.id, filename=os.path.basename(full_path_qr_file),
                           full_path=full_path_qr_file)
