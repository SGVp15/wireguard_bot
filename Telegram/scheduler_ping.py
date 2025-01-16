import asyncio

import ping3

from Telegram.utils.admin import send_message_to_admins


async def ping_host(host: str = '195.91.139.50'):
    down = []
    while True:
        command = f'ping -c 1 -w2 {host} '  # > /dev/null 2>&1'

        # process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE)
        # stdout, stderr = await process.communicate()
        response = ping3.ping(host)
        # if response is None:
        # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # output, error = process.communicate(timeout=1)

        # if process.returncode == 0:
        #     print("Команда выполнена успешно")
        # else:
        #     print("Ошибка при выполнении команды:", stderr)
        #
        #
        # response = stdout
        # print(response)
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
