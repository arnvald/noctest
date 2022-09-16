from noctest.expectation import expect

class TestNumbers:

    def test_numbers(self):
        sth = 1 + 2
        expect(sth).toEqual(3)

    def test_numbers_wrong(self):
        sth = 1 + 2
        expect(sth).toEqual(4)
