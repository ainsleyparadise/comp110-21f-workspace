"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730402784"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
random: int = int(randint(1, 4))

print("Your fortune cookie says... ")


if random == 1:
    print("Today is going to be the best day ever!!")
else:
    if random == 2:
        print("Someone special is coming to you today!!")
    else:
        if random == 3:
            print("Keep your head up, great things are coming your way!")
        else:
            print("Your smile is beautiful, show it more!")

print("Now, go spread positive vibes!")