import requests

API_KEY = "b407855f9e57ea1e496313df9a905f9f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Weather in {name}: {temp}°C, {desc}")
else:
    print("City not found.")