# Spatial Query APP

Example of a Flask App that retrieves data and get features by bbox built from 2 points,

It uses spatial functionality in the backend to return valid a geojson ready to be rendered on a map or for some post-processing analysis

Usefull when you need to display data based on the userviewport of an app, you get features based on the bbox of the user viewports.

Data from OS OpenRoads will be served as example, but this example will work for any other layer for example buildings.

To make this portable data is just served for Leeds and surrounding areas.
Please, select your points inside this area.

REQUEST

For example you can output data in 4326, using as input you lat/lon points

- GET /results/?x1=436139.8&y1=434547.0&x2=434141.2&y2=433689.0&srid=4326

Or you can input coordinates in any srid, just specified the query parameter srid

- GET /results?x1=436139.8&y1=434547.0&x2=434141.2&y2=433689.0&srid=27700

## Using via form

The flask app has a form template that could be used to fill the coordinates

Base URL: The one set by Flask usually http://127.0.0.1:5000

Fill form:

- Lon Point 1 : -1.48180325428691
- Lat Point 1 : 53.79827838458832
- Lon Point 2 : -1.481861940752835
- Lat Point 2 : 53.79827838458832
- srid : 4326

You can go to your prefered map and select two points inside Leeds Area and fill the form with the coordinates.
Input the srid of your input coordinates, by default is 4326.

To visualise the output, if you selected 4326, copy the geojson returned and paste in https://geojson.io/#map=2/0/20

You will see your vector features rendered on the area specified built by the two points

## Installation

If you are in LINUX there will be some problems with the spatialite extension.
For Windows the binaries for spatialite are setup to be integrated with the app at runtime

```bash
git clone <repo>
cd <repo location in your computer>
python -m virtualenv env
source source .venv/Scripts/activate
pip install -r requirements.txt
cd server
python main.py
```

## Tests

Some simple unit example are provided under the test folder it uses the pytest test framework

```bash
cd server
python -m  pytest --log-cli-level=INFO
```

## Usage

After running the above commands the flask server must be up and running.
Activate or install your env depends if you are in Linux or Windows.

You can also clone the repo open the folder in VSCode (if you have the python extension installed), and do the following

- Python: Create Environment
- Select venv
- Select your interpreter (Python 3.9 suits better)
- You will be asked to install the requirements txt file.
- You are ready to use the app. Run the server running the main.py file in server folder

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

```

```
