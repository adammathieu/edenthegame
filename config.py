import os
basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

class Config(object):
    DEBUG = False
    TESTING = False
    POSTGRES_URL = get_env_variable("FLASK_POSTGRES_URL")
    POSTGRES_USER = get_env_variable("FLASK_POSTGRES_USER")
    POSTGRES_PW = get_env_variable("FLASK_POSTGRES_PW")
    POSTGRES_DB = get_env_variable("FLASK_POSTGRES_DB")
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']+POSTGRES_USER+':'+POSTGRES_PW+'@'+POSTGRES_URL+'/'+POSTGRES_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
