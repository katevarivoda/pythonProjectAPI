import json

import requests
from uuid import uuid4
from json import dumps

import random
import string

from assertpy import assert_that

from api import endpoints
from conftest import generate_random_user, generate_random_email, generate_new_unique_user


def test_delete_user():
    new_user = generate_new_unique_user()
    user_data = new_user.json()
    person_to_be_deleted = user_data["id"]
    url = f'{endpoints.BASE_URL}/{person_to_be_deleted}'
    payload = {}
    headers = endpoints.HEADERS
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 204



