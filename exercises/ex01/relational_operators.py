"""Writing relational operations with inputs"""

__author__ = "730402784"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
less_than: bool = (left < right)
less_equal: bool = (left >= right)
equal: bool = (left == right)
not_equal: bool = (left != right)

print(str(left) + " < " + str(right) + " is " + str(less_than))
print(str(left) + " >= " + str(right) + " is " + str(less_equal))
print(str(left) + " == " + str(right) + " is " + str(equal))
print(str(left) + " != " + str(right) + " is " + str(not_equal))
