import logging
import re
from langdetect import detect

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\S+', '', text)     # Remove mentions
    text = re.sub(r'#\S+', '', text)     # Remove hashtags
    text = re.sub(r'\s+', ' ', text)     # Remove extra whitespace
    text = text.strip().lower()
    return text
