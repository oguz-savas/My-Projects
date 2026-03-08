import requests
import datetime
import time

#1 URLs
response = "http://ip-api.com/json/"
#2 Requests
response = requests.get(response)
#3 Status Controls
response.raise_for_status()
#4 Json Parse
data = response.json()
#5 Getting Data
my_lat = data["lat"]
my_lon = data["lon"]

#6 Overhead Function
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lon = float(data["iss_position"]["longitude"])

    if (
        my_lat-5 <= iss_lat <= my_lat+5
        and my_lon-5 <= iss_lon <= my_lon+5
    ):
        return True
    else:
        return False
#7 Night Function
def is_night():
    params = {"lat": my_lat, "lng": my_lon}
    response = requests.get("https://api.sunrise-sunset.org/json", params=params)
    response.raise_for_status()
    data = response.json()

    sunset = data["results"]["sunset"]
    sunrise = data["results"]["sunrise"]
    c

    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    current_hour = datetime.datetime.now().hour

    if current_hour >= sunset_hour or current_hour <= sunrise_hour:
        return True
    else:
        return False
#8 While Loop
while True:
    if is_iss_overhead() and is_night():
        print("ISS is overhead")
    time.sleep(60)



















