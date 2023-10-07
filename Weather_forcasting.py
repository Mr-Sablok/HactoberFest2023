import requests

def get_weather(api_key, city, country):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': f'{city},{country}',
        'appid': api_key,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']

        print(f"Weather in {city}, {country}: {weather_description}")
        print(f"Temperature: {temperature}°C, Humidity: {humidity}%")
    else:
        print(f"Failed to retrieve weather data. Error: {data['message']}")

if __name__ == "__main__":
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    city = input("Enter city: ")
    country = input("Enter country code (e.g., US): ")

    get_weather(api_key, city, country)
