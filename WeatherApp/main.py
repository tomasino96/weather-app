import datetime as dt
import requests #pip install requests(Windows)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
GEO_URL = "http://api.openweathermap.org/geo/1.0/direct?"
API_KEY = open('api_key', 'r').read()
CITY = "New York"

geo_url = GEO_URL + "q=" + CITY + "&appid=" + API_KEY
geo_response = requests.get(geo_url).json()

location_data = geo_response[0]

latitude = location_data['lat']
longitude = location_data['lon']

latitude_str = str(latitude)
longitude_str = str(longitude)

weather_url = BASE_URL + "lat=" + latitude_str + "&lon=" + longitude_str + "&appid=" + API_KEY
weather_response = requests.get(weather_url).json()

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

#print(geo_response) #geographical data
#print(weather_response) #weather data

temp_kelvin = weather_response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)

humidity = weather_response['main']['humidity']

timezone_offset = weather_response['timezone'] 
sunrise_unix = weather_response['sys']['sunrise']
sunset_unix = weather_response['sys']['sunset']

sunrise_utc = dt.datetime.fromtimestamp(sunrise_unix, tz=dt.timezone.utc)
sunset_utc = dt.datetime.fromtimestamp(sunset_unix, tz=dt.timezone.utc)

sunrise_time = sunrise_utc + dt.timedelta(seconds=timezone_offset)
sunset_time = sunset_utc + dt.timedelta(seconds=timezone_offset)

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C")
print(f"Humidity in {CITY} is: {humidity}%")
print(f"Sun rises in {CITY} at: {sunrise_time} local time")
print(f"Sun sets in {CITY} at: {sunset_time} local time")