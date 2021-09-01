#!/bin/bash

curl -X POST "http://localhost:8083/connectors" -H 'Content-Type: application/json' -d'
{
    "name": "crypto-sink",
    "config": {
        "connector.class": "io.confluent.connect.elasticsearch.ElasticsearchSinkConnector",
        "type.name": "kafka-connect",
        "topics": "crypto",
        "tasks.max": "2",
        "value.converter": "org.apache.kafka.connect.json.JsonConverter",
        "connection.url": "http://elastic_kibana:9200",
        "key.ignore": "true",
        "key.converter": "org.apache.kafka.connect.json.JsonConverter"
    }
}
'