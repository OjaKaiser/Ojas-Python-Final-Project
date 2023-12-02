import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
        """Set units to imperial or metric based on country if possible"""
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None
    
def display_weather(weather_data):
    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°F")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")


def suggest_outfit(weather_data):
    description = weather_data['weather'][0]['description'].lower()
    temperature = weather_data['main']['temp']

    
if __name__ == "__main__":
    api_key = "c9a340caa354b220f863dc4586383dc6"
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)