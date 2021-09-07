"""Repeating a beat in a loop."""

__author__ = "730402784"


# Begin your solution here...

beat: str = input("What beat do you want to repeat? ")
question: int = int(input("How many times do you want to repeat it? "))
counter: int = 1

if question <= 0:
    print("No beat...")
while counter <= question:
    counter = counter + 1
    print(beat)
