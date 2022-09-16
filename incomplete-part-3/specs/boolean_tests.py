from noctest.expectation import expect

class TestBooleans:

    def test_correct(self):
        expect(True).toEqual(True)

    def test_wrong(self):
        expect(True).toEqual(False)
