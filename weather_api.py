# weather_api.py
import requests

API_KEY = "c3f76a7c5659fbf5127e530941b1bd9c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    print("Status Code:", response.status_code)  # Zugefügt für die Fehlersuche
    if response.status_code == 200:
        return response.json()
    else:
        print("Fehler API:", response.text)  # Fehlermeldung
        return None

