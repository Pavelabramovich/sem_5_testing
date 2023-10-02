from unittest import TestCase
from unittest import main as unittest_main

from main_decorator import main
from tasks.task2.people import main as test_main
from test_tools import AssertNotRaisesMixin, AssertLenEqualMixin, IoTestCaseMixin


class TestPeople(
    AssertLenEqualMixin,
    AssertNotRaisesMixin,
    IoTestCaseMixin,
    TestCase
):
    @classmethod
    def get_output_lines(cls, input_lines=('',)):
        with super().get_output_lines(input_lines=input_lines) as output_lines:
            test_main()

        return output_lines

    def test_strings_count(self):
        output = self.get_output_lines([
            "vasua petrov 34",
            "petya vasuliev 56",
            "vova vovochkin 45",
            ''
        ])

        self.assertLenEqual(output, 6)

    def test_ages_format(self):
        output = self.get_output_lines([
            "vasua petrov 34",
            "petya vasuliev 56",
            "vova vovochkin 45",
            ''
        ])

        *people, min_age, max_age, average_age, = output

        with self.assertNotRaises(ValueError):
            _ = int(min_age)
            _ = int(max_age)
            _ = float(average_age)

    @classmethod
    def get_deconstructed_output(cls, input=['']):
        *people, min_age, max_age, average_age, = cls.get_output_lines(input)

        return {
            'average_age': float(average_age),
            'max_age': int(max_age),
            'min_age': int(min_age),
            'people': people
        }

    def test_min_age(self):
        output = self.get_deconstructed_output([
            "vasua petrov 34",
            "petya vasuliev 56",
            "vova vovochkin 45",
            ''
        ])

        self.assertEqual(output['min_age'], 34)

    def test_max_age(self):
        output = self.get_deconstructed_output([
            "vasua petrov 34",
            "petya vasuliev 56",
            "vova vovochkin 45",
            ''
        ])

        self.assertEqual(output['max_age'], 56)

    def test_average_age(self):
        output = self.get_deconstructed_output([
            "vasua petrov 34",
            "petya vasuliev 56",
            "vova vovochkin 45",
            ''
        ])

        self.assertEqual(output['average_age'], (34 + 56 + 45) / 3)

    def test_people(self):
        output = self.get_deconstructed_output([
            "vasua petrov 34",
            "petya vasuliev 56",
            "vova vovochkin 45",
            ''
        ])

        expected_res = [
            "vasua 34 petrov",
            "petya 56 vasuliev",
            "vova 45 vovochkin",
        ]

        res = output['people']

        self.assertSequenceEqual(res, expected_res)

    def test_no_name(self):
        with self.assertRaises(ValueError):
            people = self.get_output_lines([
                "vasua petrov 34",
                "petya vasuliev 56",
                "vovochkin 45",
                ''
            ])

    def test_no_age(self):
        with self.assertRaises(ValueError):
            people = self.get_output_lines([
                "vasua petrov 34",
                "petya vasuliev 56",
                "vovochkin vavav",
                ''
            ])

    def test_jumble_age(self):
        with self.assertRaises(ValueError):
            people = self.get_output_lines([
                "vasua petrov 34",
                "petya vasuliev sfdgv",
                "vovochkin vavav 45",
                ''
            ])

    def test_negative_age(self):
        with self.assertRaises(ValueError):
            people = self.get_output_lines([
                "vasua petrov 34",
                "petya vasuliev 67",
                "vovochkin vavav -45",
                ''
            ])

    def test_zero_age(self):
        with self.assertRaises(ValueError):
            people = self.get_output_lines([
                "vasua petrov 34",
                "petya vasuliev 4",
                "vovochkin vavav 0",
                ''
            ])


main = main(unittest_main)
