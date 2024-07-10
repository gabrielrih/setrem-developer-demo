#import boto3
#import json
import time

from abc import ABC, abstractmethod
from typing import Dict

import src.env as envs


class QueueManager(ABC):
    @abstractmethod
    def receive_message(self) -> str:
        pass


class FakeQueueManager(QueueManager):
    def __init__(self):
        self.is_first = True
        self.sleep_time_in_seconds = 60

    def receive_message(self) -> Dict:
        if self.is_first:
            self.is_first = False
            return self._get_fake_content()
        time.sleep(self.sleep_time_in_seconds)
        return self._get_fake_content()
    
    def _get_fake_content(self) -> str:
        return {
            'repo_url': 'https://github.com/gabrielrih/setrem-developer-testing.git'
        }


# class QueueManager:
#     def __init__(self):
#         self.sqs = boto3.client("sqs", region_name=envs.AWS_REGION)
#         self.queue = envs.FORK_REPO_QUEUE_URL
#         if not self.queue:
#             raise ValueError("FORK_REPO_QUEUE_URL is empty")

#     def send_message(self, data: Dict):
#         self.sqs.

#         response = self.sqs.send_message(
#             QueueUrl = self.queue,
#             MessageBody = json.dumps(data)
#         )
#         return response
