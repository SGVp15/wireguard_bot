import asyncio

from Telegram.main import start_bot
from utils.log import log


async def main():
    tasks = [
        start_bot(),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    log('WG-bot start')
    asyncio.run(main())
