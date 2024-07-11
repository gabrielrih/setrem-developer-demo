from unittest import TestCase, mock

from src.bucket import (
    BucketManagerBuilder,
    S3BucketManager,
    FakeBucketManager
)


class TestBucketManagerBuilder(TestCase):
    def setUp(self):
        self.builder = BucketManagerBuilder()
        self.mock_bucket_name = mock.patch('src.bucket.envs.S3_BUCKET_NAME', return_value = 'fake_value')
        self.start_mocks()

    def start_mocks(self):
        self.mock_bucket_name.start()

    def tearDown(self):
        self.stop_mocks()

    def stop_mocks(self):
        self.mock_bucket_name.stop()

    def test_build_real_implementation(self):
        bucket = self.builder.build_real_implementation()
        self.assertIsInstance(bucket, S3BucketManager)

    def test_buil_fake_implementation(self):
        bucket = self.builder.build_fake_implementation()
        self.assertIsInstance(bucket, FakeBucketManager)


class TestS3BucketManager(TestCase):
    def setUp(self):
        self.fake_source_path = '/tmp/fake-source-path'
        self.mock_bucket_name = mock.patch('src.bucket.envs.S3_BUCKET_NAME', return_value = 'fake_value')
        self.start_mocks()

    def start_mocks(self):
        self.mock_bucket_name.start()

    def tearDown(self):
        self.stop_mocks()

    def stop_mocks(self):
        self.mock_bucket_name.stop()

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
