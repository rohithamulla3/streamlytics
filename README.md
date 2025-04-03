# Streamlytics

Real-time social sentiment tracker using Twitter + Kafka + Spark + Elasticsearch + Grafana.

## Run Steps

1. Start services:
    docker-compose up -d

2. Start tweet ingestion:
    python twitter_stream.py

3. Start Spark streaming:
    spark-submit spark_streaming.py

4. Visit Grafana:
    http://localhost:3000
