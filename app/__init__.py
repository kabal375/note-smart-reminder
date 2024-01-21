from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.auth import controller as auth_controller
from app.auth import models as auth_models
from app.auth import views as auth_views
