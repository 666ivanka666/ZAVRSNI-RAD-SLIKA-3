from pickle import FALSE, TRUE
from urllib import request
import requests
import json

from datetime_utils import formatted_date, formatted_time

class WeatherForecast:
    def __init__(self, city):
        self.url = f"https://weatherdbi.herokuapp.com/data/weather/{city}"
        self.fallbackurl = f"https://api.open-meteo.com/v1/forecast?latitude=45.79&longitude=15.96&current_weather=true&hourly=relativehumidity_2m"
        self.isusingfallback = FALSE
        self.data = None
        self.send_request()

    def send_request(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = json.loads(response.text)
        else:
            self.isusingfallback = TRUE
            response = requests.get(self.fallbackurl)
            self.data = json.loads(response.text)

    def get_formatted_weather_data(self):
        if self.isusingfallback and self.isusingfallback == TRUE:
            return {
                "location": "Zagreb",
                "current_temperature": self.data["current_weather"]["temperature"],
                "humidity": self.data["hourly"]["relativehumidity_2m"][0],
                "description": "Fallback API - no desc",
                "last_refresh": f"{formatted_date()} {formatted_time()}"
            }
        else:
            return {
                "location": self.data["region"],
                "current_temperature": self.data["currentConditions"]["temp"]["c"],
                "humidity": self.data["currentConditions"]["humidity"],
                "description": self.data["currentConditions"]["comment"],
                "last_refresh": f"{formatted_date()} {formatted_time()}"
            }
