##################### Starting Project ######################
import smtplib
from datetime import datetime
import pandas
import random


my_email = "bilalroze94@gmail.com"
password = "BIaq#123abcd"

# Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)

# Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")

# Dictionary comprehension template for pandas DataFrame:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates
    # and replace the [NAME] with the person's actual name from birthdays.csv
    # Think about the relative file path to open each letter.
    # Use the random module to get a number between 1-3 to pick a random letter.
    # Use the replace() method to replace [NAME] with the actual name.
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the letter generated to that person's email address.
    # Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    # call .starttls()
    # Log in to your email service with email/password.
    # Making sure security setting is set to allow less secure apps.
    # The message should have the Subject: Happy Birthday then after \n\n The Message Body.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Happy Birthday\n\n{contents}")
