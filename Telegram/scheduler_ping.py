import asyncio
import os

from Telegram.utils.admin import send_message_to_admins


async def ping_ip(ip: str = '195.91.139.50'):
    await asyncio.sleep(10)
    down = []
    while True:
        command = f'ping -c 1 -w2 {ip} '#> /dev/null 2>&1'
        response = os.system(command)

        if response == 0 and down:
            await send_message_to_admins(text=f"{ip} is UP!")
            print(f"{ip} is UP!")
            down = []

        if response != 0:
            down.append(True)

        if len(down) == 3 and all(down):
            await send_message_to_admins(text=f"{ip} is DOWN!")
            print(f"{ip} is DOWN!")

        await asyncio.sleep(5)
