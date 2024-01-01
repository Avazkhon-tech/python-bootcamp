import smtplib
import datetime as dt
from random import *

my_email = "a69707776@gmail.com"
password = "ahll idge dpwo uqhg"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open('quotes.txt') as file:
        data = file.readlines()
        quote = choice(data)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="avazkhonnazirov@yahoo.com",
            msg=f"Subject:Hello\n\n{quote}")




