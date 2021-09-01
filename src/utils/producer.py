import json
import datetime as dt
from kafka import KafkaProducer
from .logger import CryptoLogger


# Define process logger
logger = CryptoLogger()

def init_producer():
    logger.info('Initializing Kafka producer at {}'.format(dt.datetime.utcnow()))
    producer = KafkaProducer(
      bootstrap_servers='localhost:9092',
      value_serializer=lambda v: json.dumps(v, default=str).encode('utf-8')
    )
    logger.info('Initialized Kafka producer at {}'.format(dt.datetime.utcnow()))

    return producer
