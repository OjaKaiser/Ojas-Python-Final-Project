import requests

def get_weather(api_key, city):
    base_url = "waiting for account to activate"
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