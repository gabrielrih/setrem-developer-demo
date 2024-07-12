from typing import Dict

from src.repo import GitCloner, CompactorProxy
from src.queue import QueueManagerBuilder
from src.bucket import BucketManagerBuilder
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


class Manager:
    def __init__(self, dry_run: bool = False):
        self.queue = QueueManagerBuilder.build_real_implementation()
        self.bucket = BucketManagerBuilder.build_real_implementation()
        if dry_run:
            self.queue = QueueManagerBuilder.build_fake_implementation()
            self.bucket = BucketManagerBuilder.build_fake_implementation()
        self.cloner = GitCloner()

    def receive_a_single_message(self) -> Dict:
        message: Dict = self.queue.receive_a_single_message()
        logger.info(f'Received message ={message}')
        return message

    def clone_repo(self, message: Dict) -> str:
        repo_url = message['repo_url']
        path: str = self.cloner.clone_repo(url = repo_url)
        logger.info(f'Repository cloned on {path =}')
        return path

    def compact_folder(self, path: str) -> str:
        compactor = CompactorProxy(path = path)
        output_file = compactor.compact()
        logger.info(f'The compacted file is {output_file}')
        return output_file

    def update_file_to_bucket(self, file_path: str) -> None:
        self.bucket.upload_file(source_path = file_path)
        logger.info('Uploaded to bucket!')
