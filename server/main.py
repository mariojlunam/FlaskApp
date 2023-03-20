import os
import json

from flask import request, render_template, jsonify, url_for, redirect
from sqlalchemy import event
from dotenv import load_dotenv

from core import create_app
from forms import BboxForm
from models import *
from helper import build_geojson
from sql_template import ROADS_QUERY

load_dotenv()
    
# Spatialite path to add spatial functionalities to sqlite
spatialite_path = os.getenv("SPATIALITE_PATH")
os.environ["PATH"] = f"{spatialite_path};{os.environ['PATH']}"

# create server instance from app factory
app = create_app("default")

# add extension spatialite to sqlite3
with app.app_context():
    @event.listens_for(db.engine, "connect")
    def load_spatialite(dbapi_conn, connection_record):
        dbapi_conn.enable_load_extension(True)
        dbapi_conn.load_extension("mod_spatialite")

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found, please see list of current routes"


@app.route("/", methods=["POST", "GET"])
def query_data():

    # Instance the BboxForm class
    query_form = BboxForm()
    
    if request.method == "POST" and query_form.validate():
        lon1 = query_form.x1.data
        lat1 = query_form.y1.data
        lon2 = query_form.x2.data
        lat2 = query_form.y2.data
        srid = query_form.srid.data

        # Redirect to results if form is validated
        return redirect(url_for("results", x1=lon1, y1=lat1, x2=lon2, y2=lat2, srid=srid))
    else:
        return render_template("query.html", title="Query", form=query_form)


@app.route("/results", methods=["GET"])
def results():

    # Query Parameters from url request
    lon1 = request.args.get("x1", type=float)
    lat1 = request.args.get("y1", type=float)
    lon2 = request.args.get("x2", type=float)
    lat2 = request.args.get("y2", type=float)

    # In case all coordinates haven't been provided
    if None in [lon1, lat1, lon2, lat2]:
        return "Not coordinates provided, please check your parameters"

    # For srid since args is a dict we can specify the default value if a KeyError occurs
    srid_coords = request.args.get("srid", 4326, type=int)

    # Always use parameters binding instead of string literal to prevent SQL INJECTION
    QUERY = ROADS_QUERY.bindparams(
        x1=lon1, y1=lat1, x2=lon2, y2=lat2, srid=srid_coords)

    results = db.session.execute(QUERY)

    # From query sanitise output to build geojson
    values = [(json.loads(row.geom), json.loads(row.props)) for row in results]

    # Build features collection
    geojson = {"type": "FeatureCollection",
               "features": list(map(build_geojson, values))}

    # Return a valid geojson, jsonify add 'application/json' header for the response
    return jsonify(geojson)


if __name__ == "__main__":
    app.run(debug=True)
