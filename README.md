# Spatial Query APP

Example of a Flask App that retrieve data based in bbox build from 2 points,

It uses spatial functionality in the backend to return valid geojson that could be used to rendered on maps
or for different uses.

Data from OS OpenRoads will be served as example, but this example will work for any other layer for example buildings.

To make this portable data is just served for Leeds and surrounding areas.
Please, select your points inside this area.

REQUEST

For example you can output data in 4326, using as input you lat/lon points

GET /results/?x1=436139.8&y1=434547.0&x2=434141.2&y2=433689.0&srid=4326

Or you can input coordinates in any srid, just specified the query parameter srid
GET /results?x1=436139.8&y1=434547.0&x2=434141.2&y2=433689.0&srid=27700

## Using via form

The flask app has a form template that could be used to fill the coordinates

QUERY IN 27700 OUTPUT 4326 (Input Coordinates in 27700 but output in 4326)
#results?x1=436139.8&y1=434547.0&x2=434141.2&y2=433689.0&srid=4326

QUERY IN 4326 IN
#results?x1=-1.481803254286913&y1=53.79827838458832&x2=-1.481861940752835&y2=53.80416168334681&srid=4326

You can go to your prefer map and select two points inside Leeds Area and fill the form with the coordinates.
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

After running the above commands the flask server must be up and running

-Python: Create Environment

- Select your interpreter (Python 3.9 suits better)
- You will be asked to install the requirements txt file.
- You are ready to use the app. Run the server running the main.py file

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

```

```

```
