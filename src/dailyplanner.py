import requests

def get_weather(api_key, city):
    base_url = ""
    params = {
        "q": city,
        "appid": api_key,
        "units": "imperial"
    }