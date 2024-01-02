##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
from random import choice

letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

now = dt.datetime.now()
day_now = now.day
month_now = now.month
year_now = now.year

data = pandas.read_csv('birthdays.csv')
no_of_people = len(data)

for i in range(no_of_people):
    name = data.loc[i]['name']
    year = data.loc[i]['year']
    month = data.loc[i]['month']
    day = data.loc[i]['day']
    if year == year_now and month == month_now and day == day_now:
        letter = choice(letters)
        with open(f'letter_templates/{letter}', 'r') as file:
            wish = file.read()
            wish = wish.replace('[NAME]', name)





# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




