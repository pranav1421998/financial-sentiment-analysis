## authenticates with Twitter API and starts streaming tweets containing financial keywords
## Tweets are saved as JSON files in data/raw/

import tweepy
import os
import json
import logging
from config.config import (TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                           TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET,
                           FINANCIAL_KEYWORDS, RAW_DATA_DIR, LOG_FILE)
from scripts.utils import setup_logging

# Setup logging
setup_logging(LOG_FILE)
logger = logging.getLogger(__name__)

def authenticate_twitter():
    auth = tweepy.OAuth1UserHandler(
        TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
        TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
    )
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        tweet_data = {
            'id': status.id_str,
            'created_at': str(status.created_at),
            'text': status.text,
            'user': status.user.screen_name
        }
        # Save tweet to file
        filename = os.path.join(RAW_DATA_DIR, f"{status.id_str}.json")
        with open(filename, 'w') as f:
            json.dump(tweet_data, f)
        logger.info(f"Collected tweet ID {status.id_str}")

    def on_error(self, status_code):
        logger.error(f"Streaming error: {status_code}")
        if status_code == 420:
            # Disconnect the stream to avoid being rate limited
            return False

def start_streaming(api):
    if not os.path.exists(RAW_DATA_DIR):
        os.makedirs(RAW_DATA_DIR)
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    logger.info("Starting Twitter stream...")
    stream.filter(track=FINANCIAL_KEYWORDS, languages=['en'])

if __name__ == "__main__":
    api = authenticate_twitter()
    start_streaming(api)
