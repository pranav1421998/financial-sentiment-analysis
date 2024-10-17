## The dashboard displays sentiment distribution and trends over time.
## Users can filter data by date range using the sidebar.

import streamlit as st
import pandas as pd
import plotly.express as px
from config.config import SENTIMENT_DATA_FILE

# Set page configuration
st.set_page_config(page_title='Financial Sentiment Analysis', layout='wide')

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv(SENTIMENT_DATA_FILE)
    data['created_at'] = pd.to_datetime(data['created_at'])
    return data

data = load_data()

# Sidebar filters
st.sidebar.header('Filters')
start_date = st.sidebar.date_input('Start Date', data['created_at'].min())
end_date = st.sidebar.date_input('End Date', data['created_at'].max())

# Filter data based on user input
filtered_data = data[(data['created_at'] >= pd.to_datetime(start_date)) &
                     (data['created_at'] <= pd.to_datetime(end_date))]

# Main dashboard
st.title('Real-time Financial Sentiment Analysis')

st.subheader('Sentiment Distribution')
sentiment_counts = filtered_data['sentiment'].value_counts()
st.bar_chart(sentiment_counts)

st.subheader('Sentiment Over Time')
filtered_data['sentiment_score'] = filtered_data['sentiment'].map({'Positive': 1, 'Neutral': 0, 'Negative': -1})
time_chart = px.line(filtered_data, x='created_at', y='sentiment_score', title='Sentiment Score Over Time')
st.plotly_chart(time_chart, use_container_width=True)

st.subheader('Latest Tweets')
st.dataframe(filtered_data[['created_at', 'user', 'text', 'sentiment']].tail(10))
