import asyncio
import os
from datetime import datetime

from Telegram.utils.admin import send_message_to_admins
from utils.log import log


async def ping_host(host: str = '195.91.139.50', hostname=''):
    down = []
    while True:
        param = '-n' if os.name == 'nt' else '-c'

        command = f'ping {param} 1 -w2 {host} > /dev/null 2>&1'

        response = os.system(command)

        if response == 0 and down:
            await send_message_to_admins(text=f"✅ {datetime.now()} - {hostname} {host} is UP! ✅")
            log.error(f"{hostname} {host} is UP!")
            down = []

        if response != 0:
            down.append(True)

        if len(down) == 2 and all(down):
            await send_message_to_admins(text=f"❌ {datetime.now()} - {hostname} {host} is DOWN! ❌")
            log.error(f"{hostname} {host} is DOWN!")

        await asyncio.sleep(10)
