import os

postgres_local_base = "postgresql://postgres:root@localhost:5432/BoopIt"

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "bof")
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/BoopIt"
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/BoopTest"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "postgres://rqttytvqezhguw:9b0a6d99f6aafd459fdc4f21e665e03a8bd16ac5b325da74a84ba0651d8965dc@ec2-3-224-165-85.compute-1.amazonaws.com:5432/dco07qasdmjsul"

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
key = Config.SECRET_KEY

