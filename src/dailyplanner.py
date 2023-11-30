import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }

     response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print(f"Error: Unable to fetch weather data. Status code: {response.status_code}")
        return None
    
if __name__ == "__main__":
    api_key = "c9a340caa354b220f863dc4586383dc6"
    city = input("Enter the city name: ")

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)