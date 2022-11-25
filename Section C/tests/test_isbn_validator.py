import isbn_validator

# Tests valid ISBN-13
def test_product_sum_13_true():
    validator_test = isbn_validator.isbn_number_validator("9780316066525")
    assert validator_test == True

# Tests invalid ISBN-13
def test_product_sum_13_false():
    validator_test = isbn_validator.isbn_number_validator("9780316066524")
    assert validator_test == False

# Tests valid ISBN-10
def test_product_sum_10_true():
    validator_test = isbn_validator.isbn_number_validator("0316066524")
    assert validator_test == True

# Tests invalid ISBN-10
def test_product_sum_10_false():
    validator_test = isbn_validator.isbn_number_validator("0330301824")
    assert validator_test == False