from noctest.expectation import expect

def test_num_success():
    expect(1+1).toEqual(2)

def test_num_failure():
    expect(1+1).toEqual(1)

