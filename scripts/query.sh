#!/bin/bash

curl -X GET "localhost:9200/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "query": {
    "type": {
      "value": "kafka-connect"
    }
  }
}
'