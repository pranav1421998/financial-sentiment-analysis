## reads raw tweet files, cleans the text, and saves the preprocessed data in data/processed/

import os
import json
from config.config import RAW_DATA_DIR, PROCESSED_DATA_DIR, LOG_FILE
from scripts.utils import setup_logging, clean_text, is_english
import logging

# Setup logging
setup_logging(LOG_FILE)
logger = logging.getLogger(__name__)

def preprocess_tweets():
    if not os.path.exists(PROCESSED_DATA_DIR):
        os.makedirs(PROCESSED_DATA_DIR)
    for filename in os.listdir(RAW_DATA_DIR):
        raw_file = os.path.join(RAW_DATA_DIR, filename)
        processed_file = os.path.join(PROCESSED_DATA_DIR, filename)
        with open(raw_file, 'r') as f:
            tweet = json.load(f)
        text = tweet.get('text', '')
        # Exclude retweets and replies
        if text.startswith('RT @') or 'retweeted_status' in tweet:
            continue
        # Check if the text is English
        if not is_english(text):
            continue
        # Clean and normalize text
        cleaned_text = clean_text(text)
        tweet['cleaned_text'] = cleaned_text
        # Save preprocessed tweet
        with open(processed_file, 'w') as f:
            json.dump(tweet, f)
        logger.info(f"Preprocessed tweet ID {tweet['id']}")

if __name__ == "__main__":
    preprocess_tweets()
