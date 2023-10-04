import json

import pytest
import requests

from api import endpoints
from api.endpoints import HEADERS, BASE_URL
from conftest import generate_random_user, generate_random_email, generate_random_status, \
    generate_random_gender, get_random_string


@pytest.fixture
def valid_user_data():
    unique_last_name = generate_random_user()
    random_email = generate_random_email()
    random_gender = generate_random_gender()
    random_status = generate_random_status()
    return {
        "name": unique_last_name,
        "email": random_email,
        "gender": random_gender,
        "status": random_status,
    }


@pytest.fixture
def invalid_user_data():
    unique_last_name = generate_random_user()
    random_email = generate_random_email()
    random_gender = get_random_string(5)
    random_status = generate_random_status()
    return {
        "name": unique_last_name,
        "email": random_email,
        "gender": random_gender,
        "status": random_status,
    }


@pytest.mark.smoke
def test_add_new_unique_user(valid_user_data):
    payload = json.dumps(valid_user_data)
    response = requests.request("POST", BASE_URL, headers=HEADERS, data=payload)
    created_user_data = response.json()
    assert response.status_code == 201
    assert created_user_data["name"] == valid_user_data["name"]
    assert created_user_data["email"] == valid_user_data["email"]
    assert created_user_data["gender"] == valid_user_data["gender"]
    assert created_user_data["status"] == valid_user_data["status"]
def test_adding_new_user_with_valid_parameters(valid_user_data):
    payload = json.dumps(valid_user_data)
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 201


def test_adding_user_with_invalid_parameters(invalid_user_data):
    payload = json.dumps(invalid_user_data)
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 422


def test_status_code_on_empty_submission():
    payload = {}
    response = requests.post(BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 422




def test_status_code_on_empty_submission():
    payload = {}
    response = requests.request("POST", BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 422


def test_endpoint_error_on_empty_submission():
    payload = {}
    headers = endpoints.HEADERS
    response = requests.post(BASE_URL, headers=headers, data=payload)
    assert response.status_code == 422
    expected_errors = [
        {"field": "email", "message": "can't be blank"},
        {"field": "name", "message": "can't be blank"},
        {"field": "gender", "message": "can't be blank, can be male of female"},
        {"field": "status", "message": "can't be blank"},
    ]
    assert response.json() == expected_errors

