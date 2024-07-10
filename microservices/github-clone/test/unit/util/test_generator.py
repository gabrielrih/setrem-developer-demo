from unittest import TestCase

from src.util.generator import generate_random_string


class TestStandaloneMethods(TestCase):
    def test_get_random_string(self):
        # Given
        lenght = 8

        # When
        string = generate_random_string(length = lenght)

        # Then
        self.assertEqual(len(string), lenght)
        self.assertIsInstance(string, str)
        self.assertIsNotNone(string)
