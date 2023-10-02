from unittest import TestCase
from unittest import main as unittest_main
from main_decorator import main
from math import inf, log

from tasks.task1.prints import main as test_main

from test_tools import AssertBetweenMixin, AssertLenEqualMixin, IoTestCaseMixin


class TestPrints(
    AssertBetweenMixin,
    AssertLenEqualMixin,
    IoTestCaseMixin,
    TestCase
):

    @classmethod
    def get_output_lines(cls, input_lines=('',)):
        with super().get_output_lines(input_lines=input_lines) as output_lines:
            test_main()

        return output_lines

    def test_lines_count(self):
        lines = self.get_output_lines()

        self.assertLenEqual(lines, 3)

    def test_hello_world(self):
        lines = self.get_output_lines()

        expected_res = "Hello, world!"
        res = lines[0]
        self.assertEqual(res, expected_res)

    def test_andhiagain(self):
        lines = self.get_output_lines()

        expected_res = "Andhiagain!"
        res = lines[1]
        self.assertEqual(res, expected_res)

    def test_exclamation_marks(self):
        lines = self.get_output_lines()

        res = lines[2]
        expected_res = '!' * len(res)

        self.assertEqual(res, expected_res)

    def test_exclamation_marks_count(self):
        tmp_min = inf
        tmp_max = -inf

        get_marks_count = lambda: len(self.get_output_lines()[2])

        min_count = 5
        max_count = 50

        length = max_count - min_count + 1

        allowable_error = 1e-9

        # If there is a probability of getting a number outside the range, it will be at least length / (length + 1)
        # each time. Therefore, to obtain an acceptable error, needed to calculate the logarithm using this base.
        iterations_count = int(log(allowable_error, length / (length + 1)))

        for i in range(iterations_count):
            count = get_marks_count()

            if tmp_min > count:
                tmp_min = count

            if tmp_max < count:
                tmp_max = count

        self.assertBetween(tmp_min, min_count, max_count)
        self.assertBetween(tmp_max, min_count, max_count)


main = main(unittest_main)
