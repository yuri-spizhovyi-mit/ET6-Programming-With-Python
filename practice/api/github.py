from base import APIClient


class GitHubClient(APIClient):
    def get_user_repos(self, username):
        path = f"/users/{username}/repos"
        return self.get(path)
