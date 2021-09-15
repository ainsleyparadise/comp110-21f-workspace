"""Drawing forests in a loop."""

__author__ = "123456789"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
depth: int = int(input("Depth: "))
counter: int = 1
nothing: str = ""

if counter <= 0:
    print(nothing)
while counter <= depth:
    print(TREE + nothing)
    counter = counter + 1
    nothing += TREE + ""
