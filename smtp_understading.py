import smtplib
import datetime as dt
import random

my_email = "bilalroze94@gmail.com"
password = "BIaq#123abcd"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Wednesday Motivation\n\n{quote}"
                            )


















# import smtplib
# import random
#
# my_email = "bilalroze94@gmail.com"
# password = "BIaq#123abcd"
#
# with smtplib.SMTP("smtp.gmail.com") as new_connection:
#     # Starting transport layer security, to secure the connection
#     new_connection.starttls()
#     # Loging into email provider
#     new_connection.login(user=my_email, password=password)
#     new_connection.sendmail(from_addr=my_email,
#                             to_addrs="cs21.bilal@gmail.com",
#                             msg="Subject:Hi\n\nThis is the body of the gmail.")


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day = now.day
# day_of_week = now.weekday()
# print(day_of_week)
#
#
# date_of_birth = dt.datetime(year=1997, month=3, day=3, hour=4)
# print(date_of_birth)


