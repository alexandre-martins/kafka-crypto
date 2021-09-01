# Kafka-crypto

Simple implementation of a kafka stack with custom producer and kafka-connect consumer
to gather real time cryptocurrency data and send it to an elasticsearch cluster.

## Usage

1. Install project requirements
    ```bash
    pip install -r requirements.txt
    ```
2. Spin up infrastrucuture (Kafka stack, elasticsearch and kibana)
    ```bash
    docker-compose up -d
    ```
3. Create kafka topic inside broker container
    ```bash
    docker exec -it <kafka_broker_container_id> bash
    kafka-topics --create --topic crypto --partitions 3 --replication-factor 1 --zookeeper zoo1:2181
    ```
4. Start producing data
    ```bash
    python src/request_data.py
    ```
5. Create kafka-connect elasticsearch sink
    ```bash
    bash scripts/elastic_sink.sh
    ```
6. Verify if data is being sinked to the elasticsearch cluster
    ```bash
    bash scripts/query.sh
    ```
    You should receive some output with the collected data.

If you want to, you can access some user interfaces on:

- localhost:8001 -> Kafka topics UI
- localhost:8003 -> Kafka-connect UI
- localhost:5601 -> Kibana (for building real-time dashboards)

Have fun :)
