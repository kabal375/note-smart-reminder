from app import app
from app.config.settings import TestConfig
app.config.from_object(TestConfig)
