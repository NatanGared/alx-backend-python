class GithubOrgClient:
    def __init__(self):
        self.base_url = "https://api.github.com"

    def get_json(self, url):
        # Simulated method to fetch JSON data from a URL
        pass

    def org(self, org_name):
        url = f"{self.base_url}/orgs/{org_name}"
        return self.get_json(url)