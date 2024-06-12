import pika
import logging
from settings import ProducerSettings


class RabbitMQConnection:
    _instance = None
    _connection_params = None
    _logger = logging.getLogger("RabbitMQConnection")

    def __new__(cls, settings: ProducerSettings) -> "RabbitMQConnection":
        if cls._instance is None:
            cls._instance = super(RabbitMQConnection, cls).__new__(cls)
            cls._connection_params = pika.ConnectionParameters(
                host=settings.PRODUCER_HOST,
                port=settings.PRODUCER_PORT,
                virtual_host=settings.VIRTUAL_HOST,
                credentials=pika.PlainCredentials(
                    username=settings.PRODUCER_USERNAME, 
                    password=settings.PRODUCER_PASSWORD
                )
            )
            cls._connection = None
            cls._channel = None
            cls._logger.info("RabbitMQConnection instance created")
        return cls._instance

    def connect(self):
        if self._connection is None:
            self._connection = pika.BlockingConnection(self._connection_params)
            self._channel = self._connection.channel()
            self._logger.info("RabbitMQ connection established")
        return self._channel

    def __enter__(self):
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @classmethod
    def close(cls):
        if cls._connection is not None:
            cls._connection.close()
            cls._connection = None
            cls._logger.info("RabbitMQ connection closed")
        else:
            cls._logger.info("Connection already closed")
            pass
