import asyncio

from Telegram.main import start_bot
from Utils.log import log


async def main():
    await start_bot()


if __name__ == '__main__':
    try:
        log.info('bot START')
        # asyncio.run сам создаст loop и запустит main()
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        log.info("Бот остановлен")
    finally:
        log.error('Exam_Registration_bot STOP')
