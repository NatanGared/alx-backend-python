#!/usr/bin/env python3
import unittest
from unittest import TestCase
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        github_client = GithubOrgClient()

        github_client.org(org_name)

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

if __name__ == '__main__':
    unittest.main()