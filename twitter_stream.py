import tweepy
from kafka import KafkaProducer
import json

BEARER_TOKEN = 'YOUR_TWITTER_BEARER_TOKEN'
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

class TwitterStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        if tweet.referenced_tweets is None:
            data = {'text': tweet.text, 'id': tweet.id, 'created_at': str(tweet.created_at)}
            print("Sending tweet to Kafka:", data)
            producer.send('raw_tweets', value=data)

stream = TwitterStream(BEARER_TOKEN)
stream.add_rules(tweepy.StreamRule("data OR AI OR football"))
stream.filter(tweet_fields=['created_at'])
