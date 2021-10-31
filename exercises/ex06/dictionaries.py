"""Practice with dictionaries."""

__author__ = "730402784"

# Define your functions below


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Function that inverts the keys and values of a dictionary."""
    dict2: dict[str, str] = {}
    for key in dict1:
        new_key: str = dict1[key]
        if new_key in dict2:
            raise KeyError("Each key must be unique!")
        dict2[new_key] = key

    return dict2


def favorite_color(dict3: dict[str, str]) -> str:
    """Function that returns the common favorite color."""
    dict4: dict[str, str] = {}
    color = str(dict4)
    i = 0
    j = 1
    for key in dict3:
        if dict3[key] == dict3[key]:
            color = dict3[key]
            i = i + 1
            j = j + 1
        else:
            i = i + 1
            j = j + 1
    
    return color


def count(list1: list[str]) -> dict[str, int]:
    """Function that counts the number of times a value is present."""
    dict5: dict[str, int] = {}
    i = 0
    while i < len(list1):
        if list1[i] in dict5:
            dict5[list1[i]] += 1
        else:
            dict5[list1[i]] = 1
        i += 1

    return dict5