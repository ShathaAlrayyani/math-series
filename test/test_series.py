import pytest
from math_series.series import fibonacci

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_2():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected
