import argparse
from contextlib import contextmanager
import io
from unittest.mock import patch
from contextlib import redirect_stderr


class ArgparseTestCaseMixin:
    @staticmethod
    @contextmanager
    def get_output_lines(*args):
        output_lines = []

        with redirect_stderr(argparse_hidden_errors_stream := io.StringIO()):
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                with patch('argparse._sys.argv', ['', *args]):
                    try:
                        yield output_lines
                    finally:
                        output_lines += fake_stdout.getvalue().splitlines()
