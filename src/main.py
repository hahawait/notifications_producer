import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from apps.bot.bot import get_bot
from apps.app import send_unread_messages

from settings import get_config
from logger.logger import init_logger


def main():
    config = get_config()
    init_logger('INFO')
    user_bot = get_bot(config.bot_settings)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        send_unread_messages, 
        'interval', 
        minutes=60, 
        args=[config.producer_settings, user_bot,]
    )

    try:
        user_bot.start()
        scheduler.start()
    finally:
        loop = asyncio.get_event_loop()
        loop.run_forever()
        scheduler.shutdown()
        user_bot.disconnect()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Sheduler was stopped!!!")
