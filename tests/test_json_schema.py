import jsonschema
from jsonschema import validate
from referencing import jsonschema
from conftest import generate_random_user, generate_random_email, get_random_string

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "email": {"type": "string"},
        "gender": {"type": "string"},
        "status": {"type": "string"}
    },
    "required": ["name", "email", "gender", "status"],

}

name_validate = generate_random_user()
email_validate = generate_random_email()
gender_validate = get_random_string(10)
status_validate = get_random_string(5)


def test_valid_json_schema():
    try:
        validate(instance={"name": name_validate, "email": generate_random_email(), "gender": gender_validate,
                           "status": status_validate}, schema=schema)
        print("Schema is valid")

    except jsonschema.exceptions.ValidationError as ve:
        print("JSON data is invalid", ve)


# No error, the JSON is valid.

def test_invalid_type():
    try:
        validate(
            instance={"name": name_validate, "email": generate_random_email(), "gender": 1, "status": status_validate},
            schema=schema)
        print("Schema is valid")
    except jsonschema.exceptions.ValidationError as ve:
        print("JSON data is invalid", ve)


# ValidationError: 1 is not of type 'str' on instance 'gender'

def test_no_required_property():
    try:
        validate(instance={"name": name_validate, "gender": gender_validate, "status": status_validate}, schema=schema)
        print("Schema is valid")
    except jsonschema.exceptions.ValidationError as ve:
        print("JSON data is invalid", ve)

# ValidationError: 'email' is a required property