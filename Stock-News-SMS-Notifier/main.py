# Import necessary libraries and modules
import requests  # To get information from the internet
from twilio.rest import Client  # To send text messages
import os  # To access secret information securely
from dotenv import load_dotenv  # To load secrets from a file

# Load secret information from a file (for security)
load_dotenv()

# Get phone numbers and API credentials from secret information
sender_number = os.getenv("sender_number")
receiver_number = os.getenv("receiver_number")
Account_SID = os.getenv("Account_SID")
Auth_Token = os.getenv("Auth_Token")

# Get the name of the stock and company from secret information
NEWS_API = os.getenv("NEWS_API")
STOCK_NAME = os.getenv("STOCK_NAME")
COMPANY_NAME = os.getenv("COMPANY_NAME")

# Define where to get stock market data
STOCK_ENDPOINT = os.getenv("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.getenv("NEWS_ENDPOINT")
STOCK_API = os.getenv("STOCK_API")

# Define how to ask for stock market data
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": os.getenv("STOCK_API"),
}

# Get daily stock market data
stock_response = requests.get(STOCK_ENDPOINT, params=parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]

# Make a list of daily stock data points
data_list = [value for (key, value) in stock_data.items()]

# Print the list of stock data points
print(data_list)

# Get yesterday's closing price
yesterday_data = float(data_list[0]["4. close"])
print(yesterday_data)

# Get the day before yesterday's closing price
day_before_yesterday = float(data_list[1]["4. close"])
print(day_before_yesterday)

# Calculate how much the stock price changed from yesterday to the day before yesterday
diff = yesterday_data - day_before_yesterday
print(diff)

# Decide if the stock price went up or down and calculate how much it changed in percentage
up_down = "📈" if diff > 0 else "📉"
percent = (diff / yesterday_data) * 100
print(percent)

# Check if the percentage change is big enough to be interesting (0.5% or more)
if abs(percent) > 0.5:
    # Define how to ask for news articles
    news_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API,
    }

    # Get news articles about the company
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()

    # Make a list of news articles
    articles = news_response.json()["articles"]

    # Select the top three news articles
    articles_list = articles[:3]
    print(articles_list)

    # Make the news articles look nice with stock information
    formatted_article = [f"{STOCK_NAME}:{up_down}{round(percent)}\n" \
                         f"Headline:{articles['title']}\nBrief:{articles['description']}" for articles in articles_list]
    print(formatted_article)

    # Set up a way to send text messages
    client = Client(Account_SID, Auth_Token)

    # Send text messages with the nice news articles to a phone number
    for article in formatted_article:
        message = client.messages \
            .create(
            body=article,
            from_=sender_number,
            to=receiver_number,
        )
        # Print the status of each sent message
        print(message.status)