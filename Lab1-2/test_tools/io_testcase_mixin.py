from contextlib import contextmanager
import io
from unittest.mock import patch


class IoTestCaseMixin:
    @staticmethod
    @contextmanager
    def get_output_lines(input_lines=('',)):
        output_lines = []

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            with patch('builtins.input', side_effect=input_lines):
                try:
                    yield output_lines
                finally:
                    output_lines += fake_stdout.getvalue().splitlines()
