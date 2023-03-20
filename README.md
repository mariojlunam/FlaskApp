# Foobar

Example of a Flask App that retrieve data based in bbox build from 2 points,

It uses spatial functionality in the backend to return valid geojson that could be used to rendered on maps
or for different uses.

Usefull when you need to display data based on the userviewport of and app.

Data from OS OpenRoads will be served
To make this portable data is just served for Leeds and surrounding areas.
Please, select your points inside this area.

You can hit the api using the endpoints

QUERY IN 27700 OUTPUT 4326 (Input Coordinates in 27700 but output in 4326)
#results?x1=436139.8&y1=434547.0&x2=434141.2&y2=433689.0&srid=4326

QUERY IN 4326 IN
#results?x1=-1.481803254286913&y1=53.79827838458832&x2=-1.481861940752835&y2=53.80416168334681&srid=4326

Or use the the UI with the form

## Installation

If you are in LINUX there will be some problems with the spatialite extension.
For Windows the binaries for spatialite are setup to be integrated with the app at runtime

```bash
git clone <repo>
cd <repo location in your computer>
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

```

## Usage

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
```
