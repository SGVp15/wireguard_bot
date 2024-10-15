from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from ..Call_Back_Data import CallBackData
from ..config import ADMIN_ID
from ..keybords.menu_main import k_main_menu
from ..main import dp, bot
from ..states.Form import Form
from wireguard.wireguard_class import WIREGUARD as wg
from utils.log import log


@dp.callback_query(Form.create_user,
                   F.data.in_({CallBackData.create_user_ok, })
                   & F.from_user.id.in_({*ADMIN_ID, })
                   )
async def create_user(callback_query: types.callback_query, state: FSMContext):
    print('create_user')
    data = await state.get_data()
    user = data.get('name')
    print(f'{user}')
    text, file, qr_code_file = wg.create_user(user)
    log.info('create_user {user}')
    await state.clear()

    file = FSInputFile(file, filename=user)
    await bot.send_message(
        text=f'Config file code {user}',
        chat_id=callback_query.from_user.id,
    )
    await bot.send_document(
        chat_id=callback_query.from_user.id,
        document=file, reply_markup=k_main_menu
    )

    file = FSInputFile(qr_code_file, filename=f'qr_{user}')
    await bot.send_message(
        text=f'QR code {user}',
        chat_id=callback_query.from_user.id,
    )
    await bot.send_document(
        chat_id=callback_query.from_user.id,
        document=file, reply_markup=k_main_menu
    )
