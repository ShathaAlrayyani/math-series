import pytest
from math_series.series import fibonacci, lucas, sum_series


def test_fibonacci1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci2():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci3():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


# Tests for lucas function:
def test_lucas1():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas2():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas3():
    actual = lucas(5)
    expected = 11
    assert actual == expected


# Tests for sum_series function
def test_sum_series1():
    actual = sum_series(0)
    expected = 0
    assert actual == expected
