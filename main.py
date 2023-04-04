import smtplib
import datetime as dt
import random
import pandas

PLACEHOLDER = "[NAME]"

my_email = "glebtus94@gmail.com"
my_password = "ffrineqpplbnkowc"

today = dt.datetime.now()
birthday_day = today.day
birthday_month = today.month

my_birthday = pandas.read_csv("birthdays.csv")
my_birthday_dict = my_birthday.to_dict(orient='records')

for _ in range(len(my_birthday_dict)):
    if my_birthday_dict[_]['month'] == birthday_month:
        if my_birthday_dict[_]['day'] == birthday_day:
            open_random_letter = random.randint(1, 3)
            name = my_birthday_dict[_]["name"]
            with open(f"letter_templates/letter_{open_random_letter}.txt") as letter_data:
                letter = letter_data.read()
            replaced_letter = letter.replace(PLACEHOLDER, name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=my_password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="ivascenko.gleb@gmail.com",
                    msg='Subject:Happy Birthday\n\n'
                        f'{replaced_letter}')
        else:
            print("No Birthdays today")



#_______________ANOTHER SOLUTION___________________
# today = dt.datetime.now()
# today_tuple = (today.month, today.day)
#
# data = pandas.read_csv('birthdays.csv')
#
# birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
#
# my_email = "glebtus94@gmail.com"
# my_password = "ffrineqpplbnkowc"
#
# if today_tuple in birthday_dict:
#     birthday_person = birthday_dict[today_tuple]
#     file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
#     with open(file_path) as letter_data:
#         contents = letter_data.read()
#         edited_contents = contents.replace("[NAME]", birthday_person["name"])
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=my_password)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs="ivascenko.gleb@gmail.com",
#             msg='Subject:Happy Birthday\n\n'
#                 f'{edited_contents}'
#         )

