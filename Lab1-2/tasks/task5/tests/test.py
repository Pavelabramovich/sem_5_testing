from unittest import TestCase
from unittest import main as unittest_main

from tasks.task5.parse_files import main as test_main
from test_tools import ArgparseTestCaseMixin
from pathlib import Path

from os.path import exists as file_exists, isdir as directory_exists
from os import remove as file_delete, mkdir as create_directory
from shutil import rmtree as delete_directory
import os
from main_decorator import main


class TestParseFiles(ArgparseTestCaseMixin, TestCase):
    TEST_DIR = Path(__file__).resolve().parent / 'test_dir'

    @classmethod
    def get_output_lines(cls, *args):
        with super().get_output_lines(*args) as output_lines:
            test_main()

        return output_lines

    def setUp(self):
        if not directory_exists(self.TEST_DIR):
            create_directory(self.TEST_DIR)

        extensions = ['txt', 'json', 'xml']

        for i in range(3):
            dir_path = self.TEST_DIR / f'dir{i}'
            create_directory(dir_path)

            for j in range(3):
                with open(dir_path / f'file{j}{os.extsep}{extensions[j]}', "w+") as file:
                    file.write("123")

    def tearDown(self):
        delete_directory(self.TEST_DIR)

    def test_normal(self):
        expected_res = [str(self.TEST_DIR / f'dir{i}' / 'file0.txt') for i in range(3)]
        res = self.get_output_lines(str(self.TEST_DIR), ".txt")

        self.assertSequenceEqual(res, expected_res)

    def test_no_dot_extension(self):
        expected_res = [str(self.TEST_DIR / f'dir{i}' / 'file1.json') for i in range(3)]
        res = self.get_output_lines(str(self.TEST_DIR), "json")

        self.assertSequenceEqual(res, expected_res)

    def test_extra_slash_path(self):
        expected_res = [str(self.TEST_DIR / f'dir{i}' / 'file1.json') for i in range(3)]
        res = self.get_output_lines(f"{self.TEST_DIR}/", ".json")

        self.assertSequenceEqual(res, expected_res)

    def test_no_files(self):
        expected_res = []
        res = self.get_output_lines(str(self.TEST_DIR), ".pdf")

        self.assertSequenceEqual(res, expected_res)

    def test_directory_does_not_exist(self):
        with self.assertRaises(NotADirectoryError):
            _ = self.get_output_lines(str(self.TEST_DIR / 'not_existed_dir'), ".txt")

    def test_incorrect_extension_double_extsep(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines(str(self.TEST_DIR), ".txt.json")

    def test_extra_args(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines(str(self.TEST_DIR), ".txt", ".json")

    def test_flaw_args(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines(str(self.TEST_DIR))


main = main(unittest_main)
