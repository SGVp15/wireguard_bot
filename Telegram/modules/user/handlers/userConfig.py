import os

from aiogram import F, Router
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from Telegram.MyCallBackData import MyCallBackData
from Telegram.config import ADMIN_ID, USERS_ID
from Telegram.modules.user.handlers.files import my_send_document
from Telegram.modules.user.keyboards.menu_files import RETURN_CONFIG_FILE
from Telegram.modules.user.keyboards.menu_userConfig import k_back_to_menu_users
from Telegram.modules.user.states.mashine_state import UserState
from config import DEBUG
from utils.log import log
from wireguard.user_config import UserConfig
from wireguard.wireguard_class import WIREGUARD as wg

if DEBUG:
    print(f'import {__name__}')

router = Router()


@router.callback_query(UserState.create_user,
                       F.data.in_({MyCallBackData.config_user_create_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
                       )
async def create_user_config(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    name = data.get('name')
    config_string, full_path_conf_file, full_path_qr_file = wg.create_user(name)
    log.info('create_user {user}')
    await state.clear()

    await my_send_document(chat_id=callback_query.from_user.id, filename=os.path.basename(full_path_conf_file),
                           full_path=full_path_conf_file)
    await my_send_document(chat_id=callback_query.from_user.id, filename=os.path.basename(full_path_qr_file),
                           full_path=full_path_qr_file)


@router.callback_query(UserState.rename_user,
                       F.data.in_({MyCallBackData.config_user_rename_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
                       )
async def rename_user_config(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_config: UserConfig = data.get('user_config')
    if user_config.rename_conf(user_config.new_name):
        log.info('rename_user {user} -> {new_name}')
        await callback_query.message.edit_text(
            text=f'Rename: <b>{user_config.name}</b> -> <b>{user_config.new_name}</b> ok',
            reply_markup=k_back_to_menu_users,
            parse_mode=ParseMode.HTML,

        )
    else:
        if DEBUG: print(__name__, ' else')
        await callback_query.message.edit_text(
            text=f'Такое имя уже существует {user_config.new_name}',
            reply_markup=k_back_to_menu_users,
            parse_mode=ParseMode.HTML,

        )
    await state.clear()


@router.callback_query(UserState.delete_user,
                       F.data.in_({MyCallBackData.config_user_delete_ok, })
                       & F.from_user.id.in_({*ADMIN_ID, *USERS_ID})
                       )
async def delete_user_config_ok(callback_query: CallbackQuery,
                                state: FSMContext):
    data = await state.get_data()
    user_config: UserConfig = data.get('user_config')
    user_config.delete_conf()
    await callback_query.message.edit_text(
        text=f'Delete: <b>{user_config.name}</b> - ok',
        reply_markup=k_back_to_menu_users,
        parse_mode=ParseMode.HTML,
    )
    await state.clear()


@router.callback_query(RETURN_CONFIG_FILE.filter())
async def return_config_file(callback_query: CallbackQuery,
                             callback_data: RETURN_CONFIG_FILE,
                             state: FSMContext):
    user_config = UserConfig(callback_data.name)
    if user_config.return_conf():
        log.info('rename_user {user} -> {new_name}')
        await callback_query.message.edit_text(
            text=f'Восстановлен: <b>{user_config.name}</b>',
            reply_markup=k_back_to_menu_users,
            parse_mode=ParseMode.HTML,
        )
    else:
        if DEBUG: print(__name__, ' else')
        await callback_query.message.edit_text(
            text=f'Возникли проблемы с восстановлением {user_config.new_name}',
            reply_markup=k_back_to_menu_users,
            parse_mode=ParseMode.HTML,

        )
    await state.clear()
    await state.clear()
