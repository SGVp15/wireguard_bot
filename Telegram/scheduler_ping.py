import asyncio
import os

from Telegram.utils.admin import send_message_to_admins


async def ping_host(host: str = '195.91.139.50'):
    down = []
    while True:
        # command = f'ping -c 1 -w2 {host} > /dev/null 2>&1'

        param = '-n' if os.name == 'nt' else '-c'
        hostname = '195.91.139.50'
        response = os.system(f"ping {param} 1 {hostname}")
        if response is None and down:
            await send_message_to_admins(text=f"{host} is UP!")
            print(f"{host} is UP!")
            down = []

        if response != 0:
            down.append(True)

        if len(down) == 2 and all(down):
            await send_message_to_admins(text=f"{host} is DOWN!")
            print(f"{host} is DOWN!")

        await asyncio.sleep(3)
