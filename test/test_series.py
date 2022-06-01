import pytest
import math_series.series

def test_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
