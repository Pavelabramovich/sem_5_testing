class AssertBetweenMixin:
    def assertBetween(self, value, left, right, msg=None):
        if not (left <= value <= right):
            msg = self._formatMessage(msg, f"{value} not between {left} and {right}")
            raise self.failureException(msg)
