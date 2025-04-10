import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path, params=None):
        url = f"{self.base_url}{path}"
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
