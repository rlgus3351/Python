#Todo 1. Use the datetime module too botain thje currnet dat of the week .
#Todo 2. Open the quotes.txt file and obtain a list of quotes.  
#Todo 3. use the random module ot pick a random quote from your list of quotes. 
#Todo 4. user tme smtplib so send the email to yourself.
from multiprocessing import connection
import smtplib
import datetime as dt
import random

MY_EMAIL = "gihyun3351@gmail.com"
MY_PASSWORD = "Rkskekfk1!"


now = dt.datetime.now()
weekday = now.weekday() 
if weekday == 6:
    with open(file = "quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote =random.choice(all_quotes)
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs= MY_EMAIL, 
            msg =f"Subject : Monday Motivaiton\n\n{quote}"
        )

