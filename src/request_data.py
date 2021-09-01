import json, requests, asyncio, yaml
import datetime as dt
from utils.producer import init_producer
from utils.logger import CryptoLogger


# Define process logger
logger = CryptoLogger()

def get_configs(type):
    """Read the config files definied in configs/ dir."""

    if type == 'currencies':
        path = 'src/configs/currencies.yaml'
        with open(path, 'rb') as f:
            config = yaml.safe_load(f)
        return config
    elif type == 'schema':
        path = 'src/configs/schema.json'
        with open(path, 'r') as f:
            schema = json.load(f)
        return schema
    else:
        raise ValueError("Config type not definied.")


async def get_crypto_currency(producer, topic, partition, crypto, request_frequency, schema):
    while True:
        endpoint = f'https://api.coinbase.com/v2/prices/{crypto}-USD/spot'
        response = requests.get(endpoint)

        if response.status_code == 200:
            raw_data = json.loads(response.content)

            data = {
              "schema": schema,
              "payload": {
                "timestamp": dt.datetime.utcnow(),
                "currency": raw_data['data']['base'],
                "amount": float(raw_data['data']['amount'])
              }
            }
            logger.info('API requested at {0}'.format(dt.datetime.utcnow()))
            logger.info('Producing record: {}'.format(data))
            # Produce record to kafka
            producer.send(topic=topic, partition=partition, value=data)
        else:
            logger.info(f'API request failed with status code {response.status_code} at {dt.datetime.utcnow()}')

        await asyncio.sleep(request_frequency)

# Turn on kafka producer
producer = init_producer()

curr = get_configs(type='currencies')
schema = get_configs(type='schema')

async def main():
    tasks = []
    for currency in curr['currencies']:
        tasks.append(
            get_crypto_currency(
                producer,
                'crypto',
                currency['partition'],
                currency['name'],
                currency['request_frequency'],
                schema=schema
            )
        )

    await asyncio.gather(*tasks)


if __name__=='__main__':
    asyncio.run(main())
