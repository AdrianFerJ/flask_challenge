import os 

class BaseConfig:
    """Base configuration"""
    SECRET_KEY = 'ShhuperSecreto!'
    TESTING = False
    DEBUG = True
    USERNAME = 'admin'
    PASSWORD = 'admin'
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    # define the full path for the db (same lvl as this file)
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = 'comments.db'
    DATABASE_PATH = os.path.join(basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


class DockerDevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 


# class TestingConfig(BaseConfig):
#     """Testing configuration"""
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL') 


# class ProductionConfig(BaseConfig):
#     """Production configuration"""
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
