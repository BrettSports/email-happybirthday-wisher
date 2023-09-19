import smtplib
from datetime import datetime
import pandas as pd
import random

MY_EMAIL = "youremail@email.com"
PASSWORD = "admin_password" #Enter your password in the quotes, may need to generate an app password from your email client
HOST_STRING = "smtp.gmail.com" # Enter your smpt (e.g. Gmail's is "smtp.gmail.com"). You can find this online.

today = datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP(HOST_STRING) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}"
                            )





