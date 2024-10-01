import sys
import os
import json
import pytest

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"People List" in response.data

def test_json_data():
    with open('app/data.json', 'r') as file:
        data = json.load(file)
    assert isinstance(data, list)
    assert all('name' in person and 'linkedin' in person for person in data)