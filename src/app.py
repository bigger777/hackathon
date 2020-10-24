from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from views import *

if __name__ == "__main__":
    app.run()
