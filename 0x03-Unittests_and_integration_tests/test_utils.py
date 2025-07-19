#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map  # Adjust the import based on your project structure

class TestAccessNestedMap(unittest.TestCase):

        @parameterized.expand([
                    ({"a": 1}, ("a",), 1),
                    ({"a": {"b": 2}}, ("a",), {"b": 2}),
                    ({"a": {"b": 2}}, ("a", "b"), 2),
                    ])
        def test_access_nested_map(self, nested_map, path, expected):
                    self.assertEqual(access_nested_map(nested_map, path), expected)
class TestAccessNestedMap(unittest.TestCase):

        @parameterized.expand([
                    ({}, ("a",), KeyError),
                    ({"a": 1}, ("a", "b"), KeyError)
        ])
        def test_access_nested_map_exception(self, nested_map, path, expected_exception):
                    with self.assertRaises(expected_exception) as context:
                        utils.access_nested_map(nested_map, path)
                    self.assertEqual(str(context.exception), "Key not found in nested map")


if __name__ == '__main__':
    unittest.main()
