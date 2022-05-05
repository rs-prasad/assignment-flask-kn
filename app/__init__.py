import os
from dotenv import load_dotenv
from flask import Flask
# blue print imports
from .weather.routes import weather_bp

load_dotenv()  # loads env variables

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['FLASK_EVN'] = os.getenv("FLASK_ENV")


app.register_blueprint(weather_bp)
