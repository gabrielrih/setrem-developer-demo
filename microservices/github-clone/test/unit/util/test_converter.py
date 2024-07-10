from unittest import TestCase

from src.util.converter import string_to_json, json_to_string


class TestConverter(TestCase):
    def test_string_to_json(self):
        # Given
        json_as_string = '{"key": "value"}'
        expected_output_as_json = {
            "key": "value"
        }
        
        # When
        output = string_to_json(json_as_string)

        # Then
        self.assertEqual(output, expected_output_as_json)

    def test_json_to_string(self):
        # Given
        input_as_dict = {
            'repo_url': "https://github.com/gabrielrih/MSSQL_Management_Queries.git"
        }
        expected_output = '{"repo_url": "https://github.com/gabrielrih/MSSQL_Management_Queries.git"}'

        # When
        output = json_to_string(input_as_dict)

        # Then
        self.assertIsInstance(output, str)
        self.assertEqual(output, expected_output)
