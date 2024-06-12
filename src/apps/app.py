from telethon import TelegramClient

from settings import ProducerSettings

from apps.bot.handlers import handle_unread_messages
from apps.producer.producer import RabbitMQFacade
from apps.producer.connection import RabbitMQConnection


async def send_unread_messages(settings: ProducerSettings, user_bot: TelegramClient):
    connection = RabbitMQConnection(settings)
    rabbitmq_facade = RabbitMQFacade(settings.QUEUE_NAME, connection)

    unread_messages = await handle_unread_messages(user_bot)
    rabbitmq_facade.send_unread_messages(unread_messages)
