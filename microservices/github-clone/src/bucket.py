import boto3

from botocore.exceptions import ClientError
from abc import ABC, abstractmethod

import src.env as envs

from src.util.logger import Logger


logger = Logger.get_logger(__name__)


class BucketManagerBuilder:
    @staticmethod
    def build_real_implementation():
        return S3BucketManager()
    
    @staticmethod
    def build_fake_implementation():
        return FakeBucketManager()


class BucketManager(ABC):
    def __init__(self):
        self.bucket_name = envs.S3_BUCKET_NAME
        if not self.bucket_name:
            raise ValueError('The environment variable S3_BUCKET_NAME should not be empty')

    @abstractmethod
    def upload_file(self, source_path: str, target_path: str) -> None: pass


class S3BucketManager(BucketManager):
    def __init__(self):
        super().__init__()
        self.client = boto3.client('s3', region_name = envs.AWS_REGION)

    def upload_file(self, source_path: str, target_path: str = '') -> None:
        if not target_path:
            target_path = source_path
        try:
            self.client.upload_file(
                source_path,
                self.bucket_name,
                target_path
            )
        except ClientError as e:
            logger.exception(e)


class FakeBucketManager(BucketManager):
    def __init__(self):
        super().__init__()

    def upload_file(self, *_, **__) -> None:
        return None
