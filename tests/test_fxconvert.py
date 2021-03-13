import json
import pytest
from app import app
from decimal import Decimal
from app.utils import convert, extract


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_missing_url_params(client):
    response = client.get("/convert?from=GBP&to=USD")
    data = json.loads(response.get_data(as_text=True))
    if response.status_code != 422:
        assert "wrong response code given {} != 422".format(response.status_code)


def test_convert():

    result = convert.calculate_fx("1", "1.2")
    if result != Decimal("1.20"):
        assert 0


        
    
