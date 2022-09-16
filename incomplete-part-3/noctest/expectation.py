import operator

def expect(value):
    return Expectation(value)

class FailedExpectation(RuntimeError):
    def __init__(self, message):
        self.message = message

class Expectation():
    def __init__(self, value):
        self.value = value

    def toEqual(self, comp):
        return self._assert(comp, operator.eq)

    def notToEqual(self, comp):
        return self._assert(comp, operator.is_not)

    def _assert(self, comp, op):
        if not op(self.value, comp):
            raise FailedExpectation(
                f"expected {self.value} {self._operator_word(op)} {comp}")
        return True

    def _operator_word(self, op):
        if op == operator.eq:
            return "to equal"
        if op == operator.is_not:
            return "not to equal"
