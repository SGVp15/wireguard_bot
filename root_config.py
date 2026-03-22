from pathlib import Path

from dotenv import dotenv_values, find_dotenv

VERSION = '1.3'

config = dotenv_values(find_dotenv())

BOT_TOKEN: str | None = config.get('BOT_TOKEN')
ADMIN_ID: list[int] = [int(x) for x in config['ADMIN_ID'].split(',')]
USERS_ID: list[int] = [int(x) for x in config['USERS_ID'].split(',')]

if not BOT_TOKEN:
    raise f'ERROR .ENV {BOT_TOKEN=}'

DIR_DATA = Path('./data').resolve()
DIR_DATA.mkdir(parents=True, exist_ok=True)
LOG_FILE = DIR_DATA / 'log.txt'


DIR_template = DIR_DATA / 'output' / 'template'
DIR_template.mkdir(parents=True, exist_ok=True)
TEMPLATE_FILE_XLSX = DIR_template / 'template.xlsx'

PATH_DOWNLOAD_FILE = DIR_DATA / 'input'
DOCUMENTS = PATH_DOWNLOAD_FILE / 'documents'
DOCUMENTS.mkdir(parents=True, exist_ok=True)
SYSTEM_LOG = DIR_DATA / 'systemlog.txt'
