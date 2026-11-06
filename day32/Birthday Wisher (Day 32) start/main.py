import datetime as dt
import random
import smtplib
myemail = "dhanyagctcse@gmail.com"


with open("quotes.txt") as txt:
    list =[]
    for line in txt.readlines():
        list.append(line)

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    quote = random.choice(list)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=myemail, password="iulp hqkt uulf nzzj")
        connection.sendmail(from_addr=myemail, to_addrs="dhanyagct@gmail.com",
                            msg=f"Subject:Hello\n\n{quote}")

