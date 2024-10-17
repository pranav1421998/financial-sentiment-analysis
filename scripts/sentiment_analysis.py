## reads preprocessed tweets, performs sentiment analysis, and saves the results to data/sentiment_data.csv

import os
import json
import pandas as pd
from langchain import OpenAI
from langchain.prompts import PromptTemplate
from config.config import OPENAI_API_KEY, PROCESSED_DATA_DIR, SENTIMENT_DATA_FILE, LOG_FILE
from scripts.utils import setup_logging
import logging

# Setup logging
setup_logging(LOG_FILE)
logger = logging.getLogger(__name__)

# Initialize OpenAI LLM
llm = OpenAI(openai_api_key=OPENAI_API_KEY)

# Define the prompt template
template = """
Analyze the sentiment of the following tweet and classify it as Positive, Negative, or Neutral.
Tweet: "{tweet}"
Sentiment:
"""
prompt = PromptTemplate(template=template, input_variables=['tweet'])

def analyze_sentiment(text):
    prompt_text = prompt.format(tweet=text)
    response = llm(prompt_text)
    sentiment = response.strip()
    return sentiment

def process_sentiment_analysis():
    tweets_data = []
    for filename in os.listdir(PROCESSED_DATA_DIR):
        processed_file = os.path.join(PROCESSED_DATA_DIR, filename)
        with open(processed_file, 'r') as f:
            tweet = json.load(f)
        cleaned_text = tweet.get('cleaned_text', '')
        sentiment = analyze_sentiment(cleaned_text)
        tweet['sentiment'] = sentiment
        tweets_data.append(tweet)
        logger.info(f"Analyzed sentiment for tweet ID {tweet['id']}")
    # Save the data to a CSV file
    df = pd.DataFrame(tweets_data)
    df.to_csv(SENTIMENT_DATA_FILE, index=False)
    logger.info(f"Sentiment data saved to {SENTIMENT_DATA_FILE}")

if __name__ == "__main__":
    process_sentiment_analysis()
