import asyncio
import subprocess

from pythonping import ping

from Telegram.utils.admin import send_message_to_admins


async def ping_ip(ip: str = '195.91.139.50'):
    await asyncio.sleep(10)
    down = []
    while True:
        command = f'ping -c 1 -w2 {ip} '  # > /dev/null 2>&1'

        process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()

        # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # output, error = process.communicate(timeout=1)

        if process.returncode == 0:
            print("Команда выполнена успешно")
        else:
            print("Ошибка при выполнении команды:", error)
        # process.kill()


        response = stdout
        print(response)
        if response == 0 and down:
            await send_message_to_admins(text=f"{ip} is UP!")
            print(f"{ip} is UP!")
            down = []

        if response != 0:
            down.append(True)

        if len(down) == 2 and all(down):
            await send_message_to_admins(text=f"{ip} is DOWN!")
            print(f"{ip} is DOWN!")

        await asyncio.sleep(3)
