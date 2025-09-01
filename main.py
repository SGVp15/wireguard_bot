import asyncio

from Telegram.main import start_bot
from Telegram.scheduler_ping import ping_host
from utils.log import log


async def main():
    tasks = [
        start_bot(),
        ping_host('195.91.139.50', 'ITExpert-Rinet'),
        ping_host('82.198.187.7', 'ITExpert-Globus'),
        ping_host('82.142.155.191', 'VL Moscow'),
        ping_host('82.209.222.210', 'VL Minsk'),
        ping_host('45.8.117.13', 'VL KZ'),
    ]
    await asyncio.gather(*tasks)

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()


if __name__ == '__main__':
    log.info('wireguard-bot start')
    asyncio.run(main())
