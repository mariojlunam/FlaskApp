from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import CONFIGURATION

# Initialise the Database
db = SQLAlchemy()

def create_app(config_name):
    
    # App instance
    app = Flask(__name__)

    # configure app
    app.config.from_object(CONFIGURATION[config_name])
    
    # Initialise Extensions
    db.init_app(app)

    return app

