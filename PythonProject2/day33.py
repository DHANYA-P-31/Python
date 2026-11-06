import requests
from datetime import datetime
import smtplib

MY_LAT = 11.0212236
MY_LONG = 76.9353728

def overhead():
    responses = requests.get(url="http://api.open-notify.org/iss-now.json")
    responses.raise_for_status()

    longitude = float(responses.json()["iss_position"]["longitude"])
    Latitude = float(responses.json()["iss_position"]["latitude"])

    if MY_LAT-5 <= Latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5:
        return True
def night():
    parameters = {
        "lat": MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    Time = datetime.now().hour

    if Time>= sunset or Time<=sunrise:
        return True

if overhead() and night():
    connection = smtplib.SMTP("smtp.gmail.com")
    myemail = "dhanyagctcse@gmail.com"
    connection.login(user=myemail, password="iulp hqkt uulf nzzj")
    connection.sendmail(from_addr=myemail, to_addrs=myemail,
                        msg="Subject:Look up\n\nIss is above")