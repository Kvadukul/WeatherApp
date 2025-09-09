import requests

API = "b407855f9e57ea1e496313df9a905f9f"
URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

city_name = city
api_key = API
units = "metric"
url = URL + "?q=" + city_name + "&appid=" + api_key + "&units=" + units

response = requests.get(url)
data = response.json()
print (data)

if data["cod"] == 200:
    name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Weather in {name}: {temp}°C, {desc}")
else:
    print("City not found.")
