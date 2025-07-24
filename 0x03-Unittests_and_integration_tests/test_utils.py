#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

class TestAccessNestedMapExceptions(unittest.TestCase):

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), TypeError)
    ])
    def access_nested_map(nested_map, path):
        current = nested_map
        for key in path:
            if not isinstance(current, dict):
                raise TypeError(f"Expected dictionary at key '{key}'")
            if key not in current:
                raise KeyError(f"Key '{key}' not found")
            current = current[key]
        return current
'''
class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_json = Mock(return_value=test_payload)
        mock_get.return_value.json = mock_json

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch the a_method to track calls
        with patch.object(test_instance, 'a_method') as mock_method:
            mock_method.return_value = 42  # Set the return value

            # First call to a_property - should call a_method
            result1 = test_instance.a_property()
            self.assertEqual(result1, 42)

            # Second call to a_property - should use cached result
            result2 = test_instance.a_property()
            self.assertEqual(result2, 42)

            # Verify a_method was called only once
            mock_method.assert_called_once()
'''
if __name__ == '__main__':
    unittest.main()