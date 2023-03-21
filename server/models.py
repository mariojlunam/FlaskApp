from core import db
from geoalchemy2 import Geometry

# Base class


class Base:

    id = db.Column(db.Integer, primary_key=True, nullable=False)


class Roads(db.Model):
    """
    Generates db model for our Roads table

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=False)
    roadclassification = db.Column(db.String(22), unique=False, nullable=True)
    roadfunction = db.Column(db.String(30), unique=False, nullable=True)
    length = db.Column(db.Float, unique=False, nullable=False)
    geom = db.Column(Geometry("LINESTRING", management=True, srid=27700))
