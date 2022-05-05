import requests
import os

from flask import request


def fetch_weather_data():
    api_key = os.getenv("Weather_API_key")
    lat = request.form.get("lat", default=None, type=float)
    lon = request.form.get("lon", default=None, type=float)
    print(lat, lon)

    if lat == None or lon == None:
        return "Invalid latitude or longitude", 400
    if lat > 90 or lat < -90:
        return "latitude should be between -90 to 90", 400
    if lon > 180 or lon < -180:
        return "longitude should be between -180 to 180", 400

    url = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}".format(
        lat=lat, lon=lon, API_key=api_key)

    resp = requests.get(url)
    return resp.json(), 200
