from unittest import TestCase
from unittest import main as unittest_main
from main_decorator import main
from tasks.task3.rectangle import main as test_main
from test_tools import ArgparseTestCaseMixin


class TestRectangle(ArgparseTestCaseMixin, TestCase):
    @classmethod
    def get_output_lines(cls, *args):
        with super().get_output_lines(*args) as output_lines:
            test_main()

        return output_lines

    def test_normal(self):
        output = self.get_output_lines("10", "11")

        self.assertEqual(output[0], '110.0')

    def test_no_args(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines()

    def test_extra_args(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("123", "345", "567")

    def test_not_numeric_arg(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("23", "er")

    def test_negative_arg(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("23", "-45")

    def test_zero_arg(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("23", "0")

    def test_nan_arg(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("nan", "45")

    def test_inf_arg(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("inf", "45")

    def test_overflow(self):
        with self.assertRaises(ValueError):
            _ = self.get_output_lines("1E200", "1E200")


main = main(unittest_main)
