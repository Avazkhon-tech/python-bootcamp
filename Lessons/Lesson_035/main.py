import requests
from twilio.rest import Client

weather_params = {
    "lat": '',
    "lon": '',
    "appid": '',
    "cnt": "4"
}
# api authentication

auth_token = "auth token"
account_sid = "account sid"

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()
data = response.json()

weather_ids = [data['list'][i]['weather'][0]['id'] for i in range(4)]
will_rain = False
for i in weather_ids:
    if i < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Remember to bring an umbrella!",
        from_='from number',
        to='to number'
    )
    print(message.status)


