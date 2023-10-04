import pytest
import requests
from api import endpoints
from api.endpoints import HEADERS
from conftest import generate_random_id, generate_new_unique_user


@pytest.mark.delete
def test_delete_user():
    new_user = generate_new_unique_user()
    user_data = new_user.json()
    person_to_be_deleted = user_data["id"]
    url = f'{endpoints.BASE_URL}/{person_to_be_deleted}'
    payload = {}
    headers = endpoints.HEADERS
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 204


@pytest.mark.delete
def test_deleting_nonexistent_user():
    user_id = generate_random_id()
    url = f'{endpoints.BASE_URL}/{user_id}'
    payload = {}
    response = requests.request("DELETE", url, headers=HEADERS, data=payload)
    assert response.status_code == 404


@pytest.mark.delete
def test_delete_user_without_authorization():
    new_user = generate_new_unique_user()
    user_data = new_user.json()
    person_to_be_deleted = user_data["id"]
    url = f'{endpoints.BASE_URL}/{person_to_be_deleted}'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'}
    payload = {}
    response = requests.request("DELETE", url, headers=headers, data=payload)
    assert response.status_code == 404
