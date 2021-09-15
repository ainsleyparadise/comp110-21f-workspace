"""An exercise in remainders and boolean logic."""

__author__ = "730402784"


# Begin your solution here...

number: int = int(input("Enter an int: "))
tar: bool = bool(number % 2 == 0)
heel: bool = bool(number % 7 == 0)
empty: str = ""


if tar is True and heel is True:
    print("TAR HEELS")
else:
    if tar is True:
        print("TAR")
    if heel is True:
        print("HEELS")
    if tar is False and heel is False:
        print("CAROLINA")
