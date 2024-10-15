import logging

from config import SYSTEM_LOG

file_log = logging.FileHandler(SYSTEM_LOG)
console_out = logging.StreamHandler()


def configure_logging(level=logging.INFO):
    logging.basicConfig(
        handlers=(file_log, console_out),
        level=level,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="[%(asctime)s.%(msecs)03d] %(module)10s:%(lineno)-3d %(levelname)-7s - %(message)s",
        encoding='utf-8',
    )


configure_logging()
log = logging.getLogger(__name__)

#
# def backup_logs():
#     with open(file=LOG_FILE, mode="r", encoding='utf-8') as f:
#         s = f.read()
#     with open(file=LOG_BACKUP, mode="a", encoding='utf-8') as f:
#         f.write(s + '\n')
