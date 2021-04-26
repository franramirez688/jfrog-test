import json
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', 'backend'))

import pytest

import app as backend_app


@pytest.fixture
def client():
    backend_app.app.config['TESTING'] = True

    with backend_app.app.test_client() as client:
        yield client


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/contacts')
    expected = json.dumps([
      {
        "id": 1,
        "name": "Leanne Graham",
        "username": "Bret",
        "email": "Sincere@april.biz",
        "address": {
          "street": "Kulas Light",
          "suite": "Apt. 556",
          "city": "Gwenborough",
          "zipcode": "92998-3874",
          "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
          }
        },
        "phone": "1-770-736-8031 x56442",
        "website": "hildegard.org",
        "company": {
          "name": "Romaguera-Crona",
          "catchPhrase": "Multi-layered client-server neural-net",
          "bs": "harness real-time e-markets"
        }
      }
    ])
    assert bytes(expected, 'utf-8') in rv.data
