from api.github import GitHubClient
from api.weather import WeatherClient

# GitHub API call
github = GitHubClient("https://api.github.com")
repos = github.get_user_repos("octocat")
for repo in repos[:3]:
    print("🔹", repo["name"])

# Weather API call (you need a real API key)
weather = WeatherClient("https://api.openweathermap.org", "YOUR_API_KEY")
forecast = weather.get_weather("London")
print("🌤️ Temp:", forecast["main"]["temp"], "°C")
