def dig_pow(n, p):
    digits = list(str(n))
    q = 0
    for index, digit in enumerate(digits):
        q = q + int(digit) ** (p + index)
    if q % n == 0:
        return q // n
    else:
        return -1


print(dig_pow(89, 1))
print(dig_pow(92, 1))
print(dig_pow(46288, 3))
