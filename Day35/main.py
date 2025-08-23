import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("TWILIO_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters={
    "lat": 51.507351,
    "lon": -0.127758,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+16812401900",
        to="+919515727375",
    )
    print(message.status)



