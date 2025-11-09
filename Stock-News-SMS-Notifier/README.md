# Stock-News-SMS-Notifier
## Stock News SMS Notifier
The Stock News SMS Notifier is a Python script designed to keep you informed about stock market trends and related news articles via SMS notifications. This project combines financial data retrieval, analysis, and news aggregation to provide valuable insights in real-time.

## Key Features
Fetches daily stock market data for a specified stock using the Alpha Vantage API.
Calculates the percentage change in stock prices and determines whether they are rising or falling.
Retrieves news articles related to a specific company from a news API (e.g., NewsAPI).
Sends SMS notifications containing stock information and news headlines using Twilio.
## How It Works
The script retrieves daily stock market data for a chosen stock, calculates price changes, and determines stock trends.

If a significant change is detected, it searches for news articles related to the associated company.

Relevant news headlines and stock information are formatted into SMS messages.

SMS messages are sent to a specified phone number using Twilio, providing timely updates on stock performance and related news.

## Getting Started
To use the Stock News SMS Notifier:

Set up your environment variables, including API keys and phone numbers, in a .env file.

Run the script to start monitoring your chosen stock and receiving SMS notifications.
