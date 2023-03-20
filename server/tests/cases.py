
# Values Keys from form, if the form changed just a the new key to be tested
FORM_KEYS = ["x1", "x2", "y1", "y2", "srid", "submit"]

# Form values to populate objects 4326 srid
FORM_VALUES = {"x1": -1.481803254286913, 
               "y1": 53.79827838458832,
               "x2": -1.5433470259011415, 
               "y2": 53.788049310372685, 
               "srid": 4326,
               "submit": True}

# URL to be redirected after POST form
URL = "/results?x1=-1.481803254286913&y1=53.79827838458832&x2=-1.5433470259011415&y2=53.788049310372685&srid=4326"