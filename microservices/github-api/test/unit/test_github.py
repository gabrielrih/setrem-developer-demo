from unittest import TestCase, mock
from typing import Dict

from src.github import (
    get_user,
    get_user_repos
)


class TestGitHub(TestCase):
    def setUp(self):
        self.expected_fake_response = {
            'key': 'value'
        }

    @mock.patch('requests.get')
    def test_get_user(self, mock_requests_get):
        # Given
        mock_requests_get.return_value = MockRequestsGetMethod(
            expected_response = self.expected_fake_response
        )

        # When
        response = get_user(username = 'fake-username')

        # Then
        mock_requests_get.assert_called()
        self.assertIsInstance(response, Dict)
        self.assertEqual(response, self.expected_fake_response)

    @mock.patch('requests.get')
    def test_get_user_repos(self, mock_requests_get):
        # Given
        mock_requests_get.return_value = MockRequestsGetMethod(
            expected_response = self.expected_fake_response
        )

        # When
        response = get_user_repos(username = 'fake-username')

        # Then
        mock_requests_get.assert_called()
        self.assertIsInstance(response, Dict)
        self.assertEqual(response, self.expected_fake_response)


class MockRequestsGetMethod:
    def __init__(self, expected_response: Dict = {}):
        self.expected_response = expected_response

    def json(self) -> Dict:
        return self.expected_response
        