from flask import Flask
from models import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from views import *

if __name__ == "__main__":
    app.run("0.0.0.0", 8000)
