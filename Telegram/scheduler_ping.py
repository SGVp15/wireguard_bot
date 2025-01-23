import asyncio
import os
from datetime import datetime

from Telegram.utils.admin import send_message_to_admins
from utils.log import log


async def ping_host(host: str = '195.91.139.50', hostname='', num=5):
    down = []
    host_is_down = False
    while True:
        param = '-n' if os.name == 'nt' else '-c'

        command = f'ping {param} 1 -w2 {host} > /dev/null 2>&1'

        response = os.system(command)

        if response == 0 and host_is_down:
            await send_message_to_admins(text=f'✅ {datetime.now()} - {hostname} {host} is UP! ✅')
            log.error(f'{hostname} {host} is UP!')
            down = []
            host_is_down = False

        if response != 0:
            down.append(True)

        if len(down) == num and all(down):
            host_is_down = True
            await send_message_to_admins(text=f'❌ {datetime.now()} - {hostname} {host} is DOWN! ❌')
            log.error(f'{hostname} {host} is DOWN!')

        await asyncio.sleep(10)
