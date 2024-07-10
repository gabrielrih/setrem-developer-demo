from src.queue import FakeQueueManager
from src.repo import GitCloner, CompactorProxy
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


if __name__ == '__main__':
    queue = FakeQueueManager()
    cloner = GitCloner()
    while True:
        message: str = queue.receive_message()
        logger.info(f'Received {message =}')

        path: str = cloner.clone_repo(url = message)
        logger.info(f'Repository cloned on {path =}')

        compactor = CompactorProxy(path = path)
        output_file = compactor.compact()
        logger.info(f'The compacted file is {output_file}')

        # FIX IT
        # Send data to S3
        logger.info('Sending it to S3')
