import requests

API = "b407855f9e57ea1e496313df9a905f9f"
URL = "https://api.openweathermap.org/data/2.5/weather"
ForecastURL = "https://api.openweathermap.org/data/2.5/forecast"

city = input("Enter city name: ")

city_name = city
api_key = API
units = "metric"
url = URL + "?q=" + city_name + "&appid=" + api_key + "&units=" + units

response = requests.get(url)
data = response.json()

if data["cod"] == 200:
    name = data["name"]
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    sea = data["main"]["sea_level"]
    wind = data["wind"]["speed"]
    print(f"Weather in {name}: {temp}°C, {desc}, Sea Level is {sea}, Wind Speed is {wind}m/s")
    
    option= input("Would you like to see the 5 day forecast?  (y/n) ").lower()
    if option == "y":
        forecast_url = ForecastURL + "?q=" + city_name + "&appid=" + api_key + "&units=" + units
        forecast_response = requests.get(forecast_url)
        forecast_data = forecast_response.json()

        if int(forecast_data["cod"]) == 200:
            print(f"\n5-Day Forecast for {name}:\n")
            for entry in forecast_data["list"]:
                if entry["dt_txt"].endswith("12:00:00"): 
                    date = entry["dt_txt"][:10]
                    temp = entry["main"]["temp"]   
                    print(f"{date}: {temp}°C")
                
                    




elif data["cod"] == 404:
    print("City not found.")
else:
    print ("Server Issue")
