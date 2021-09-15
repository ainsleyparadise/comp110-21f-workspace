"""Finding duplicate letters in a word."""

__author__ = "730402784"

word: str = str(input("Enter a word: "))
x: int = 0
y: int = 0
a: str = str(word[x])
b: str = str(word[y])
duplicate: bool = True


while x < len(word) and y <= len(word):
    if word[x] == word[y] and a != b:
        duplicate = True
    else:
        x = x + 1
        y = y + 1
        
print("Found duplicate: " + str(duplicate))
