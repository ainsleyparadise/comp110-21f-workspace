"""Writing numeric operators with inputs"""

__author__ = "730402784"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
exp: int = int(left ** right)
div_float: str = str(left / right)
div_floor: int = int(left // right)
div_rem: int = int(left % right)

print(str(left) + " ** " + str(right) + " is " + str(exp))
print(str(left) + " / " + str(right) + " is " + str(div_float))
print(str(left) + " // " + str(right) + " is " + str(div_floor))
print(str(left) + " % " + str(right) + " is " + str(div_rem))

