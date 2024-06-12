import json
from apps.models import Message
from apps.producer.connection import RabbitMQConnection


class RabbitMQFacade:
    def __init__(self, queue_name: str, connection: RabbitMQConnection) -> None:
        self.queue_name = queue_name
        self.connection = connection

    def send_unread_messages(self, messages: list[Message]):
        messages_json = json.dumps([message.model_dump_json() for message in messages])
        with self.connection as channel:
            channel.queue_declare(queue=self.queue_name, durable=True)
            channel.basic_publish(
                exchange='', 
                routing_key=self.queue_name, 
                body=messages_json.encode('utf-8')
            )
