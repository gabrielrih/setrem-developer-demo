from unittest import TestCase, mock

from src.bucket import (
    BucketManagerBuilder,
    S3BucketManager,
    FakeBucketManager
)


class TestBucketManagerBuilder(TestCase):
    def setUp(self):
        self.builder = BucketManagerBuilder()

    def test_build_real_implementation(self):
        bucket = self.builder.build_real_implementation()
        self.assertIsInstance(bucket, S3BucketManager)

    def test_buil_fake_implementation(self):
        bucket = self.builder.build_fake_implementation()
        self.assertIsInstance(bucket, FakeBucketManager)


class TestS3BucketManager(TestCase):
    def setUp(self):
        self.fake_source_path = '/tmp/fake-source-path'

    @mock.patch('boto3.client')
    def test_upload_file_when_success(self, mock_boto3_client):
        # Given
        mock_boto3_client.return_value = MockBoto3ClientForS3()

        # When
        bucket = S3BucketManager()
        bucket.upload_file(source_path = self.fake_source_path)

        # Then
        mock_boto3_client.is_called_once()


class MockBoto3ClientForS3:
    def upload_file(self, *_, **__) -> None:
        return None
