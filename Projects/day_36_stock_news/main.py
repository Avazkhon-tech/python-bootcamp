import requests
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = "HMLHW02HBB2YKN4T"
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key
}

auth_token = "auth token"
account_sid = "account sid"


# url = 'https://www.alphavantage.co/query'
# r = requests.get(url, params=parameters)
# data = r.json()
# data = data["Time Series (Daily)"]
# last_two_dates = [f"{(list(data))[i]}" for i in range(2)]

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stock_price():
    # I could not finish this part because api call limit was reached
    return True
# yesterday_close = data[last_two_dates[0]]['4. close']
# print(yesterday_close)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
url = "https://newsapi.org/v2/everything?q=bitcoin&apiKey=978922e357bd4b828482a45831547ea2"
response = requests.get(url)
news_data = response.json()
title = news_data["articles"][0]['title']
description = news_data["articles"][0]['description']
print(description)

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
if check_stock_price():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"{STOCK}"
             f"Headline: {title}\n"
             f"Brief: {description}",
        from_='from number',
        to='to number'
    )
    print(message.status)

