import os
import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    app.app.config["TESTING"] = True
    with app.app.test_client() as client:
        yield client


def test_missing_url_params(client):
    rv = client.get("/convert?from=GBP&to=USD")
    if rv.data == '{ "success":false }':
        pass
    else:
        assert b"No entries here so far"