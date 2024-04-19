from dotenv import dotenv_values

config = dotenv_values('./.env')

BOT_TOKEN = config['BOT_TOKEN']
ADMIN_ID = [int(x) for x in config['ADMIN_ID'].split(',')]
USERS_ID = [int(x) for x in config['USERS_ID'].split(',')]

SERVER_IP = config['SERVER_IP']

LOG_FILE = './data/.log.txt'

PATTERN_USER = r'\s*([А-Я][а-я]+\s+[А-Я][а-я]+)\s*'

EMAILS_SALLER = ['a.katkov@itexpert.ru', 'a.rybalkin@itexpert.ru', 'g.savushkin@itexpert.ru']
