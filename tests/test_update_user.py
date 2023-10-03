import json
import requests
from api import endpoints
from conftest import generate_random_user, generate_random_email, generate_new_unique_user


def test_update_user():
    new_user = generate_new_unique_user()
    user_data = new_user.json()
    person_to_be_updated = user_data["id"]
    url = f'{endpoints.BASE_URL}/{person_to_be_updated}'
    updated_name = generate_random_user()
    payload = json.dumps({
        "name": updated_name
    })
    headers = endpoints.HEADERS
    response = requests.request("PUT", url, headers=headers, data=payload)
    assert response.status_code == 200
    data = response.json()
    updated_user_name = data.get("name")
    assert updated_user_name == updated_name
