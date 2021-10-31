"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730402784"


def test_invert1() -> None:
    """Invert Test 1."""
    dict1 = {'UNC': 'Duke', 'Clemson': 'NC State'}
    assert invert(dict1) == {'Duke': 'UNC', 'NC State': 'Clemson'}


def test_invert2() -> None:
    """Invert Test 2."""
    dict2 = {'blue': 'yellow'}
    assert invert(dict2) == {'yellow': 'blue'}
    

def test_invert3() -> None:
    """Invert Test 3."""
    dict3 = {'x': 'y'}
    assert invert(dict3) == {'y': 'x'}


def test_favorite_color1() -> None:
    """Favorite Color Test 1."""
    dict4 = {'Amanda': 'blue', 'Samantha': 'blue', 'Jenna': 'yellow'}
    assert favorite_color(dict4) == 'blue'


def test_favorite_color2() -> None:
    """Favorite Color Test 2."""
    dict5 = {'Anne': 'red', 'Anna': 'purple', 'Emily': 'red'}
    assert favorite_color(dict5) == 'red'


def test_favorite_color3() -> None:
    """Favorite Color Test 3."""
    dict6 = {'Caroline': 'green', 'Riley': 'black', 'Isabella': 'black', 'Forbes': 'green'}
    assert favorite_color(dict6) == 'green'


def test_count1() -> None:
    """Count Test 1."""
    list1 = ['Virginia', 'Sarah', 'Margaret', 'Katie', 'Margaret', 'Sarah']
    assert count(list1) == {'Virginia': 1, 'Sarah': 2, 'Margaret': 2, 'Katie': 1}


def test_count2() -> None:
    """Count Test 2."""
    list2 = ['Anne', 'Addie']
    assert count(list2) == {'Anne': 1, 'Addie': 1}


def test_count3() -> None:
    """Count Test 3."""
    list3 = ['bed', 'chair', 'chair', 'table', 'chair']
    assert count(list3) == {'bed': 1, 'chair': 3, 'table': 1}