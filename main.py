import requests
import smtplib


MY_EMAIL ="tumbawakala@gmail.com"
PASSWORD ="kutd fhpy jdbe ygra"


api_key = "a674fa00336a2ef683c562ee1780b9d8"
END_POINT = "http://api.openweathermap.org/data/2.5/forecast"

LAT = 32.814018
LONG = -96.948891
CNT = 4

PARAMETERS = {
    "lat" : LAT,
    "lon" : LONG,
    "appid" : api_key,
    "cnt" : CNT,
    "units": "metric"
}
response = requests.get(url=END_POINT, params=PARAMETERS)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 800  :
        will_rain = True

if will_rain:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="ashraay.9@gmail.com",
                        msg="Subject:Weather info\n\n"
                            "Its going to rain so get ur umbrella ready")