import boto3
import json

from typing import Dict

import env as envs


class QueueManager:
    def __init__(self):
        self.sqs = boto3.client("sqs", region_name=envs.AWS_REGION)
        self.queue = envs.FORK_REPO_QUEUE_URL
        if not self.queue:
            raise ValueError("FORK_REPO_QUEUE_URL is empty")

    def send_message(self, data: Dict):
        response = self.sqs.send_message(
            QueueUrl = self.queue,
            MessageBody = json.dumps(data)
        )
        return response

