import asyncio

from Telegram.main import start_bot


async def main():
    tasks = [
        start_bot(),
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    print('WG-bot start')
    asyncio.run(main())