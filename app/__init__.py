import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv()  # loads env variables

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['FLASK_EVN'] = os.getenv("FLASK_ENV")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")

db = SQLAlchemy(app)

# blue print imports
from .weather.routes import weather_bp
from .posts.routes import posts_bp

#db.create_all()
app.register_blueprint(weather_bp)
app.register_blueprint(posts_bp)
