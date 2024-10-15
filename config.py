from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

SERVER_IP = config['SERVER_IP']

SYSTEM_LOG = './data/.log.txt'

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'
