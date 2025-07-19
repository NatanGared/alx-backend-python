#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from test_utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
