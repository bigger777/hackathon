import os


db_path = "sqlite:///" + os.path.join(basedir, 'db.sqlite')


class Config:
    DEBUG = True
    SECRET_KEY = "secret_key"
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
