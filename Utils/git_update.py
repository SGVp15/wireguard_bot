import os
import subprocess
import sys
from asyncio import sleep

from Utils.log import log


def check_for_updates():
    result = subprocess.run(["git", "pull"], capture_output=True, text=True)
    rows = str(result.stdout).split('\n')
    if len(rows) > 3:
        return True
    return False


def pull_updates():
    subprocess.run(["git", "pull"])


def restart_script():
    python = sys.executable
    os.execv(python, [python] + sys.argv)


async def git_update():
    if check_for_updates():
        log.info('BOT UPDATE')
        pull_updates()
        restart_script()
    await sleep(60)
