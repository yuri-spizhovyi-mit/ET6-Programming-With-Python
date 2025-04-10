from base import APIClient


class WeatherClient(APIClient):
    def __init__(self, base_url, api_key):
        super().__init__(base_url)
        self.api_key = api_key

    def get_weather(self, city):
        path = "/data/2.5/weather"
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        return self.get(path, params)
