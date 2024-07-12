import boto3
import time

from abc import ABC, abstractmethod
from typing import Dict, List

import src.env as envs

from src.util.converter import string_to_json
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


class QueueManagerBuilder:
    @staticmethod
    def build_real_implementation():
        return SQSQueueManager()

    @staticmethod
    def build_fake_implementation():
        return FakeQueueManager()


class QueueManager(ABC):
    def __init__(self):
        self.queue = envs.FORK_REPO_QUEUE_URL
        if not self.queue:
            raise ValueError("The environment variable FORK_REPO_QUEUE_URL should not be empty")
    
    @abstractmethod
    def receive_a_single_message(self) -> str: pass


class SQSQueueManager(QueueManager):
    def __init__(self):
        super().__init__()
        self.client = boto3.client('sqs', region_name = envs.AWS_REGION)

    def receive_a_single_message(self) -> Dict:
        messages = self.wait_until_receive_messages(max_messages = 1)
        message = messages[0]
        self.delete_message(receipt_handle = message['ReceiptHandle'])
        return string_to_json(message['Body'])

    def wait_until_receive_messages(self, max_messages: int = 1, time_to_wait_in_seconds: int = 20) -> List:
        while True:
            response = self.client.receive_message(
                QueueUrl = self.queue,
                AttributeNames = ['SentTimestamp'],
                MaxNumberOfMessages = max_messages,
                MessageAttributeNames = ['All'],
                VisibilityTimeout = 0,
                WaitTimeSeconds = time_to_wait_in_seconds  # higher value is necessary to avoid receiving too much empty messages
            )
            messages = response.get('Messages')
            if not messages:
                ''' Sometimes there is no message, so continue until receive one '''
                continue
            logger.debug(f'Received {messages =}')
            return messages

    def delete_message(self, receipt_handle: str) -> None:
        self.client.delete_message(
            QueueUrl = self.queue,
            ReceiptHandle = receipt_handle
        )


class FakeQueueManager(QueueManager):
    def __init__(self):
        super().__init__()
        self.is_first = True
        self.sleep_time_in_seconds = 60

    def receive_a_single_message(self) -> Dict:
        if self.is_first:
            self.is_first = False
            return self._get_fake_content()
        time.sleep(self.sleep_time_in_seconds)
        return self._get_fake_content()
    
    def _get_fake_content(self) -> Dict:
        return {
            'repo_url': 'https://github.com/gabrielrih/setrem-developer-testing.git'
        }
