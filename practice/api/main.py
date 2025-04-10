from github import GitHubClient
from dotenv import load_dotenv
import os
from weather import WeatherClient

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")

# GitHub API call
github = GitHubClient("https://api.github.com")
repos = github.get_user_repos("octocat")
for repo in repos[:3]:
    print("🔹", repo["name"])

weather = WeatherClient("https://api.openweathermap.org", API_KEY)
forecast = weather.get_weather("London")

print("🌤️ Weather in London:")
print("Temperature:", forecast["main"]["temp"], "°C")
print("Condition:", forecast["weather"][0]["description"])
