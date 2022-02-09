import os
class Config:
    pass
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
     #'postgresql+psycopg2://moringa:blog@localhost/pitches'
class DevConfig(Config):
    DEBUG = True
    # 'postgresql+psycopg2://moringa:blog@localhost:5433/pitches'