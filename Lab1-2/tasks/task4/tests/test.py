from unittest import TestCase

from unittest import main as unittest_main
from tasks.task4.table import get_table, main as test_main
from test_tools import ArgparseTestCaseMixin, AssertHasAttrMixin

from bs4 import BeautifulSoup
import re
from main_decorator import main
from os.path import exists as file_exists, isdir as directory_exists
from os import remove as file_delete, mkdir as create_directory
from shutil import rmtree as delete_directory
from tasks.task4.hex_rgb_converters import hex_to_rgb, rgb_to_hex


class TestHexRgbConverters(TestCase):
    def test_to_rgb_normal(self):
        color = "#FEFF01"

        expected_res = (254, 255, 1)
        res = hex_to_rgb(color)

        self.assertSequenceEqual(res, expected_res)

    def test_to_rgb_extra_len(self):
        color = "#FEFF015"

        with self.assertRaises(ValueError):
            _ = hex_to_rgb(color)

    def test_to_rgb_flaw_len(self):
        color = "#FEFF0"

        with self.assertRaises(ValueError):
            _ = hex_to_rgb(color)

    def test_to_rgb_no_sharp(self):
        color = "FEFF01"

        with self.assertRaises(ValueError):
            _ = hex_to_rgb(color)

    def test_to_rgb_no_16_base(self):
        color = "#WAF014"

        with self.assertRaises(ValueError):
            _ = hex_to_rgb(color)

    def test_to_hex_normal(self):
        color = (254, 255, 1)

        expected_res = "#FEFF01"
        res = rgb_to_hex(color)

        self.assertSequenceEqual(res, expected_res)

    def test_to_hex_extra_len(self):
        color = (254, 255, 1, 45)

        with self.assertRaises(ValueError):
            _ = rgb_to_hex(color)

    def test_to_hex_flaw_len(self):
        color = (254, 255)

        with self.assertRaises(ValueError):
            _ = rgb_to_hex(color)

    def test_to_hex_more_than_255(self):
        color = (256, 0, 0)

        with self.assertRaises(ValueError):
            _ = rgb_to_hex(color)

    def test_to_hex_negative(self):
        color = (-1, 0, 0)

        with self.assertRaises(ValueError):
            _ = rgb_to_hex(color)


class TestTable(ArgparseTestCaseMixin, AssertHasAttrMixin, TestCase):
    @classmethod
    def get_html(cls):
        return BeautifulSoup(get_table(), "html.parser")

    def test_has_table(self):
        parsed_html = self.get_html()
        self.assertHasAttr(parsed_html, 'table')

    def test_only_rows(self):
        parsed_html = self.get_html()

        for row in [elem for elem in parsed_html.table.children if str(elem).strip()]:
            # Check that element is row.
            self.assertHasAttr(row, 'tr')

            for table_data in [elem for elem in row.children if str(elem).strip()]:
                # Check that element is table data.
                self.assertHasAttr(table_data, 'td')

    @classmethod
    def get_rows(cls):
        parsed_html = cls.get_html()
        return [elem for elem in parsed_html.table.children if str(elem).strip()]

    def test_white_black_gradient(self):
        rows = self.get_rows()

        color_dict = {
            'white': "#FFFFFF",
            'black': "#000000",
            'silver': "#C0C0C0",
            'gray': "#808080",
            'light gray': "#D3D3D3",
            'dark gray': "#A9A9A9",
        }

        tmp_color = (255, 255, 255) # White

        for row in rows:
            if match := re.match(r"background\s*:\s*([^;]*?)\s*;", row['style']):
                color = match[1]

                if new_color := color_dict.get(color.lower()):
                    color = new_color
            else:
                color = color_dict['white']

            color = hex_to_rgb(color)

            if color.count(color[0]) != 3:
                raise self.failureException(f"{color} color is not shade of gray.")

            if not all(color[i] <= tmp_color[i] for i in range(3)):
                raise self.failureException(f"The gradient is not gradual.")
            else:
                tmp_color = color


class TestFiles(TestCase):
    def setUp(self):
        if file_exists("data_file.txt"):
            file_delete("data_file.txt")

    def tearDown(self):
        if file_exists("data_file.txt"):
            file_delete("data_file.txt")

        if file_exists("data_file.json"):
            file_delete("data_file.json")

        if directory_exists("data_file"):
            delete_directory("data_file")

    def test_file_not_exist(self):
        test_main()

        if not file_exists("data_file.txt"):
            raise self.failureException(f"data_file.txt does not exists.")

    def test_file_exist(self):
        with open("data_file.txt", "w+") as file:
            file.write("123")

        test_main()

        if not file_exists("data_file.txt"):
            raise self.failureException(f"data_file.txt does not exists.")

    def test_file_exist_with_other_extension(self):
        with open("data_file.json", "w+") as file:
            file.write("123")

        test_main()

        if not file_exists("data_file.txt"):
            raise self.failureException(f"data_file.txt does not exists.")

    def test_directory_exist(self):
        create_directory("data_file")

        test_main()

        if not file_exists("data_file.txt"):
            raise self.failureException(f"data_file.txt does not exists.")


main = main(unittest_main)
