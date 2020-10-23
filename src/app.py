from flask import Flask
from models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from views import *
