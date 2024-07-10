import shutil

from abc import ABC, abstractmethod
from git import Repo

from .util.generator import generate_random_string


class GitCloner:
    def __init__(self, base_path: str = '/tmp'):
        self.base_path = base_path

    def clone_repo(self, url: str) -> str:
        to_path = self.get_new_path()
        Repo.clone_from(
            url = url,
            to_path = to_path
        )
        return to_path
    
    def get_new_path(self) -> str:
        path = f'{self.base_path}/{generate_random_string()}'
        return path


class CompactorProxy:
    def __init__(self, path: str):
        self.path = path
        self.compactor = CompactorUsingShutil(path)

    def compact(self) -> str:
        return self.compactor.compact()


class Compactor(ABC):
    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def compact(self) -> str: pass


class CompactorUsingShutil(Compactor):
    def __init__(self, path: str):
        super().__init__(path)
        self.extension = 'zip'

    def compact(self) -> str:
        shutil.make_archive(self.path, self.extension, self.path)
        output_file = f'{self.path}.{self.extension}'
        return output_file
