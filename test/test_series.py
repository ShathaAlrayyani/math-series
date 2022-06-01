import pytest
from math_series.series import fibonacci


def test_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_2():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_3():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected
