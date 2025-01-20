import os
from dotenv import dotenv_values, find_dotenv

DEBUG = True

VERSION = '1.7.1'

config = dotenv_values(find_dotenv())

SERVER_IP = config['SERVER_IP']

IPV4NETWORK = '172.26.10.1/24'

WG_SERVER_PORT = 443

SYSTEM_LOG = './.log.txt'

PATH_WG = os.path.join('/', 'etc', 'wireguard')

WG_CONF = os.path.join(PATH_WG, 'wg0.conf')
WG_PRIVATE_KEY = os.path.join(PATH_WG, 'private.key')
WG_DUMP = './wg_dump.txt'

PATH_CONFIG = os.path.join(PATH_WG, 'confs')
PATH_QR = os.path.join(PATH_WG, 'qr')
PATH_KEYS = os.path.join(PATH_WG, 'keys')

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'

for path in (PATH_CONFIG, PATH_QR, PATH_KEYS):
    os.makedirs(path, exist_ok=True)
