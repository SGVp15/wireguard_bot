import logging

from config import SYSTEM_LOG

logging.basicConfig(
    filename=SYSTEM_LOG,
    level=logging.INFO,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)
