class AssertLenEqualMixin:
    def assertLenEqual(self, col, length, msg=None):
        if not (len(col) == length):
            msg = self._formatMessage(msg, f"col length equals {len(col)}, not {length}")
            raise self.failureException(msg)
