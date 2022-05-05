from flask import Blueprint

from .controller import fetch_weather_data

weather_bp = Blueprint('weather_bp', __name__)

weather_bp.add_url_rule(
    rule='/weather', view_func=fetch_weather_data, methods=['GET'])
