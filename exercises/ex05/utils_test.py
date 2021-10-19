"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730402784"


def test_only_evens_edge() -> None:
    """Only Evens Test 1."""
    list1: list[int] = [1, 2, 3]
    assert only_evens(list1) == [2]


def test_only_evens_use1() -> None:
    """Only Evens Test 2."""
    list2: list[int] = []
    assert only_evens(list2) == []


def test_only_evens_use2() -> None:
    """Only Evens Test 3."""
    list3: list[int] = [1, 5, 8, 12, 13]
    assert only_evens(list3) == [8, 12]


def test_sub_edge() -> None:
    """Sub Test 1."""
    a_list: list[int] = [0, 5, 10, 15]
    assert sub(a_list, 1, 3) == [5, 10]


def test_sub_use1() -> None:
    """Sub Test 2."""
    a_list: list[int] = []
    assert sub(a_list, 0, 3) == []


def test_sub_use2() -> None:
    """Sub Test 3."""
    a_list: list[int] = [1, 2, 3, 4, 5]
    assert sub(a_list, 1, 4) == [2, 3, 4]


def test_concat_edge() -> None:
    """Concat Test 1."""
    d: list[int] = [1, 2, 3]
    e: list[int] = [4, 5, 6]
    assert concat(d, e) == [1, 2, 3, 4, 5, 6]


def test_concat_use1() -> None:
    """Concat Test 2."""
    d: list[int] = []
    e: list[int] = [1]
    assert concat(d, e) == [1]


def test_concat_use2() -> None:
    """Concat Test 3."""
    d: list[int] = [10, 7, 5, 6, 3]
    e: list[int] = [1, 4, 2]
    assert concat(d, e) == [10, 7, 5, 6, 3, 1, 4, 2]
