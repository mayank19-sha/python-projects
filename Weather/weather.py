import requests

api_key="3e0f9cf849a03209450fc0d9e36fb1a7"

city=input("Enter city name: ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response=requests.get(url)

if response.status_code==200:
    data=response.json()
    temperature=data['main']['temp']
    humidity=data['main']['humidity']
    description=data['weather'][0]['description']
    
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather Description: {description}")
else:
    print("Error fetching weather data.")
