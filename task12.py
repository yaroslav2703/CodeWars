def zero(act=None):  # your code here
    if act is None:
        return 0
    else:
        return operation(0, act)


def one(act=None):  # your code here
    if act is None:
        return 1
    else:
        return operation(1, act)


def two(act=None):  # your code here
    if act is None:
        return 2
    else:
        return operation(2, act)


def three(act=None):  # your code here
    if act is None:
        return 3
    else:
        return operation(3, act)


def four(act=None):  # your code here
    if act is None:
        return 4
    else:
        return operation(4, act)


def five(act=None):  # your code here
    if act is None:
        return 5
    else:
        return operation(5, act)


def six(act=None):  # your code here
    if act is None:
        return 6
    else:
        return operation(6, act)


def seven(act=None):  # your code here
    if act is None:
        return 7
    else:
        return operation(7, act)


def eight(act=None):  # your code here
    if act is None:
        return 8
    else:
        return operation(8, act)


def nine(act=None):  # your code here
    if act is None:
        return 9
    else:
        return operation(9, act)


def plus(operator):  # your code here
    return [operator, '+']


def minus(operator):  # your code here
    return [operator, '-']


def times(operator):  # your code here
    return [operator, '*']


def divided_by(operator):  # your code here
    return [operator, '//']


def operation(first, act):
    if act[1] == '+':
        return first + act[0]
    elif act[1] == '-':
        return first - act[0]
    elif act[1] == '//':
        return first // act[0]
    elif act[1] == '*':
        return first * act[0]


print(four(plus(eight())))
print(seven(times(five())))
print(nine(divided_by(two())))

