"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def all(xs: list[int], number: int) -> bool:
    """Function saying whether the ints are the same."""
    i: int = 0
    if len(xs) == 0:
        return False
    else:
        while i < len(xs):
            if xs[i] == number:
                i += 1
            else:
                return False
        return True
    

def is_equal(a: list[int], b: list[int]) -> bool:
    """Function determining if lists are equal."""
    i: int = 0
    if len(a) != len(b):
        return False
    else:
        while i < len(a):
            if a[i] == b[i]:
                i += 1
            else:
                return False
        return True


def max(input: list[int]) -> int:
    """Function determining max."""
    i: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        while i <= len(input):
            if input[i] <= input[i + 1]:
                i += 1
            else:
                return int(input[i])
