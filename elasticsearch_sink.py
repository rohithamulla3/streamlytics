from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

def index_to_elasticsearch(record):
    es.index(index="tweets_sentiment", document=record)
