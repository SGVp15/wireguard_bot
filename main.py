import asyncio
import signal

from Telegram.main import start_bot
from Telegram.scheduler_ping import ping_ip
from utils.log import log
from wireguard.wireguard_class import WIREGUARD


async def ping_ip_with_cancellation(cancellation_event):
    """Continuously pings the IP address until cancellation is requested."""
    while True:
        try:
            await asyncio.wait_for(ping_ip(), timeout=60)  # Ping every 60 seconds
        except asyncio.TimeoutError:
            log.warning("Ping timed out.")
        except asyncio.CancelledError:
            log.info("Ping loop cancelled.")
            break
        await asyncio.sleep(1)  # Brief delay between pings


async def main():
    tasks = [
        start_bot(),
        ping_ip_with_cancellation(asyncio.Event()),  # Pass a cancellation event
    ]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    WIREGUARD().create_all_qrcodes()
    log.info('wireguard-bot start')

    # Graceful shutdown on Ctrl+C
    cancellation_event = asyncio.Event()
    signal.signal(signal.SIGINT, lambda sig, frame: cancellation_event.set())

    asyncio.run(main(), cancellation_event=cancellation_event)
