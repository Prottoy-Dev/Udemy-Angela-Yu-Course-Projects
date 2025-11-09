"""
Birthday Reminder and Email Automation

This script reads a CSV file containing birthday data and checks if there are any birthdays
today. If a birthday is found, it sends a birthday email to the person using a random
template.

Dependencies:
- datetime
- random
- smtplib
- pandas
- os
- dotenv

Usage:
- Make sure to have the 'birthdays.csv' file and 'letter_templates' directory in the
  same directory as this script.
- Store your email credentials in a .env file with 'my_email' and 'my_pass' variables.

"""

import datetime as dt
import random
import smtplib
import pandas
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
my_email = os.getenv("my_email")
my_pass = os.getenv("my_pass")

# Read birthday data from CSV file
with open("birthdays.csv") as file:
    data = pandas.read_csv(file)

# Get current date
now = dt.datetime.now()
now_tuple = (now.month, now.day)

# Create a dictionary of birthdays from the CSV data
birthday_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

# Check if there's a birthday today
if now_tuple in birthday_dict:
    birthday_person = birthday_dict[now_tuple]

    # Choose a random letter template
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    # Read and customize the letter content with the birthday person's name
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", birthday_person["name"])

    # Send a birthday email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{new_content}"
        )





