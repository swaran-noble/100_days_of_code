import requests
from datetime import datetime as dt
import smtplib
import time

# The details are fake. Please use your respective credentials
MY_EMAIL = "catchabreak617@gmail.com"
MY_PASSWORD = "wwxxcifrmgvnborv"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if abs(iss_longitude-MY_LONG)<=5 and abs(iss_latitude-MY_LAT)<=5:
        return True



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now()

    if time_now.hour >=sunset or time_now.hour<=sunrise:
        return True

while True:
    time.sleep(60) #To run the code every 60 seconds
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look Up\n\nThe ISS is above you in the sky"
            )




