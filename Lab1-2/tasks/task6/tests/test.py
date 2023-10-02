from unittest import TestCase
from unittest import main as unittest_main

import requests
from main_decorator import main
from tasks.task6.saving_from_url import main as test_main
from test_tools import ArgparseTestCaseMixin
from pathlib import Path

from os.path import exists as file_exists, isdir as directory_exists
from os import remove as file_delete, mkdir as create_directory
from shutil import rmtree as delete_directory


class TestParseFiles(ArgparseTestCaseMixin, TestCase):
    TEST_DIR = Path(__file__).resolve().parent / 'test_dir'

    @classmethod
    def run_test_main(cls, *args):
        with super().get_output_lines(*args):
            test_main()

    def setUp(self):
        if not directory_exists(self.TEST_DIR):
            create_directory(self.TEST_DIR)

    def tearDown(self):
        delete_directory(self.TEST_DIR)

    def test_normal(self):
        self.run_test_main("https://htmlbook.ru/files/images/html/tag_form_1.png", str(self.TEST_DIR))

        if not file_exists(self.TEST_DIR / 'tag_form_1.png'):
            raise self.failureException(f"File don't saved.")

    def test_not_file(self):
        self.run_test_main("https://htmlbook.ru/files/images", str(self.TEST_DIR))

        if not file_exists(self.TEST_DIR / 'images.html'):
            raise self.failureException(f"File don't saved.")

    def test_invalid_image(self):
        with self.assertRaises(requests.exceptions.RequestException):
            self.run_test_main("https://htmlbook.ru/files/images/html/tag_invalid_1.png", str(self.TEST_DIR))

    def test_invalid_url(self):
        with self.assertRaises(requests.exceptions.InvalidURL):
            self.run_test_main("https://", str(self.TEST_DIR))

    def test_directory_does_not_exist(self):
        with self.assertRaises(NotADirectoryError):
            self.run_test_main("https://htmlbook.ru/files/images/html/tag_form_1.png",
                               str(self.TEST_DIR / 'not_existed_dir'))

    def test_extra_args(self):
        with self.assertRaises(ValueError):
            self.run_test_main("https://htmlbook.ru/files/images/html/tag_form_1.png", str(self.TEST_DIR), "356")

    def test_flaw_args(self):
        with self.assertRaises(ValueError):
            self.run_test_main("https://htmlbook.ru/files/images/html/tag_form_1.png" + str(self.TEST_DIR))


main = main(unittest_main)
