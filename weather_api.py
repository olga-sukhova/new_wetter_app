import requests
import os

API_KEY = os.environ.get('API_weather_app')
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    print("Status Code:", response.status_code)
    if response.status_code == 200:               # Überprüfung, ob die API-Antwort erfolgreich, HTTP-Statuscode 200 bedeutet "OK"
        return response.json()
    else:
        print("Fehler der API::", response.text)
        return None
