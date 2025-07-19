import unittest
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        # Create an instance of GithubOrgClient
        github_client = GithubOrgClient()

        # Call the org method
        github_client.org(org_name)

        # Assert that get_json was called once with the expected URL
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

if __name__ == '__main__':
    unittest.main()