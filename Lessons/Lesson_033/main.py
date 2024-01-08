import smtplib
import time
import requests
from datetime import datetime
MY_LONG = -0.127758
MY_LAT = 41.377491

my_email = "email address to send from"
password = "code generated in the app for this code"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

longitude = data["iss_position"]['longitude']
latitude = data["iss_position"]['latitude']
def iss_overhead():
    if MY_LONG - 5 < longitude < MY_LONG + 5 and MY_LAT - 5 < latitude < MY_LAT + 5:
        return True
parameters = {
    "lat": MY_LONG,
    "long": MY_LAT,
    'formatted': 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
time_now = datetime.now().hour
def is_night():
    if time_now <= sunrise and time_now >= sunset:
        return True

while True:
    if is_night() and iss_overhead():
        connection = smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:Look up! \n\nThe ISS is above you in the sky."
        )
    time.sleep(1)
