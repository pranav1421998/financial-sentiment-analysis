import os
from dotenv import load_dotenv
load_dotenv()

# Twitter API credentials
TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')

# OpenAI API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Data directories
DATA_DIR = 'data'
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
SENTIMENT_DATA_FILE = os.path.join(DATA_DIR, 'sentiment_data.csv')

# Log file
LOG_FILE = 'logs/app.log'

# Financial keywords for tweet collection
FINANCIAL_KEYWORDS = ['stock', 'market', 'invest', 'trading', 'NASDAQ', 'NYSE', 'S&P 500']
