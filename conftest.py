import json
import string
from uuid import uuid4
import requests
import random
from api import endpoints


def generate_random_gender():
    gender_options = ["male", "female"]
    selected_gender = random.choice(gender_options)
    return selected_gender


def generate_random_status():
    status_options = ["active", "inactive"]
    selected_status = random.choice(status_options)
    return selected_status

def generate_random_email():
    domain = "@example.com"
    username_length = random.randint(5, 10)
    username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
    return username + domain


def generate_random_user():
    unique_last_name = f'User {str(uuid4())}'
    return unique_last_name


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_new_unique_user():
    url = endpoints.BASE_URL
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
    headers = endpoints.HEADERS
    response = requests.request("POST", url, headers=headers, data=payload)
    return response


def get_all_users():
    url = endpoints.BASE_URL
    response = requests.get(url)
    return response


def search_user_by_name(peoples, unique_last_name):
    return [person for person in peoples if person['name'] == unique_last_name]
