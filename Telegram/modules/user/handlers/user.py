import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.modules.user.handlers.files import my_send_document
from Telegram.modules.user.keyboards.menu_files import DELETE_CONFIG_FILE
from Telegram.modules.user.keyboards.menu_user import k_back_to_menu_users
from Telegram.modules.user.states.mashine_state import UserState
from config import DEBUG
from utils.log import log
from wireguard.user_config import UserConfig
from wireguard.wireguard_class import WIREGUARD as wg, WIREGUARD

if DEBUG:
    print(f'import {__name__}')

router = Router()


@router.callback_query(UserState.create_user,
                       F.data.in_({MyCallBackData.create_user_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
                       )
async def create_user_config(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user = data.get('name')
    config_string, full_path_conf_file, full_path_qr_file = wg.create_user(user)
    log.info('create_user {user}')
    await state.clear()

    await my_send_document(chat_id=callback_query.from_user.id, filename=os.path.basename(full_path_conf_file),
                           full_path=full_path_conf_file)
    await my_send_document(chat_id=callback_query.from_user.id, filename=os.path.basename(full_path_qr_file),
                           full_path=full_path_qr_file)


@router.callback_query(UserState.rename_user,
                       F.data.in_({MyCallBackData.user_config_rename_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
                       )
async def rename_user_config(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_config = UserConfig(data.get('name'))
    user_config.rename_conf('new_name')
    log.info('create_user {user}')
    await state.clear()


@router.callback_query(DELETE_CONFIG_FILE.filter())
async def delete_user_config(callback_query: CallbackQuery,
                             callback_data: DELETE_CONFIG_FILE, ):
    name = callback_data.name
    u = UserConfig(name)
    u.delete_conf()
    await callback_query.message.edit_text(
        text=f'Delete: {name} - ok',
        reply_markup=k_back_to_menu_users
    )
