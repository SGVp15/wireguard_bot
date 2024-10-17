from xml.sax.handler import version

from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

SERVER_IP = config['SERVER_IP']

SYSTEM_LOG = './.log.txt'
WG_CONF = '/etc/wireguard/wg0.conf'
WG_DUMP = './wg_dump.txt'

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'


VERSION = '1.2'