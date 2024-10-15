from aiogram import F
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from ..Call_Back_Data import CallBackData
from ..config import ADMIN_ID
from ..keybords.inline import main_menu
from ..main import dp, bot
from ..states.Form import Form
from WG import wg
from utils.log import log


@dp.callback_query(Form.menu_restart_service_wg,
                   F.data.in_({CallBackData.restart_service_wg_ok, })
                   & F.from_user.id.in_({*ADMIN_ID, })
                   )
async def restart_service(callback_query: types.callback_query, state: FSMContext):
    await state.clear()
    restart_service()
    await bot.send_message(text='restart service - ok',
                           chat_id=callback_query.from_user.id,
                           reply_markup=main_menu
                           )
