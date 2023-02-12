import pandas as pd
import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

proxy_client = TwilioHttpClient()
proxy_client.session.proxies = {'https': os.environ['https_proxy']}

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "627c2fdef557f1994747b53843488ee8" 
account_sid = ""
auth_token = ""

weather_param = {
    "lat" : 51.507351,
    "lon" : -0.127758,
    "appid" : api_key,
    "exclude" : "current,minutely,daily,alerts"
}

response = requests.get(OWM_Endpoint, params=weather_param)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Clinet(account_sid, auth_token, http_client = proxy_client)
    message = client.messages \
        .create(
            body = "It's going to rain today. Remember to bring an umbrella",
            from = "",
            to = "",
    )
    print(message.status)

    
# print(weather_slice)
# print(weather_data["hourly"][0]["weather"][0]["id"])
