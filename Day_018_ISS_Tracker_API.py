import requests
from geopy.geocoders import Nominatim


#1 URL
url = 'http://api.open-notify.org/iss-now.json'

#2 Status Control
response = requests.get('http://api.open-notify.org/iss-now.json')
response.raise_for_status() # If getting error

#3 JSON Parse
data = response.json()

#4 Getting Data
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

print(f"ISS Location: {latitude}, {longitude}")
print(f"Latitude: {latitude}, Longitude: {longitude}")

#5 Getting Location Info

geolocator =Nominatim(user_agent ="gep_app")
location = geolocator.reverse(f"{latitude}, {longitude}")


if location and "country" in location.raw.get("address", {}):
    print("Country:", location.raw["address"]["country"])
else:
    print("ISS is over the ocean 🌊")





