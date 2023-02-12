import smtplib, ssl

# smtp_server = "smtp.Rgmail.com"
# port = 587  # For starttls
# my_email = "girlgus3351@gmail.com"
# password = "Rkskekfk1!"

# with server = smtplib.SMTP("smtp.gmail.com", 587) as server:
#     server.starttls()
#     server.login(user = my_email, password= password)
#     server.sendmail(
#         from_addr = my_email,
#         to_addrs = "rnjsrlgus0521@gmail.com",
#         msg = "Subject: Hello\n\n This is the body of mt email"
#     )

#     server.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday() 
# print(day_of_week)

date_of_birth = dt.datetime(year=1998 , month=9, day=28)
print(date_of_birth)