from typing import List, Dict

from src.queue import FakeQueueManager, SQSQueueManager
from src.repo import GitCloner, CompactorProxy
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


if __name__ == '__main__':
    #queue = FakeQueueManager()
    queue = SQSQueueManager()
    cloner = GitCloner()
    logger.info('Waiting for messages...')
    while True:
        message: Dict = queue.receive_a_single_message()
        logger.info(f'Received message ={message}')
        path: str = cloner.clone_repo(url = message['repo_url'])
        logger.info(f'Repository cloned on {path =}')
        compactor = CompactorProxy(path = path)
        output_file = compactor.compact()
        logger.info(f'The compacted file is {output_file}')

        # # FIX IT
        # # Send data to S3
        # logger.info('Sending it to S3')
