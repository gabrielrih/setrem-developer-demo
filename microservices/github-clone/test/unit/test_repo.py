import os
from unittest import TestCase

from src.repo import (
    GitCloner,
    CompactorProxy
)


class TestClone(TestCase):
    def setUp(self):
        self.expected_path_prefix = '/tmp'
        self.cloner = GitCloner(base_path = self.expected_path_prefix)
        self.public_repo_url = 'https://github.com/gabrielrih/MSSQL_Management_Queries.git'

    def test_get_path(self):
        # When
        path = self.cloner.get_new_path()
        self.assertIsInstance(path, str)
        self.assertIsNotNone(path)
        self.assertTrue(self.is_string_contains_substring(
            string = path,
            substring = self.expected_path_prefix
        ))

    @staticmethod
    def is_string_contains_substring(string: str, substring: str) -> bool:
        if substring in string:
            return True
        return False
    
    def test_clone_repo(self):
        # When
        path = self.cloner.clone_repo(url = self.public_repo_url)

        # Then
        self.assertTrue(
            self.is_folder_exists(path),
            msg = 'The repo should be cloned on {path}, but it was not'
        )
        self.assertTrue(
            self.does_the_folder_have_content(path),
            msg = 'The {path} should have content from the cloned repo, but it have not'
        )

    @staticmethod
    def is_folder_exists(path: str) -> bool:
        return os.path.exists(path)

    @staticmethod
    def does_the_folder_have_content(path: str) -> bool:
        items_in_folder = os.listdir(path)
        if not items_in_folder:
            return False
        return True


class TestCompactorProxy(TestCase):
    def setUp(self):
        self.folder = self.create_empty_folder()
        self.compactor = CompactorProxy(path = self.folder)

    def create_empty_folder(self) -> str:
        path = '/tmp/oqkkkkuqod'
        if os.path.exists(path):
            return path
        os.mkdir(path)
        return path
    
    def test_compact(self):
        # Given
        expected_output_file = f'{self.folder}.zip'

        # When
        output_file = self.compactor.compact()

        # Then
        self.assertIsInstance(output_file, str)
        self.assertEqual(output_file, expected_output_file)
        self.assertTrue(
            self.is_file_exists(path = output_file),
            msg = f'The {output_file =} should exist but it does not exists'
        )

    @staticmethod
    def is_file_exists(path: str) -> bool:
        return os.path.exists(path)
