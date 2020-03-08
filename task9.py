import math


def is_square(n):
    return True if n >= 0 and str(math.sqrt(n)).split('.')[1] == '0' else False


print(is_square(-1))
print(is_square(25))
print(is_square(26))
print(is_square(144))
print(is_square(8532))
