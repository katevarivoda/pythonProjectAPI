import json
import pytest
import requests
from api import endpoints
from api.endpoints import BASE_URL, HEADERS
from conftest import generate_random_user, generate_random_email, generate_new_unique_user, generate_random_id, \
    generate_random_gender, generate_random_status


@pytest.fixture
def user_to_update():
    return generate_new_unique_user().json()


def test_update_user(user_to_update):
    user_id = user_to_update["id"]
    url = f'{BASE_URL}/{user_id}'
    updated_name = generate_random_user()
    updated_email = generate_random_email()
    updated_gender = generate_random_gender()
    updated_status = generate_random_status()
    payload = json.dumps({
        "name": updated_name,
        "email": updated_email,
        "gender": updated_gender,
        "status": updated_status
    })
    response = requests.request("PUT", url, headers=HEADERS, data=payload)
    assert response.status_code == 200
    updated_user_data = response.json()
    assert updated_user_data["name"] == updated_name
    assert updated_user_data["email"] == updated_email
    assert updated_user_data["gender"] == updated_gender
    assert updated_user_data["status"] == updated_status


def test_partial_update_user(user_to_update):
    user_id = user_to_update["id"]
    url = f'{BASE_URL}/{user_id}'
    updated_name = generate_random_user()
    payload = json.dumps({
        "name": updated_name
    })
    response = requests.request("PUT", url, headers=HEADERS, data=payload)
    assert response.status_code == 200
    updated_user_data = response.json()
    assert updated_user_data["name"] == updated_name


def test_update_nonexistent_user():
    user_id = generate_random_id()
    url = f'{BASE_URL}/{user_id}'
    payload = {}
    response = requests.request("PUT", url, headers=HEADERS, data=payload)
    assert response.status_code == 404
