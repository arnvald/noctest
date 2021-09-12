from noctest.expectation import expect

def test_success():
    expect(True).toEqual(True)

def test_not_equal_success():
    expect(True).notToEqual(False)

def test_failure():
    expect(False).toEqual(True)

def test_not_equal_failure():
    expect(True).notToEqual(True)

