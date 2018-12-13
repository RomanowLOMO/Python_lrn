import pytest
from test_lrn.my_func_for_tests import my_function


def test_rle_py():
    assert my_function.rle('mississippi') == [
        ('m', 1), ('i', 1), ('s', 2), ('i', 1),
        ('s', 2), ('i', 1), ('p', 2), ("i", 1)
    ]


def test_rle_empty_py():
    assert list(my_function.rle("")) == []

