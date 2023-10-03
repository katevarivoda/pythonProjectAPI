# api/client.py

import requests

class APIClient:
    def __init__(self):
        self.session = requests.Session()

    def get(self, url):
        return self.session.get(url)

    def post(self, url, data):
        return self.session.post(url, json=data)

    # Implement other HTTP methods as needed
