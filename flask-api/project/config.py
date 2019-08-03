import os 

class BaseConfig:
    """Base configuration"""
    SECRET_KEY = 'ShhuperSecreto!'
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


class DeveLocalDBConfig(BaseConfig):
    """Development configuration"""
    # get base directory where this file runs
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = 'comments.db'
    # define the full path for the database
    DATABASE_PATH = os.path.join(basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 


class TestingConfig(BaseConfig):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL') 


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
