
# Real-time Financial Sentiment Analysis from Twitter

## Overview
This project aims to build a real-time financial sentiment analysis system by collecting tweets related to finance and analyzing their sentiment using GPT-3 integrated with LangChain. The system includes a data pipeline for tweet collection and preprocessing, a sentiment analysis module, and a visualization dashboard.

## Features
- **Real-time Tweet Collection:** Uses Tweepy to scrape tweets containing financial keywords.
- **Data Preprocessing:** Filters out noise, handles language variations, and cleans text data.
- **Sentiment Analysis:** Integrates GPT-3 with LangChain for enhanced sentiment classification.
- **Visualization Dashboard:** Displays sentiment trends using an interactive Streamlit app.
- **Scalable Deployment:** Designed to be deployed on AWS for scalability and reliability.

## Table of Contents
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
  1. [Data Collection](#1-data-collection)
  2. [Data Preprocessing](#2-data-preprocessing)
  3. [Sentiment Analysis](#3-sentiment-analysis)
  4. [Visualization Dashboard](#4-visualization-dashboard)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Structure

```
financial_sentiment_analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── config/
│   └── config.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── sentiment_data.csv
├── logs/
│   └── app.log
├── scripts/
│   ├── data_collection.py
│   ├── data_preprocessing.py
│   ├── sentiment_analysis.py
│   └── utils.py
├── dashboard/
│   └── dashboard.py
├── models/
│   └── __init__.py
└── tests/
    └── test_utils.py
```

- `config/`: Configuration files and settings.
- `data/`: Contains raw, processed, and final sentiment data.
- `logs/`: Log files for monitoring and debugging.
- `scripts/`: Core scripts for data collection, preprocessing, and analysis.
- `dashboard/`: Streamlit app for data visualization.
- `models/`: Placeholder for any machine learning models (optional).
- `tests/`: Unit tests for the project.

## Prerequisites
- Python 3.7 or higher
- Twitter Developer Account: Access to the Twitter API.
- OpenAI Account: API key for GPT-3.
- AWS Account (Optional): For deployment purposes.

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/financial_sentiment_analysis.git
cd financial_sentiment_analysis
```

### Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts ctivate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration

### Set Up Environment Variables
Create a `.env` file in the project root directory:
```bash
touch .env
```

Add your API keys and configuration variables to the `.env` file:
```env
# Twitter API credentials
TWITTER_CONSUMER_KEY=your_consumer_key
TWITTER_CONSUMER_SECRET=your_consumer_secret
TWITTER_ACCESS_TOKEN=your_access_token
TWITTER_ACCESS_SECRET=your_access_secret

# OpenAI API key
OPENAI_API_KEY=your_openai_api_key
```

### Update Configuration File
The `config/config.py` file is already set up to read from environment variables. Ensure that all paths and settings meet your requirements.

## Running the Application

### 1. Data Collection
Run the data collection script to start collecting tweets in real-time.
```bash
python scripts/data_collection.py
```
- **Description:** This script uses Tweepy to stream tweets containing predefined financial keywords.
- **Output:** Raw tweet data saved as JSON files in `data/raw/`.

### 2. Data Preprocessing
Process the collected tweets to clean and normalize the text.
```bash
python scripts/data_preprocessing.py
```
- **Description:** Filters out non-English tweets, removes noise like URLs and mentions, and normalizes the text.
- **Output:** Cleaned tweet data saved in `data/processed/`.

### 3. Sentiment Analysis
Perform sentiment analysis on the preprocessed tweets.
```bash
python scripts/sentiment_analysis.py
```
- **Description:** Uses GPT-3 via LangChain to classify the sentiment of each tweet.
- **Output:** Sentiment data saved to `data/sentiment_data.csv`.

### 4. Visualization Dashboard
Launch the Streamlit dashboard to visualize sentiment trends.
```bash
streamlit run dashboard/dashboard.py
```
- **Description:** Displays real-time sentiment analysis results, including sentiment distribution and trends over time.
- **Access:** Open the provided local URL in your web browser.

## Usage
- **Filtering Data:** Use the sidebar in the dashboard to filter data by date range.
- **Viewing Latest Tweets:** The dashboard displays the latest analyzed tweets with their sentiment classification.
- **Monitoring Logs:** Check `logs/app.log` for real-time logging information.

## Testing
Run unit tests to verify that utility functions are working as expected.
```bash
python -m unittest discover tests
```
- **Description:** Executes all tests in the `tests/` directory.

## Contributing
Contributions are welcome! Please follow these steps:

### Fork the Repository
Click the "Fork" button at the top right of the repository page.

### Create a New Branch
```bash
git checkout -b feature/your_feature_name
```

### Commit Your Changes
```bash
git commit -am 'Add new feature'
```

### Push to the Branch
```bash
git push origin feature/your_feature_name
```

### Create a Pull Request
Submit a pull request detailing your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- OpenAI for providing the language model used.
- LangChain for seamless LLM integration.
- Streamlit for the interactive dashboard framework.
- Tweepy for Twitter API integration.

Feel free to open an issue if you find any bugs or have suggestions for improvements. Happy coding!
