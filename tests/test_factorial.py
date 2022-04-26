import pytest
from mymath.factorial import factorial

@pytest.mark.parametrize(
    "test, expected",
    [
        (3, 6), (5, 120), (10, 3628800)
    ])
def test_factorial_positive_integers(test, expected):
    assert factorial(test) == expected

def test_factorial_negative1():
    with pytest.raises(ValueError):
        factorial(-1)
