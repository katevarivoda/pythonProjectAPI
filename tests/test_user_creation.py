import json

import requests

from api import endpoints
from api.endpoints import HEADERS, BASE_URL
from conftest import generate_random_user, generate_random_email, generate_random_status, \
    generate_random_gender, get_random_string


def test_add_new_unique_user():
    unique_last_name = generate_random_user()
    random_email = generate_random_email()
    random_gender = generate_random_gender()
    random_status = generate_random_status()
    payload = json.dumps({

        "name": unique_last_name,
        "email": random_email,
        "gender": random_gender,
        "status": random_status
    })

    response = requests.request("POST", BASE_URL, headers=HEADERS, data=payload)
    created_user_data = response.json()
    assert created_user_data["name"] == unique_last_name
    assert created_user_data["email"] == random_email
    assert created_user_data["gender"] == random_gender
    assert created_user_data["status"] == random_status


def test_adding_user_with_invalid_parameters():
    unique_last_name = generate_random_user()
    random_email = generate_random_email()
    random_gender = get_random_string(5)
    random_status = generate_random_status()
    payload = json.dumps({

        "name": unique_last_name,
        "email": random_email,
        "gender": random_gender,
        "status": random_status
    })
    response = requests.request("POST", BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 422


def test_adding_user_with_empty_parameter():
    unique_last_name = generate_random_user()
    random_email = generate_random_email()
    random_status = generate_random_status()
    payload = json.dumps({

        "name": unique_last_name,
        "email": random_email,
        "status": random_status
    })
    response = requests.request("POST", BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 422


def test_status_code_on_empty_submission():
    payload = {}
    response = requests.request("POST", BASE_URL, headers=HEADERS, data=payload)
    assert response.status_code == 422


def test_endpoint_error_on_empty_submission():
    payload = {}
    headers = endpoints.HEADERS
    response = requests.request("POST", BASE_URL, headers=headers, data=payload)
    assert response.json() == [
        {
            "field": "email",
            "message": "can't be blank"
        },
        {
            "field": "name",
            "message": "can't be blank"
        },
        {
            "field": "gender",
            "message": "can't be blank, can be male of female"
        },
        {
            "field": "status",
            "message": "can't be blank"
        }
    ]
