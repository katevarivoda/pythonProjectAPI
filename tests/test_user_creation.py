import json

import requests

from api import endpoints
from conftest import generate_new_unique_user, generate_random_user, generate_random_email, generate_random_status, generate_random_gender


def test_add_new_unique_user():
    url = endpoints.BASE_URL
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
    headers = endpoints.HEADERS
    response = requests.request("POST", url, headers=headers, data=payload)
    data = response.json()
    created_user_name = data.get("name")
    created_user_email = data.get("email")
    created_user_status = data.get("status")
    created_user_gender = data.get("gender")
    assert created_user_name == unique_last_name
    assert created_user_email == random_email
    assert created_user_gender == random_gender
    assert created_user_status == random_status


def test_status_code_on_empty_submission():
    url = endpoints.BASE_URL
    payload = {}
    headers = endpoints.HEADERS
    response = requests.request("POST", url, headers=headers, data=payload)
    assert response.status_code == 422


def test_endpoint_error_on_empty_submission():
    url = endpoints.BASE_URL
    payload = {}
    headers = endpoints.HEADERS
    response = requests.request("POST", url, headers=headers, data=payload)
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
