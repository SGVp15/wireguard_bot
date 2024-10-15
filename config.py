from dotenv import dotenv_values, find_dotenv

config = dotenv_values('./.env')
print(config)
SERVER_IP = config['SERVER_IP']

LOG_FILE = './data/.log.txt'

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'
