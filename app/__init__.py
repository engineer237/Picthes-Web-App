import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevConfig, ProdConfig
from flask_migrate import Migrate
from flask_login import LoginManager

# instance of the application
app = Flask(__name__)

# dev configurations
app.config.from_object(DevConfig)
app.config['SECRET_KEY'] = '6e5591dabc255f7d'

# Database configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://moringa:blog@localhost/pitches'
# = 'postgresql+psycopg2://moringa:blog@localhost/pitches'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)
print(app.config['SQLALCHEMY_DATABASE_URI'])
# loggin configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import views