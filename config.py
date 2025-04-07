import os

from dotenv import dotenv_values, find_dotenv

DEBUG = True

VERSION = '1.8.1'

config = dotenv_values(find_dotenv())

SERVER_IP = config['SERVER_IP']

IPV4NETWORK = config['IPV4NETWORK']
WG_SERVER_LOCAL_IP = config['WG_SERVER_LOCAL_IP']
WG_SERVER_PORT = config['WG_SERVER_PORT']

SYSTEM_LOG = './.log.txt'

PATH_WG = os.path.join('/', 'etc', 'wireguard')

WG_CONF = os.path.join(PATH_WG, 'wg0.conf')
WG_PRIVATE_KEY = os.path.join(PATH_WG, 'private.key')
WG_DUMP = './wg_dump.txt'

PATH_CONFIG = os.path.join(PATH_WG, 'confs')
PATH_QR = os.path.join(PATH_WG, 'qr')
PATH_KEYS = os.path.join(PATH_WG, 'keys')

PATH_CONFIG_DELETE = os.path.join(PATH_CONFIG, 'trash')
PATH_QR_DELETE = os.path.join(PATH_QR, 'trash')
PATH_KEYS_DELETE = os.path.join(PATH_KEYS, 'trash')

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'

for path in (PATH_CONFIG, PATH_QR, PATH_KEYS):
    os.makedirs(path, exist_ok=True)
    os.makedirs(os.path.join(path, 'trash'), exist_ok=True)
