class AssertHasAttrMixin:
    def assertHasAttr(self, obj, attr, msg=None):
        if not hasattr(obj, attr):
            msg = self._formatMessage(msg, f"{obj} has no {attr} attribute.")
            raise self.failureException(msg)
