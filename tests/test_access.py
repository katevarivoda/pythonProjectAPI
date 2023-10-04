import requests

from api.endpoints import BASE_URL, HEADERS
from conftest import generate_invalid_token


def test_authorized_access():
    response = requests.request("GET", BASE_URL, headers=HEADERS)
    assert response.status_code == 200, f"Expected 200 OK, but got {response.status_code}"


def test_unauthorized_access_invalid_token():
    invalid_token = generate_invalid_token(20)
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f"Bearer {invalid_token}"
    }
    response = requests.get(BASE_URL, headers=headers)
    assert response.status_code == 401, f"Expected 401 Unauthorized, but got {response.status_code}"
