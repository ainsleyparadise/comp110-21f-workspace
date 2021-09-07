"""Counting letters in a string."""

__author__ = "730402784"


# Begin your solution here...

question: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
i: int = 0
length: int = len(word)


while i < length:
    print("Count: " + str(i))
    i = i + 1