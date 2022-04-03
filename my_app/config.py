"""Flask config class."""

import pathlib


class Config(object):
    DEBUG = False
    SECRET_KEY = "5krW6y3WCDo1FUsCr-F-Gg"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    database_file = pathlib.Path(__file__).parent.parent.joinpath("Data", "my_app.sqlite")
    SQLALCHEMY_DATABASE_URI =  'sqlite:///' + str(database_file)
    UPLOADED_PHOTOS_DEST = pathlib.Path(__file__).parent.joinpath("static/img")

class ProductionConfig(Config):
   pass

class DevelopmentConfig(Config):
    SQLALCHEMY_ECHO = True



class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_ECHO = True
