from unittest import TestCase, mock

from src.queue import QueueManager


class TestQueueManager(TestCase):
    def setUp(self):
        self.mock_repo_url = mock.patch('src.queue.envs.FORK_REPO_QUEUE_URL', return_value = 'fake_queue_url')
        self.start_mocks()

    def start_mocks(self):
        self.mock_repo_url.start()

    def tearDown(self):
        self.stop_mocks()

    def stop_mocks(self):
        self.mock_repo_url.stop()

    @mock.patch('boto3.client')
    def test_send_message(self, mock_boto3_client):
        # Given
        mock_boto3_client.return_value = MockBoto3SQSClient()

        # When
        queue = QueueManager()
        response = queue.send_message(data = 'fake_data')

        # Then
        mock_boto3_client.assert_called_once()
        self.assertIsNone(response)


class MockBoto3SQSClient:
    def send_message(*_, **__) -> None:
        return None