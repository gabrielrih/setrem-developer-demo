from unittest import TestCase, mock
from typing import List, Dict

from src.queue import (
    QueueManagerBuilder,
    SQSQueueManager,
    FakeQueueManager
)
from src.util.converter import json_to_string


class TestQueueManagerBuilder(TestCase):
    def setUp(self):
        self.builder = QueueManagerBuilder()
        self.mock_queue_url = mock.patch('src.queue.envs.FORK_REPO_QUEUE_URL', return_value = 'fake_value')
        self.start_mocks()

    def start_mocks(self):
        self.mock_queue_url.start()

    def tearDown(self):
        self.stop_mocks()

    def stop_mocks(self):
        self.mock_queue_url.stop()

    def test_build_real_implementation(self):
        bucket = self.builder.build_real_implementation()
        self.assertIsInstance(bucket, SQSQueueManager)

    def test_buil_fake_implementation(self):
        bucket = self.builder.build_fake_implementation()
        self.assertIsInstance(bucket, FakeQueueManager)


class TestSQSQueueManager(TestCase):
    def setUp(self):
        self.expected_body = {
            'repo_url': "https://github.com/gabrielrih/MSSQL_Management_Queries.git"
        }
        self.expected_messages = [
            {
                'MessageId': '911a7e0d-daf8-4cf3-81c1-6238730bdd1d',
                'ReceiptHandle': 'fake_handle',
                'MD5OfBody': 'cba17a8ea02baf24d74e8ef1fe4c5f5e',
                'Body': json_to_string(self.expected_body),
                'Attributes': {
                    'SentTimestamp': '1720633644920'
                }
            }
        ]
        self.mock_queue_url = mock.patch('src.queue.envs.FORK_REPO_QUEUE_URL', return_value = 'fake_value')
        self.start_mocks()

    def start_mocks(self):
        self.mock_queue_url.start()

    def tearDown(self):
        self.stop_mocks()

    def stop_mocks(self):
        self.mock_queue_url.stop()

    @mock.patch('src.queue.SQSQueueManager.delete_message')
    @mock.patch('src.queue.SQSQueueManager.wait_until_receive_messages')
    @mock.patch('boto3.client')
    def test_receive_a_single_message(self,
                                      mock_boto3_client,
                                      mock_wait_until_receive_messages,
                                      mock_delete_message):
        # Given
        mock_boto3_client.return_value = MockBoto3Client()
        mock_wait_until_receive_messages.return_value = self.expected_messages
        
        # When
        sqs = SQSQueueManager()
        message_body: Dict = sqs.receive_a_single_message()

        # Then
        mock_boto3_client.is_called_once()
        mock_wait_until_receive_messages.is_called_once()
        mock_delete_message.is_called_once()
        self.assertEqual(message_body, self.expected_body)


    @mock.patch('boto3.client')
    def test_wait_until_receive_messages(self, mock_boto3_client):
        # Given
        content_to_be_returned = {
            'Messages': self.expected_messages
        }
        mock_boto3_client.return_value = MockBoto3Client(
            content_to_be_returned = content_to_be_returned
        )
        
        # Given
        sqs = SQSQueueManager()
        messages: List[Dict] = sqs.wait_until_receive_messages()

        # Then
        mock_boto3_client.is_called_once()
        self.assertEqual(messages, self.expected_messages)

    @mock.patch('boto3.client')
    def test_delete_message(self, mock_boto3_client):
        # Given
        mock_boto3_client.return_value = MockBoto3Client()
        any_receipt_handle = 'any_receipt_handle'

        # When
        sqs = SQSQueueManager()
        sqs.delete_message(receipt_handle = any_receipt_handle)

        # Then
        mock_boto3_client.assert_called_once


class MockBoto3Client:
    def __init__(self, content_to_be_returned: List[Dict] = list()) -> None:
        self.content = content_to_be_returned

    def receive_message(self, *_, **__) -> Dict:
        return self.content
    
    def delete_message(self, *_, **__) -> None:
        return None
    