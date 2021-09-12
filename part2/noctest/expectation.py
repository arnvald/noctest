import operator

def expect(value):
    return Expectation(value)

class FailedExpectationError(RuntimeError):
    def __init__(self, message):
        self.message = message

class Expectation:
    def __init__(self, value):
        self.value = value

    def toEqual(self, comparison):
        self._assert(comparison, operator.eq, "to equal")

    def notToEqual(self, comparison):
        self._assert(comparison, operator.is_not, "not to equal")

    def toInclude(self, element):
        self._assert(element, operator.contains, "to include")

    def notToInclude(self, element):
        def not_include(ls, el):
            return el not in ls
        self._assert(element, not_include, "not to include")

    def _assert(self, comparison, op, message):
        if not op(self.value, comparison):
            raise FailedExpectationError(f"expected {self.value} {message} {comparison}")
