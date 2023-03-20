import pytest

from .cases import FORM_KEYS, FORM_VALUES, URL
from forms import BboxForm
from sql_template import ROADS_QUERY
from main import app
from models import *

@pytest.fixture
def client():
    
    app.config["WTF_CSRF_ENABLED"] = False
    with app.test_client() as client:
        yield client


def test_home(client):

    response = client.get("/")
    assert response.status_code == 200

    query_form = BboxForm()

    # Test if form keys needed for request exists
    for key in FORM_KEYS:
        assert key in query_form.data.keys()


def test_results(client):

    response = client.post("/", data=FORM_VALUES)

    # Test if you are redirected with the intended url
    assert response.location == URL
    

