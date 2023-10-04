import json
import requests
from api import endpoints
from conftest import (
    generate_random_user,
    generate_random_email,
    generate_random_status,
    generate_random_gender,
)


def test_error_on_nonexistent_endpoint():
    # Define the URL and payload
    url = endpoints.NON_EXISTENT_ENDPOINT
    unique_last_name = generate_random_user()
    random_email = generate_random_email()
    random_status = generate_random_status()
    random_gender = generate_random_gender()
    payload = json.dumps({
        "name": unique_last_name,
        "email": random_email,
        "gender": random_gender,
        "status": random_status
    })

    # Send the HTTP request
    headers = endpoints.HEADERS
    response = requests.post(url, headers=headers, data=payload)

    # Assert the response status code
    assert response.status_code == 404, f"Expected 404, but got {response.status_code}"
