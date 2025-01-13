import os
import os.path

from aiogram import F, Router
from aiogram.types import FSInputFile, CallbackQuery

from Telegram.Call_Back_Data import CallBackData
from Telegram.config import ADMIN_ID
from Telegram.loader import bot
from Telegram.modules.admin.keyboards.menu_admin import k_menu_admin
from Telegram.modules.admin.keyboards.menu_files import get_config_list_files_keyboard
from config import PATH_QR

router = Router(name=__name__)

