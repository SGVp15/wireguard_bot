from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

BOT_TOKEN: str | None = config.get('BOT_TOKEN')
ADMIN_ID: list[int] = [int(x) for x in config['ADMIN_ID'].split(',')]
USERS_ID: list[int] = [int(x) for x in config['USERS_ID'].split(',')]

LOG_FILE: str = './data/log.txt'
