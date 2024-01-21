from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import views, models, controllers
