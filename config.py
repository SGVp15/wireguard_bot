from pathlib import Path

from dotenv import dotenv_values, find_dotenv


DEBUG = False

VERSION = '2.2.1'

config = dotenv_values(find_dotenv())

SYSTEM_LOG = './.log.txt'

PATH_VPN = Path('/root')

PATH_CONFIG = PATH_VPN / 'confs'
PATH_QR = PATH_VPN / 'qr'
PATH_KEYS = PATH_VPN / 'keys'

PATH_CONFIG_DELETE = PATH_CONFIG / 'trash'
PATH_QR_DELETE = PATH_QR / 'trash'
PATH_KEYS_DELETE = PATH_KEYS / 'trash'

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'

for path in (PATH_CONFIG, PATH_QR, PATH_KEYS):
    path.mkdir(parents=True, exist_ok=True)
    (path / 'trash').mkdir(parents=True, exist_ok=True)
