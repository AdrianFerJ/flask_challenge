import os 

class BaseConfig:
    """Base configuration"""
    # Flask config
    SECRET_KEY = 'ShhuperSecreto!'
    TESTING = False
    DEBUG = True
    # DB config
    SQLALCHEMY_TRACK_MODIFICATIONS = False 


class DevelopmentSqliteConfig(BaseConfig):
    """Development configuration"""
    # define the full path for the db (same lvl as this file)
    basedir = os.path.abspath(os.path.dirname(__file__))
    DATABASE = 'comments.db'
    DATABASE_PATH = os.path.join(basedir, DATABASE)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH


class DevelopmentMyqlConfig(BaseConfig):
    """Development configuration"""
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    # DB_NAME = os.environ['DB_DATABASE']
    # DB_USERNAME = os.environ['DB_USERNAME']
    # DB_PASSWORD = os.environ['DB_PASSWORD']
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ['DB_USERNAME'] \
        + ':' + os.environ['DB_PASSWORD'] + '@' + os.environ['DB_HOST'] \
        + ":3306/" + os.environ['DB_DATABASE']
    

class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + os.environ['DB_USERNAME'] \
        + ':' + os.environ['DB_PASSWORD'] + '@' + os.environ['DB_HOST'] \
        + ":3306/" + os.environ['DB_DATABASE']
