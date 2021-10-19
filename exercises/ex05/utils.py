"""List utility functions part 2."""

__author__ = "730402784"

# Define your functions below


def only_evens(a: list[int]) -> list[int]:
    """Finds the even numbers of a list."""
    i: int = 0
    list1: list[int] = []
    
    while i < len(a):
        if a[i] % 2 == 0:
            list1.append(a[i])
        i += 1
    return list1


def sub(a_list: list[int], b: int, c: int) -> list[int]:
    """Generates subset of a list between the parameters."""
    i: int = 0
    list2: list[int] = []

    if b < 0:
        b = 0
    if c > len(a_list):
        c = len(a_list)
    if b < len(a_list) and b < c:
        while i < len(a_list):
            if a_list[b] <= a_list[i] < a_list[c]:
                list2.append(a_list[i])
        i += 1
    if len(a_list) == 0 or b > len(a_list) or c <= 0:
        b = 0
        c = 1
        list2 = []
    
    return list2


def concat(d: list[int], e: list[int]) -> list[int]:
    """Concatonates two lists together."""
    i: int = 0
    j: int = 0
    list3: list[int] = []
    while i < len(d):
        list3.append(d[i])
        i += 1
    while j < len(e):
        list3.append(e[j])
        j += 1
    return list3
