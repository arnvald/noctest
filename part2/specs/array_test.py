from noctest.expectation import expect

def test_inclusion():
    expect([1,2,3]).toInclude(2)

def test_exclusion_fail():
    expect([1,2,3]).notToInclude(2)

def test_exclusion_success():
    expect([1,2,3]).notToInclude(5)
