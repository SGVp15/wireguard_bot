import asyncio

from Telegram.main import start_bot
from Telegram.scheduler_ping import ping_host
from utils.log import log
from wireguard.wireguard_class import WIREGUARD


async def main():
    tasks = [
        start_bot(),
        ping_host(),
    ]
    # await asyncio.gather(*tasks)

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()


if __name__ == '__main__':
    WIREGUARD().create_all_qrcodes()
    log.info('wireguard-bot start')
    asyncio.run(main())
