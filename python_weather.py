import requests

api_key = 'bb2c404683921cdea62ce543bac5e976'


city = input("Enter a city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/"
                            f"data/2.5/weather?q={city}&appid={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = weather_data.json()['main']['temp']
converted_temp = (temp -273.15) * 9/5 + 32
rounded_temp = round(converted_temp, 1)

print(f"In {city}, the weather is {rounded_temp}°F with {weather} for the weather.") 