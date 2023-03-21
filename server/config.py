import os

base_dir = os.path.abspath(os.getcwd())


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/server/db.sqlite"
    DEBUG = True
    FLASK_ENV = "development"


class ProdConfig(Config):
    # For production mode I suggest migrate the db to postgres
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{base_dir}/server/db.sqlite"
    FLASK_ENV = "production"


CONFIGURATION = {
    "default": DevConfig,
    "development": DevConfig,
    "production": ProdConfig
}
