from typing import Dict

import src.env as envs

from src.manager import Manager
from src.util.logger import Logger


logger = Logger.get_logger(__name__)


if __name__ == '__main__':
    manager = Manager(dry_run = envs.DRY_RUN)
    logger.info('Waiting for messages...')
    while True:
        message: Dict = manager.receive_a_single_message()
        path: str = manager.clone_repo(message = message)        
        file_path: str = manager.compact_folder(path)
        manager.update_file_to_bucket(file_path = file_path)
