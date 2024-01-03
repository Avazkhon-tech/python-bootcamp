##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
from random import choice
import smtplib

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
now = dt.datetime.now()
day_now = now.day
month_now = now.month

data = pandas.read_csv('birthdays.csv')
no_of_people = len(data)

my_email = "a69707776@gmail.com"
password = "ahll idge dpwo uqhg"

for i in range(no_of_people):
    email = data.loc[i]['email']
    name = data.loc[i]['name']
    month = data.loc[i]['month']
    day = data.loc[i]['day']
    if month == month_now and day == day_now:
        letter = choice(letters)
        with open(f'letter_templates/{letter}', 'r') as file:
            wish = file.read()
            wish = wish.replace('[NAME]', name)

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email,
                                msg=f"Subject: Happy Birthday\n\n"
                                    f"{wish}")


