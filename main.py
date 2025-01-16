import asyncio

from Telegram.main import start_bot
from Telegram.scheduler_ping import ping_ip
from utils.log import log
from wireguard.wireguard_class import WIREGUARD


async def main():
    tasks = [
        start_bot(),
        # ping_ip(),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    WIREGUARD().create_all_qrcodes()
    log.info('wireguard-bot start')
    asyncio.run(main())
