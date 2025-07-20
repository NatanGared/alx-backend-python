#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.org', return_value="https://api.github.com/orgs/google")
    def test_org(self, org_name, mock_org):
        github_client = GithubOrgClient()

        github_client.org(org_name)

        mock_org.assert_called_once_with(org_name)

if __name__ == '__main__':
    unittest.main()