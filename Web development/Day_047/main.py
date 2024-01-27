# from bs4 import BeautifulSoup
# import requests
# import lxml
#
# headers = {
#     "Accept-Language": "en-US,en;q=0.9",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# }
# response = requests.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6", headers=headers)
# webpage = response.content
# soup = BeautifulSoup(webpage, "lxml")
# print(soup.prettify())

import smtplib
import datetime as dt
from random import *

my_email = "a69707776@gmail.com"
password = "ahll idge dpwo uqhg"
price = 100
if price < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="avazxonnazirov334@gmail.com",
            msg=f"Subject: Price Alert!\n\n The price is ${price} now"
        )

