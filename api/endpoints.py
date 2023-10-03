# api/endpoints.py

BASE_URL = "https://gorest.co.in/public/v2/users"
ACCESS_TOKEN = "6f7202fbca5b0f9a29cbc01f0169a86735f29038f0d4bbd6599abc405ab9b8dc"
HEADERS = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer 6f7202fbca5b0f9a29cbc01f0169a86735f29038f0d4bbd6599abc405ab9b8dc'
    }



class Endpoints:
    USERS = f"{BASE_URL}/users"
    POSTS = f"{BASE_URL}/posts"
    # Add more endpoints as needed
