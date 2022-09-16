from noctest.expectation import expect

class TestStrings:

    def before_all(self):
        self.test_number = 0

    def before(self):
        self.test_number += 1
        print(f"running test {self.test_number}")

    def after(self):
        print("cleaning up after a single test")

    def after_all(self):
        print("cleaning up after all tests")

    def test_strings(self):
        sth = "randomtext"
        expect(sth).toEqual("randomtext")

    def test_strings_wrong(self):
        sth = "randomtext"
        expect(sth).toEqual("wrong value")

    def test_strings_not_equal(self):
        sth = "mytext"
        expect(sth).notToEqual("notmytext")

    def test_strings_not_equal_wrong(self):
        sth = "mytext"
        expect(sth).notToEqual("mytext")
